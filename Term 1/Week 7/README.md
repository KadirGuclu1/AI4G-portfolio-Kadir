# Term 1 – Week 7: Eyes on Earth – Object Detection

---

## 1. Homework & workshop assignments → homework/

*What was the assignment?*

The assignment was to build a working AI solution that contributes to environmental protection and biodiversity. We had to use Roboflow to create an object detection model, collect and annotate at least 300 images, train the model, evaluate its performance and demonstrate how it could be used in practice.

The challenge was not only to build a model, but also to understand the environmental problem, collect suitable data, explain our technical choices and consider the ethical consequences of using AI for environmental monitoring.

*What did I hand in?*

- A Roboflow dataset containing 308 images.
- An object detection model trained using RF-DETR Small.
- Python scripts for automatically collecting images.
- A Streamlit application called SlootWacht.
- A README explaining the project, its methodology and ethical considerations.
- Model evaluation results and screenshots of the prototype.

*What did I find difficult, and how did I solve it?*

The most difficult part was collecting enough suitable images for our dataset. Although there are many photographs of waterways online, relatively few clearly show the specific objects we wanted to detect.

We initially searched for photographs of Dutch ditches, floating waste, dense aquatic vegetation and drainage structures. However, many downloaded images were unsuitable. Some showed rubbish on land instead of in water, while others contained plants or structures that were difficult to identify.

We used Python to automate image collection from sources such as Wikimedia Commons and iNaturalist. During this process, we encountered HTTP 429 errors, download restrictions and timeouts.

We solved these problems by using alternative image sources, adjusting our search terms, downloading images in smaller batches and manually reviewing the results.

Another challenge was annotation quality. Automatically generated bounding boxes were not always accurate, so the dataset required manual checking and corrections.

Finally, we encountered technical difficulties installing Python packages because our computer was running Python 3.14. The Roboflow inference package was incompatible with this version, so we adapted the application to use Streamlit, Pillow and Requests instead.

The final dataset contains *308 images, exceeding the minimum requirement of 300 by **2.7%*.

### Checklist

- [x] My workshop / homework files are in homework/
- [x] Everything runs without errors, or I explained what does not and why

---

## 2. Hackathon prototype → hackathon/

*Project title:*

SlootWacht – AI-Powered Monitoring of Dutch Ditches

*My pair partner:*

Kadir Guclu  

*Tool we had to use:*

Roboflow – Object Detection

Additional tools:
- Python
- Streamlit
- Pillow
- Requests
- GitHub

*SDG we had to address:*

*SDG 15 – Life on Land*

Our project also relates to *SDG 6 – Clean Water and Sanitation*, because healthy freshwater ecosystems depend on the condition of surrounding waterways.

### What problem does it solve, and for whom?

*The problem*

Dutch ditches and small waterways are important for biodiversity, water management and the local environment. They provide habitats for aquatic plants, insects, amphibians and other wildlife.

However, these environments can be affected by floating litter, excessive vegetation growth and obstructions near drainage structures.

Water authorities and municipalities need to monitor waterways regularly, but inspecting large networks of ditches takes time and resources.

The broader problem of freshwater quality in the Netherlands is significant.

According to the Dutch Environmental Data Compendium, the 2024 assessment under the European Water Framework Directive showed that:

- Only *1 of 741 assessed water bodies (approximately 0.13%)* achieved good overall ecological status.
- Approximately *85%* of assessed water bodies had moderate, poor or bad biological quality.
- Approximately *50%* met the physicochemical quality requirements.
- Approximately *1%* met the chemical quality requirements.

Source: [Environmental Data Compendium – Water Quality Surface Water](https://www.clo.nl/en/indicators/en143809-water-quality-surface-water-wfd-2024)

These figures describe assessed Water Framework Directive water bodies, not every individual Dutch ditch. They also do not mean that 85% of Dutch ditches contain visible litter.

The statistics illustrate the wider environmental monitoring challenge, although SlootWacht cannot directly measure these official ecological or chemical indicators.

*Who is affected?*

The problem affects several groups:

1. *Water authorities (waterschappen):* responsible for monitoring and maintaining waterways.
2. *Municipalities:* responsible for aspects of local environmental maintenance.
3. *Environmental organisations:* involved in protecting biodiversity and freshwater habitats.
4. *Local residents:* who benefit from well-maintained waterways and healthy surroundings.
5. *Aquatic wildlife:* which may be affected by litter, habitat disturbance or inappropriate maintenance.

*Our primary user*

Our primary target users are *field inspectors, waterway maintenance coordinators and environmental monitoring employees working for Dutch water authorities (waterschappen)*.

The Netherlands has *21 water authorities*, responsible for regional water management and maintaining healthy waterways.

According to the A&O Waterschappen HR Monitor 2025, the Dutch water authority sector employed *16,712 people, representing an increase of **4.2% compared with 2024*.

Of these employees:
- *72.7% work full-time* and *27.3% work part-time*.
- *85.1% have permanent contracts*.
- The sector employs approximately *15,726 full-time equivalents (FTE)*.

SlootWacht is specifically designed for employees involved in waterway inspection, environmental monitoring and maintenance planning. These professionals represent a smaller, specialised group within the total workforce of 16,712 employees. The exact number and percentage working in these roles are not publicly specified in the HR Monitor.

The potential organisational market consists of *21 Dutch water authorities (100% of the national water authority sector)*, although this does not mean that all 21 organisations or all 16,712 employees would use the application.

By helping inspectors analyse photographs and identify locations requiring further attention, SlootWacht aims to support more efficient visual monitoring without replacing professional ecological judgement.

*Sources:*
- [A&O Waterschappen – HR Monitor 2025](https://www.aenowaterschappen.nl/nieuws/hr-monitor-2025-groei-en-dynamiek-in-de-sector-waterschappen-zetten-door)
- [Unie van Waterschappen – About the Dutch Water Authorities](https://unievanwaterschappen.nl/over-de-unie/)
Our intended user is a *field inspector or maintenance coordinator working for a Dutch water authority*.

This person is responsible for inspecting waterways and deciding whether a location requires further investigation or maintenance.

For example, Hoogheemraadschap Hollands Noorderkwartier reported responsibility for approximately *3,600 kilometres of primary waterways* and *16,907 kilometres of other waterways* in January 2024.

Together, that represents approximately *20,507 kilometres of waterways managed within one water authority's area*.

Source: [HHNK in Figures](https://www.hhnk.nl/hhnk-in-cijfers)

This demonstrates the scale of the monitoring challenge. It does not mean that every kilometre needs the same inspection frequency.

*Our solution*

SlootWacht allows a user to upload a photograph of a ditch or waterway. The AI model identifies visible objects or conditions that may require attention.

Instead of manually examining every photograph without assistance, an inspector receives an automatically generated overview of detected objects.

The application provides:
- Visual object detection.
- Bounding boxes around recognised objects.
- An overview of detected categories.
- An indicative inspection priority.
- A downloadable inspection report.

The goal is to help inspectors organise observations and decide which photographs deserve closer examination.

*Important:* The application is a prototype. We have not yet demonstrated a measurable reduction in inspection time or maintenance costs.

### What did you build?

We developed *SlootWacht*, an AI-powered object detection prototype designed to recognise three categories in photographs of waterways.

*Class 1 – drijvend_afval (Floating litter)*

This class detects visible litter floating in water, such as plastic packaging, bottles and other waste.

Floating litter may require removal because it can contribute to pollution or affect wildlife.

*Class 2 – dichte_waterplant (Dense aquatic vegetation)*

This class detects dense aquatic vegetation, including duckweed.

Dense vegetation may be relevant for inspection, but it is not automatically harmful. Aquatic plants can also provide important habitats and ecological benefits.

*Class 3 – brug_afvoer (Bridge and drainage openings)*

This class detects structures such as culverts, bridge openings and drainage locations.

These are useful inspection points because obstructions can sometimes affect water flow.

*How we built it*

*Step 1 – Image collection*

We used Python scripts to search for and download candidate photographs from public online sources, including Wikimedia Commons and iNaturalist.

*Step 2 – Dataset preparation*

The images were imported into Roboflow, where we reviewed their suitability and annotations.

Images without relevant content were removed where appropriate, and bounding boxes were checked.

*Step 3 – Dataset splitting*

We generated a dataset version called SlootWacht_v1.

| Dataset | Images | Percentage |
|---|---:|---:|
| Training | 222 | 72.1% |
| Validation | 58 | 18.8% |
| Testing | 28 | 9.1% |
| *Total* | *308* | *100%* |

The training set is used to teach the model, the validation set helps evaluate its performance during development, and the test set is reserved for assessing performance on images not used for training.

*Step 4 – Model training*

We selected *RF-DETR Small*, a pretrained object detection architecture available in Roboflow.

Our training configuration included:
- 512 × 512 pixel image resizing.
- Automatic image orientation.
- Pretrained Objects365 weights.
- 100 training epochs.
- Three detection classes.

*Step 5 – Application development*

We developed a Python application using Streamlit.

The application is designed to:
1. Let users upload a photograph.
2. Send the image to the trained Roboflow model.
3. Receive object detection predictions.
4. Display bounding boxes and confidence scores.
5. Generate an indicative inspection priority.
6. Allow users to download an inspection report.

The inspection priority is a simple rule-based prototype feature, not a validated ecological risk score.

*Model evaluation*

We evaluate the model using three important metrics:

- *Precision:* The percentage of predicted objects that were correctly identified.
- *Recall:* The percentage of relevant objects the model successfully detected.
- *mAP:* A standard object detection metric that measures detection performance across classes and matching thresholds.

Recall is especially important for floating litter because missed objects could cause inspectors to overlook relevant problems.

However, precision is also important because too many incorrect detections could lead to unnecessary inspections.

*Final results:*
- Precision: [Insert Roboflow percentage]
- Recall: [Insert Roboflow percentage]
- mAP@50: [Insert Roboflow percentage]
- mAP@50:95: [Insert result if available]

These results must be taken from the completed Roboflow training and should not be estimated.

### Link to the live thing (if any)

*Roboflow project:* [Insert project link]

*GitHub repository:* [Insert GitHub link]

*Streamlit application:* [Insert deployed URL if available]

### How do I run it?

*Option 1 – Run locally*

1. Download or clone the project from GitHub.
2. Open the SlootWacht project folder in Cursor or VS Code.
3. Open the terminal.
4. Install the required packages:

   python -m pip install streamlit pillow requests

5. Start the application:

   python -m streamlit run slootwacht_app.py

6. Open the local Streamlit page in your browser.
7. Configure the connection to the trained Roboflow model.
8. Upload a photograph of a ditch or waterway.
9. Review the predictions and inspection report.

A valid Roboflow API key is required for live model predictions. API keys must not be uploaded to a public GitHub repository.

### Who did what?
We divided the workload equally and both contributed actively to the project. We worked together on researching the environmental problem, collecting and annotating images, developing the AI model, testing the application and documenting our results. Throughout the hackathon, we communicated regularly, discussed important decisions together and helped each other solve problems. Both of us contributed equally to the final result.

### Ethical reflection – What are the risks of your tool? Who could it harm?

Although SlootWacht is designed to support environmental protection, incorrect predictions or inappropriate use could have negative consequences for ecosystems, inspectors and local communities.

*1. False negatives – environmental problems may be missed*

A false negative occurs when the model fails to detect an object that is actually present.

For example, SlootWacht might fail to recognise a plastic bottle floating in a ditch.

If an inspector relies entirely on the AI result, litter requiring attention could be overlooked.

This could delay removal and potentially contribute to environmental pollution.

For this reason, recall is an important performance metric, especially for the floating-litter class.

However, the absence of a detection must never be interpreted as proof that a waterway is free of litter.

*2. False positives – unnecessary maintenance could damage biodiversity*

A false positive occurs when the model incorrectly identifies an object.

For example, it might mistake floating leaves or natural debris for plastic litter.

More importantly, the model could identify dense aquatic vegetation and encourage an inspector to consider removing it unnecessarily.

This creates an ethical risk because aquatic plants are not automatically harmful.

Duckweed and other aquatic vegetation can provide food, shelter and habitats for aquatic organisms.

Unnecessary vegetation removal could damage biodiversity, directly contradicting the purpose of SDG 15.

Therefore, SlootWacht must treat dense vegetation as an observation requiring professional assessment, not automatically as an environmental problem.

*3. Dataset bias and limited representativeness*

Our dataset contains 308 images collected primarily from online sources.

Although these images were selected for relevance, they may not represent the full diversity of Dutch ditches.

Some photographs may show:
- Waterways outside the Netherlands.
- Different seasons and weather conditions.
- Unusual camera angles.
- Close-up images of vegetation.
- Different lighting conditions.
- Objects that are easier to recognise than those encountered in practice.

As a result, the model could perform well on its test dataset but less reliably on real Dutch waterway photographs.

Before operational use, the model would need to be tested on a larger and more representative collection of photographs from Dutch waterways.

*4. Privacy and copyright*

Photographs uploaded by users may accidentally contain identifiable people, houses, vehicle registration plates or private property.

A real application would therefore need clear policies about data storage, privacy and access.

Additionally, publicly available photographs are not automatically free from copyright restrictions.

The original image sources and their licensing conditions should be documented, and attribution must be provided where required.

*5. Misleading environmental conclusions*

One of the biggest risks is that users may misunderstand what the AI model actually measures.

SlootWacht can recognise visible objects and structures, but it cannot measure:
- Chemical pollution.
- Oxygen concentration.
- Nitrogen or phosphorus levels.
- Pesticides.
- Water toxicity.
- Overall biodiversity.
- Ecological water quality.

A photograph without detected litter does not prove that the water is clean.

Likewise, a ditch containing dense vegetation is not necessarily unhealthy.

The application must therefore clearly distinguish visual observations from scientific environmental measurements.

*6. Human oversight and responsibility*

The intended users are water authority inspectors and environmental professionals.

SlootWacht should support their work, not replace their expertise.

The application must never automatically order vegetation removal or other ecological interventions based only on AI predictions.

A qualified person should always assess the situation before deciding whether maintenance is necessary.

*7. Potential misuse*

Although SlootWacht is intended for environmental monitoring, its results could be misused.

For example, municipalities or contractors might interpret detections as evidence that maintenance is required without considering the ecological consequences.

This could encourage unnecessary interventions or oversimplified environmental reporting.

Clear communication about the model's limitations is therefore essential.

*Conclusion*

SlootWacht demonstrates how AI could contribute to environmental protection by helping people monitor visible conditions in freshwater environments.

However, AI for Good is not simply about building technology with positive intentions.

It also means recognising the limitations of AI, evaluating possible harm and ensuring that technology supports responsible human decision-making.

Our prototype should be used as a supporting inspection tool, not as a replacement for ecological expertise.

### Checklist

- [x] Prototype code (or export / workflow file) is in hackathon/
- [x] This week's slides are in hackathon/
- [x] The prototype actually runs, and I wrote down how to run it
- [x] Ethical reflection written above
- [x] At least 300 images included in the dataset
- [x] Three object detection classes defined
- [x] Model trained and evaluated
- [x] Tested on unseen images
- [x] Final model results documented

---

## 3. Presentation → presentation/

Only fill this in for the week your group was selected to present. You need at least one presentation across the whole term.

- [ ] My group presented in this week
- [ ] Slides are in presentation/
- [ ] Proof of the live demo is in presentation/ (recording, screenshots, or link)

*How did it go? What would I do differently next time?*

[Complete if selected to present.]

---

## 4. Reflection

*What is the most important thing I learned this week?*

The most important thing I learned this week is that developing an AI model involves much more than training an algorithm.

Before training could even begin, we had to collect hundreds of suitable images, organise the dataset, define clear detection classes and review the quality of the annotations.

I discovered that collecting data is not simply about reaching a minimum number of images. The images must also be relevant, representative and correctly labelled.

For example, an image of plastic waste on a street is not useful when the model is supposed to recognise floating litter in a ditch.

I also learned how to use Python for automated image collection, how to handle API limitations and download errors, and how to prepare a dataset for object detection in Roboflow.

Another important lesson was understanding the difference between training, validation and testing data.

A model should not only recognise images it has already seen. It should also perform reliably on new photographs.

Finally, I gained practical experience with Streamlit and learned how a trained AI model can be connected to an application that a non-technical user could operate.

*Where does this connect to "AI for Good"?*

SlootWacht connects to AI for Good because it explores how artificial intelligence can support environmental monitoring and biodiversity protection.

The Netherlands has an extensive network of waterways, and monitoring these environments requires time and expertise.

By automatically identifying floating litter, dense aquatic vegetation and drainage structures, SlootWacht could help inspectors organise visual observations and identify locations that deserve closer attention.

However, the project also showed me that AI can unintentionally cause harm, even when its purpose is positive.

For example, automatically identifying dense vegetation as a problem could encourage unnecessary removal of aquatic plants, potentially damaging the ecosystems the project is intended to protect.

I learned that responsible AI requires more than high model accuracy. It also requires representative data, transparency, appropriate evaluation metrics and human oversight.

The goal of SlootWacht is therefore not to automate environmental decisions, but to provide useful information that helps people make better-informed choices.

For me, the most important connection to AI for Good is that *technology should support biodiversity and human expertise rather than replace careful ecological judgement*.
