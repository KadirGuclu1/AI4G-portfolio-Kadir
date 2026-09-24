# Term 1 - Week 3: Lists & Dictionaries

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

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
Anonymous CV Screening
**My pair partner:**
Ahmet Ünlü (24125822)
**Tool we had to use:**
LLM API (via Python)
**SDG we had to address:**
SDG10 (reduced inequalities)
**What problem does it solve, and for whom?**
This tool is for a recruiters or hiring team member who screens incoming CVs, whether manually or with the help of an AI tool. It addresses the risk that a candidate's name and the assumptions people or AI models make based on it unconsciously influences how a CV is judged. By automatically removing the candidate's name and other identifying details before any evaluation happens, the tool ensures that the first-stage judgment (by a human or an AI) is based only on skills, education, and experience.

**What did you build?**
1.	Provide a CV - paste it as text, or upload a .pdf, .docx, or .txt file.
2.	Anonymize - the tool detects the candidate's name using the Gemini API and replaces it with "[CANDIDATE]". Email addresses, phone numbers, and postal codes are removed locally using pattern matching, before anything is sent to the AI.
3.	Review - the anonymized CV is shown so the user can verify it before proceeding.
4.	Evaluate - the anonymized CV and a job vacancy are sent to the Gemini API, which returns a score (1–10) and a short motivation based only on qualifications, skills, and experience.

**Link to the live thing (if any):**
https://github.com/Hubertsauce/Hackathon-week3.git
https://hackathon-week3-p4l2oy8awybyod7mhfmcyr.streamlit.app/

**How do I run it?**
1.	Provide a CV
Choose one of two options:
Paste text — copy and paste the full CV text into the text box.
Upload document upload a .pdf, .docx, or .txt file. The tool automatically extracts the text and shows it in an editable box so you can check it looks correct.
2.	Provide the job vacancy
Paste the vacancy text into the second text box.
3.	Click "Anonymize and evaluate CV"
The app will:
Detect and remove the candidate's name (shown as [CANDIDATE]), along with email, phone number, and postal code.
Show you the anonymized CV so you can review it before evaluation.
Send only the anonymized CV and the vacancy to the AI for evaluation.
Display a score (1–10) and a short motivation based only on qualifications.
4.	Review the result
Always read the anonymized CV and the AI's motivation before making any hiring decision. The tool is meant to support human judgment, not replace it, if the name wasn't detected correctly, or the evaluation seems off, double-check manually.


**Who did what?**
Ahmet made:
1.	demo project(it wasn't realy fitting the SDG)
2.	Readme
3.	main product: the API integration code and tasks code
Kadir made:
4.	Research
5.	powerpoint
6.	connection with streamlit and frontend development

**Ethical reflection - what are the risks of your tool? Who could it harm?**
The AI may occasionally fail to detect or fully remove identifying information (e.g. a name embedded in an unusual format, or indirect identity signals such as a specific university, hobby, or writing style that the anonymization step does not remove).
The scoring itself is still performed by an AI model, which can be inconsistent between runs or make evaluation errors unrelated to bias.
This tool assists human decision-making; it does not replace human review of hiring decisions.
it could harm applicants with a good CV or the judgement of the recruiter.

### Checklist
- [ ] Prototype code (or export / workflow file) is in `hackathon/`
- [ ] This week's slides are in `hackathon/`
- [ ] The prototype actually runs, and I wrote down how to run it
- [ ] Ethical reflection written above

---

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
