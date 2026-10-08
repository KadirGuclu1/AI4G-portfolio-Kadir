# Term 1 - Week 5: Machine Learning Basics

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

**What did I hand in?**
_List the files, or link to them. Notebook exports, screenshots, scripts._

**What did I find difficult, and how did I solve it?**

### Checklist
- [ ] My workshop / homework files are in `homework/`
- [ ] Everything runs without errors, or I explained what does not and why

---

## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

**Project title:**  
Model Showdown: Income-Threshold Screening

**My pair partner:**  
Amien el Azzouzi

**Tool we had to use:**  
Python, Jupyter Notebook and scikit-learn

**SDG we had to address:**  
SDG 8 — Decent Work and Economic Growth

**What problem does it solve, and for whom?**  
The prototype supports an eligibility reviewer working for a government subsidy programme. It estimates whether an applicant's annual income may be above the programme's USD 50,000 threshold. A positive prediction only flags the application for manual document verification; it should never automatically reject an applicant.

**What did you build?**  
We built a machine-learning prototype that compares K-Nearest Neighbours, Logistic Regression and Random Forest using the UCI Adult dataset. The notebook cleans and prepares the data, tunes the models with cross-validation, evaluates them on a separate test set and performs a basic fairness analysis. A reviewer can also enter a fictional applicant and receive a prediction from the recommended KNN model.

**Link to the live thing (if any):**  
There is no live deployment. The working Jupyter Notebook, model comparison table and presentation are included in the `hackathon/` folder.

**How do I run it?**

1. Install Python 3.10 or newer.
2. Open a terminal in the project folder.
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start Jupyter:

   ```bash
   jupyter lab
   ```

5. Open `Notebook-modellen.ipynb`.
6. Select **Restart Kernel and Run All Cells**.
7. The notebook downloads the UCI Adult dataset automatically when the data files are not already available.

An internet connection is required during the first run.

**Who did what?**  
Amien el Azzouzi and I worked together on the project. We jointly selected the use case, prepared the dataset, developed and tested the machine-learning pipeline, compared the models, discussed the ethical risks and prepared the presentation. We reviewed each other's work and made the final model recommendation together.

**Ethical reflection — what are the risks of your tool? Who could it harm?**  
This tool could harm applicants who genuinely qualify for financial support. A false positive could wrongly flag someone for additional verification, causing delays, stress and extra administrative work. The dataset comes from the 1994 United States labour market and contains historical inequalities, so it is not representative of current subsidy applicants in the Netherlands. The models also perform differently for men and women, meaning that some groups may receive unequal treatment. Sensitive characteristics such as sex and race should be used for fairness auditing rather than as reasons for increased scrutiny. The prototype must therefore not make automatic eligibility decisions. Any real implementation would require current local data, meaningful human review, clear explanations, privacy safeguards, continuous fairness monitoring and an accessible appeal process.

### Checklist

- [x] Prototype code is in `hackathon/`
- [x] This week's slides are in `hackathon/`
- [x] The prototype runs and the instructions are written above
- [x] Ethical reflection written above

## 3. Presentation -> [`presentation/`](presentation/)

*Only fill this in for the week your group was selected to present. You need at least **one** of these across the whole term.*

- [ ] My group presented in this week
- [ ] Slides are in `presentation/`
- [ ] Proof of the live demo is in `presentation/` (recording, screenshots, or link)

**How did it go? What would I do differently next time?**

---

## 4. Reflection

**What is the most important thing I learned this week?**

**Where does this connect to "AI for Good"?**
_One concrete link to ethics, sustainability or social impact._
