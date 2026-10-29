import base64
import io
import os
from datetime import datetime

import requests
import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="SlootWacht", page_icon="🌿", layout="wide")
st.title("🌿 SlootWacht")
st.write("AI-ondersteunde visuele inspectie van sloten — geen meting van waterkwaliteit.")

WORKSPACE = "milous-workspace"
WORKFLOW = "slootwacht-yfyfg"
COLORS = {"drijvend_afval": "#ef4444", "dichte_waterplant": "#22c55e", "brug_afvoer": "#3b82f6"}

with st.sidebar:
    st.header("Roboflow-instellingen")
    st.write(f"Workflow: **{WORKSPACE}/{WORKFLOW}**")
    api_key = st.text_input("Roboflow API-key", type="password", value=os.getenv("ROBOFLOW_API_KEY", ""))
    confidence = st.slider("Minimale confidence", 0.1, 0.9, 0.3, 0.05)
    st.caption("De sleutel wordt niet opgeslagen in het Python-bestand. Zet je sleutel nooit op GitHub.")


def get_predictions(response_json):
    """Find object-detection predictions in Roboflow Workflows output."""
    outputs = response_json.get("outputs", []) if isinstance(response_json, dict) else []
    for output in outputs:
        if not isinstance(output, dict):
            continue
        for value in output.values():
            if isinstance(value, dict) and isinstance(value.get("predictions"), list):
                return value["predictions"]
            if isinstance(value, list) and value and isinstance(value[0], dict) and "class" in value[0]:
                return value
    return []


def priority(predictions):
    counts = {name: 0 for name in COLORS}
    for p in predictions:
        name = p.get("class", "")
        if name in counts:
            counts[name] += 1
    if counts["drijvend_afval"] >= 3:
        return "Hoog", "Meerdere afvalobjecten zichtbaar; inspectie aanbevolen.", counts
    if counts["drijvend_afval"] or counts["dichte_waterplant"] >= 2:
        return "Middel", "Afval of veel waterplanten zichtbaar; handmatige controle aanbevolen.", counts
    if any(counts.values()):
        return "Laag", "Enkele doelobjecten gedetecteerd; periodieke controle.", counts
    return "Onbekend", "Geen doelobjecten gedetecteerd; dit bewijst niet dat de sloot schoon is.", counts


uploaded = st.file_uploader("Upload een nieuwe slootfoto (jpg/png)", type=["jpg", "jpeg", "png"])
if uploaded is not None:
    image = Image.open(io.BytesIO(uploaded.getvalue())).convert("RGB")
    st.image(image, caption="Geüploade foto", use_container_width=True)
    if st.button("Analyseer foto", type="primary"):
        if not api_key.strip():
            st.warning("Vul links je Roboflow API-key in.")
            st.stop()
        buf = io.BytesIO()
        image.save(buf, format="JPEG", quality=90)
        encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
        endpoint = f"https://serverless.roboflow.com/infer/workflows/{WORKSPACE}/{WORKFLOW}"
        try:
            with st.spinner("Roboflow analyseert de foto..."):
                response = requests.post(
                    endpoint,
                    json={"api_key": api_key.strip(), "inputs": {"image": {"type": "base64", "value": encoded}}},
                    timeout=90,
                )
                response.raise_for_status()
                result = response.json()
        except requests.HTTPError:
            st.error(f"Roboflow gaf HTTP {response.status_code}. Controleer je API-key en of de workflow is gepubliceerd.")
            st.stop()
        except requests.RequestException as exc:
            st.error(f"Verbindingsfout: {type(exc).__name__}. Controleer internet en probeer opnieuw.")
            st.stop()
        predictions = [p for p in get_predictions(result) if float(p.get("confidence", 0)) >= confidence]
        rendered = image.copy()
        draw = ImageDraw.Draw(rendered)
        for p in predictions:
            try:
                x, y, w, h = (float(p[k]) for k in ("x", "y", "width", "height"))
                cls = str(p.get("class", "onbekend"))
                conf = float(p.get("confidence", 0))
                color = COLORS.get(cls, "#f59e0b")
                draw.rectangle((x-w/2, y-h/2, x+w/2, y+h/2), outline=color, width=max(3, image.width // 200))
                draw.text((x-w/2, max(0, y-h/2-18)), f"{cls} {conf:.0%}", fill=color)
            except (KeyError, TypeError, ValueError):
                continue
        level, advice, counts = priority(predictions)
        st.success("Roboflow-workflow uitgevoerd!")
        st.subheader(f"Inspectieprioriteit: {level}")
        st.write(advice)
        st.image(rendered, caption="AI-detecties", use_container_width=True)
        st.write("Detecties:", counts)
        if not predictions:
            st.info("Geen detecties boven de gekozen drempel. Controleer eventueel de workflow-output in Roboflow.")
        report = "\n".join([
            "SlootWacht - inspectierapport",
            f"Datum: {datetime.now().isoformat(timespec='minutes')}",
            f"Foto: {uploaded.name}",
            f"Workflow: {WORKSPACE}/{WORKFLOW}",
            f"Inspectieprioriteit: {level}",
            f"Advies: {advice}",
            *[f"{k}: {v}" for k, v in counts.items()],
            "AI-voorspellingen moeten handmatig worden gecontroleerd.",
        ])
        st.download_button("Download inspectierapport", report, file_name="slootwacht_rapport.txt", mime="text/plain")
