from contextlib import closing
from pathlib import Path
import sqlite3

import pandas as pd
import plotly.express as px
import streamlit as st

DATABASE_PATH = Path("data/pulse.db")
VALID_LABELS = ["positive", "neutral", "negative"]

st.set_page_config(
    page_title="Technology & Infrastructure Pulse",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- MODERN DARK TECH STYLING VIA CUSTOM CSS ---
st.markdown(
    """
    <style>
    /* 1. Verwijder de witte Streamlit header balk */
    header, [data-testid="stHeader"], [data-testid="stToolbar"] {
        background-color: transparent !important;
        background: transparent !important;
    }
    
    /* 2. Algemene achtergrond met diepe tech-gradient */
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 50%, #080c14 100%) !important;
        color: #f3f4f6;
    }
    
    /* 3. Header titels en labels */
    h1, h2, h3, h4, h5 {
        color: #ffffff !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
    }
    
    /* Alle widget labels helder wit maken */
    label[data-testid="stWidgetLabel"] p,
    div[data-testid="stWidgetLabel"] label,
    div[data-testid="stWidgetLabel"] p {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    /* 4. Aangepaste metric kaarten */
    .metric-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        margin-bottom: 10px;
    }
    .metric-title {
        color: #ffffff !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        margin-bottom: 6px !important;
        letter-spacing: 0.3px;
    }
    .metric-value {
        color: #ffffff !important;
        font-size: 32px !important;
        font-weight: 800 !important;
        line-height: 1.1 !important;
    }
    
    /* 5. Alert Banner met contrast */
    .custom-alert {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid #00D2FF;
        border-left: 6px solid #00D2FF;
        border-radius: 10px;
        padding: 14px 20px;
        color: #ffffff !important;
        font-size: 14.5px;
        font-weight: 500;
        margin-top: 15px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0, 210, 255, 0.15);
    }

    /* 6. Knop styling */
    div[data-testid="stButton"] button,
    div[data-testid="stBaseButton-secondary"],
    .stButton > button {
        background-color: #1e293b !important;
        background: #1e293b !important;
        color: #ffffff !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        padding: 6px 18px !important;
        font-weight: 600 !important;
        box-shadow: none !important;
    }
    div[data-testid="stButton"] button:hover,
    div[data-testid="stBaseButton-secondary"]:hover,
    .stButton > button:hover {
        background-color: #334155 !important;
        background: #334155 !important;
        border-color: #00D2FF !important;
        color: #00D2FF !important;
    }
    div[data-testid="stButton"] button:focus,
    div[data-testid="stBaseButton-secondary"]:focus,
    div[data-testid="stButton"] button:active {
        background-color: #1e293b !important;
        background: #1e293b !important;
        border-color: #00D2FF !important;
        color: #ffffff !important;
        box-shadow: none !important;
    }
    div[data-testid="stButton"] button p,
    div[data-testid="stBaseButton-secondary"] p,
    .stButton > button p {
        color: inherit !important;
        font-weight: 600 !important;
    }

    /* 7. ZOEKBALK (st.text_input) VOLLEDIG DONKER */
    div[data-testid="stTextInput"] > div > div {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        color: #ffffff !important;
    }
    div[data-testid="stTextInput"] input {
        background-color: transparent !important;
        color: #ffffff !important;
        font-size: 14px !important;
    }
    div[data-testid="stTextInput"] input::placeholder {
        color: #94a3b8 !important;
    }
    div[data-testid="stTextInput"] > div > div:focus-within {
        border-color: #00D2FF !important;
        box-shadow: 0 0 0 1px #00D2FF !important;
    }

    /* 8. MULTISELECT FILTER (st.multiselect) VOLLEDIG DONKER */
    div[data-testid="stMultiSelect"] > div > div {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        color: #ffffff !important;
    }
    div[data-testid="stMultiSelect"] span[data-baseweb="tag"] {
        background-color: #0f172a !important;
        border: 1px solid #334155 !important;
        border-radius: 6px !important;
    }
    div[data-testid="stMultiSelect"] span[data-baseweb="tag"] span {
        color: #f1f5f9 !important;
        font-weight: 500 !important;
    }

    /* 9. RADIO BUTTONS */
    div[data-testid="stRadio"] label p {
        color: #e5e7eb !important;
        font-weight: 600 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("⚡ Technology & Infrastructure Live Pulse")
st.caption(
    "Headline sentiment monitoring for SDG 9 policy officers. "
    "Collection runs periodically. Use Refresh data to load the latest saved results."
)


@st.cache_data(ttl=60)
def load_data():
    if not DATABASE_PATH.is_file():
        return pd.DataFrame()

    database_uri = DATABASE_PATH.resolve().as_uri() + "?mode=ro"
    with closing(
        sqlite3.connect(database_uri, uri=True, timeout=10)
    ) as connection:
        table = connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            ("pulse_items",),
        ).fetchone()
        if table is None:
            return pd.DataFrame()

        dataframe = pd.read_sql_query(
            """
            SELECT title, url, source, topic, published_at, fetched_at,
                   sentiment_label, sentiment_score
            FROM pulse_items
            ORDER BY fetched_at DESC
            """,
            connection,
        )

    dataframe["fetched_at"] = pd.to_datetime(
        dataframe["fetched_at"], errors="coerce", utc=True, format="mixed"
    )
    dataframe["title"] = dataframe["title"].fillna("").astype(str)
    dataframe["sentiment_label"] = (
        dataframe["sentiment_label"].astype("string").str.strip().str.lower()
    )
    dataframe["sentiment_score"] = pd.to_numeric(
        dataframe["sentiment_score"], errors="coerce"
    )
    dataframe["filter_label"] = (
        dataframe["sentiment_label"]
        .where(dataframe["sentiment_label"].isin(VALID_LABELS), "unknown")
        .fillna("unknown")
    )
    dataframe["badge_label"] = dataframe["filter_label"].map({
        "positive": "🟢 Positive",
        "neutral": "⚪ Neutral",
        "negative": "🔴 Negative",
        "unknown": "Unknown",
    })
    return dataframe


if st.button("Refresh data", help="Read the latest saved database records."):
    load_data.clear()

try:
    data = load_data()
except (sqlite3.Error, pd.errors.DatabaseError) as error:
    st.error(
        "The database could not be read. Check data/pulse.db and run the collector "
        "from the project root. Back up existing data before making changes."
    )
    with st.expander("Technical details"):
        st.code(str(error), language="text")
    st.stop()

if data.empty:
    st.warning(
        "No saved articles are available, or the database table is missing. "
        "Run the collector from the project root: python -m src.run_pipeline"
    )
    st.info("After articles are saved, click Refresh data.")
    st.stop()

st.caption(
    "Charts show headline counts grouped by collection time in UTC, not publication "
    "time or incident severity. Table filters do not change the cards or charts."
)

invalid_times = int(data["fetched_at"].isna().sum())
if invalid_times:
    st.warning(
        f"{invalid_times} article(s) have an invalid collection timestamp. "
        "They remain in the table and total counts but are excluded from time charts."
    )

unknown_labels = int(data["filter_label"].eq("unknown").sum())
if unknown_labels:
    st.warning(
        f"{unknown_labels} article(s) have an unknown sentiment label. "
        "Use the unknown filter to inspect them."
    )

subsets = {
    label: data[data["filter_label"].eq(label)] for label in VALID_LABELS
}
card_titles = [
    "📊 Total Monitored",
    "🟢 Positive Headlines",
    "⚪ Neutral Headlines",
    "🔴 Negative Headlines",
]
card_values = [len(data)] + [len(subsets[label]) for label in VALID_LABELS]
for column, title, value in zip(st.columns(4), card_titles, card_values):
    with column:
        st.markdown(
            f'<div class="metric-box"><div class="metric-title">{title}</div>'
            f'<div class="metric-value">{value} items</div></div>',
            unsafe_allow_html=True,
        )

st.divider()
header_col, selector_col = st.columns([2, 1])
with header_col:
    st.subheader("📈 Headline Counts by Predicted Sentiment")
with selector_col:
    time_granularity = st.radio(
        "Time aggregation window:",
        options=["Hourly (1h)", "Every 3 Hours (3h)", "Daily (24h)"],
        index=1,
        horizontal=True,
    )
selected_freq = {
    "Hourly (1h)": "1h",
    "Every 3 Hours (3h)": "3h",
    "Daily (24h)": "1D",
}[time_granularity]


def make_area_series(subset, freq):
    subset = subset.dropna(subset=["fetched_at"])
    if subset.empty:
        return pd.DataFrame(columns=["fetched_at", "article_count"])
    return (
        subset.set_index("fetched_at")
        .resample(freq)
        .size()
        .reset_index(name="article_count")
    )


chart_styles = {
    "positive": ("🟢 Positive Headlines", "#00F5A0", "rgba(0,245,160,0.20)"),
    "neutral": ("⚪ Neutral Headlines", "#00D2FF", "rgba(0,210,255,0.15)"),
    "negative": ("🔴 Negative Headlines", "#FF3366", "rgba(255,51,102,0.25)"),
}
for column, label in zip(st.columns(3), VALID_LABELS):
    with column:
        title, color, fill = chart_styles[label]
        st.markdown(f"##### {title}")
        series = make_area_series(subsets[label], selected_freq)
        if series.empty:
            st.info("No timestamped articles for this sentiment.")
            continue
        figure = px.area(
            series,
            x="fetched_at",
            y="article_count",
            markers=True,
            labels={
                "fetched_at": "Collected at (UTC)",
                "article_count": "Articles",
            },
        )
        figure.update_traces(
            line_color=color,
            fillcolor=fill,
            marker=dict(size=6, color=color),
        )
        figure.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=280,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis=dict(showgrid=False, color="#9ca3af"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.06)", color="#9ca3af"),
        )
        st.plotly_chart(figure, width="stretch", key=f"chart_{label}")

st.markdown(
    """
    <div class="custom-alert">
        💡 <b>Interpretation note:</b> Review the underlying articles when headline
        counts change. Sentiment predictions do not verify incidents, measure severity,
        or represent public opinion. This note is always displayed and is not an
        automatically triggered alert.
    </div>
    """,
    unsafe_allow_html=True,
)
st.divider()
st.subheader("🔍 Inspect Items Behind the Signal")
filter_col, search_col = st.columns([2, 2])
with filter_col:
    filter_choice = st.multiselect(
        "Filter by sentiment:",
        options=VALID_LABELS + ["unknown"],
        default=VALID_LABELS + ["unknown"],
    )
with search_col:
    search_query = st.text_input(
        "Search by keyword (e.g. outage, data center, Texas):", ""
    )

filtered_data = data[data["filter_label"].isin(filter_choice)]
if search_query:
    filtered_data = filtered_data[
        filtered_data["title"].str.contains(
            search_query, case=False, na=False, regex=False
        )
    ]
st.caption(f"Showing {len(filtered_data)} of {len(data)} saved articles.")
if filtered_data.empty:
    st.info("No articles match the selected filters and search text.")

st.dataframe(
    filtered_data[
        [
            "fetched_at",
            "badge_label",
            "title",
            "sentiment_score",
            "source",
            "url",
        ]
    ],
    column_config={
        "fetched_at": st.column_config.DatetimeColumn(
            "Collected at (UTC)", format="D MMM YYYY, HH:mm"
        ),
        "badge_label": st.column_config.TextColumn(
            "Sentiment Status", help="Classified by ProsusAI/finbert"
        ),
        "title": st.column_config.TextColumn("News Headline", width="large"),
        "sentiment_score": st.column_config.ProgressColumn(
            "Model Confidence",
            min_value=0.0,
            max_value=1.0,
            format="%.2f",
            help="Model output score, not a guarantee that the prediction is correct.",
        ),
        "source": st.column_config.TextColumn("Source"),
        "url": st.column_config.LinkColumn(
            "Original Article", display_text="Read News ↗"
        ),
    },
    hide_index=True,
    width="stretch",
    height=500,
)