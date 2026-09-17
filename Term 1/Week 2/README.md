# Term 1 - Week 2: Loops & Functions

---

## 1. Homework & workshop assignments -> [`homework/`](homework/)

**What was the assignment?**

**What did I hand in?**
_List the files, or link to them. Notebook exports, screenshots, scripts._

**What did I find difficult, and how did I solve it?**

### Checklist
- [x] My workshop / homework files are in `homework/`
- [x] Everything runs without errors, or I explained what does not and why

---


## 2. Hackathon prototype -> [`hackathon/`](hackathon/)

> Your tool and your SDG for this hackathon are announced at the **start of Friday's class**.
> Write them down here once you know them.

**Project title:**
SleepWindDown - Evening Routine with Screen Reduction
**My pair partner:**
Ana Talg Wolf
**Tool we had to use:**
n8n
**SDG we had to address:**
SDG 3 - Good Health & Well-being
**What problem does it solve, and for whom?**
It addresses the impact heavy screen use can have on the sleep and mental well-being of students and young adults (16-30 years) in the Netherlands and Europe who use screens heavily and report sleep or stress issues. EU teens spend on average 4.5 hours on screens on a school day and 6.1 hours on a weekend day, with 46% spending more than six hours a day on screens during weekends. Among 16-30 year olds, 86.3% use digital devices within 30 minutes of going to bed and 55.9% use them directly before sleeping, while only 9.5% follow sleep hygiene advice and put devices away at least one hour before bedtime. Studies among university students show average screen time around 5.4 hours per day, with 61% reporting poor sleep quality and clear links between screen time, sleep problems, anxiety, low mood, and concentration issues, and research among college students finds about 40% experience poor sleep quality, with screen use in bed before sleep significantly associated with worse sleep. SleepWindDown is built for students in this range who recognize they use a lot of screens, have trouble winding down, and want a simple, non-judgmental nudge towards healthier evening habits.

**What did you build?**
An automated digital well-being coach that helps students reflect on how their screen time may affect their stress, mood, and sleep. Every evening at 21:30, the workflow sends a short form asking about today's screen time, mood, and stress, an AI node analyzes these answers and generates a personalized wind-down routine (less screens before bed, light stretching, short reflection), and depending on mood and stress the user receives either a standard or an extra supportive tip via email, with all responses and generated routines logged in Google Sheets.
**Link to the live thing (if any):**
See term1/week2/hackathon for the workflow export, links, and video demo.

**How do I run it?**
Import the n8n workflow (JSON) into your n8n instance. Connect your Google Sheets and Gmail credentials in n8n. Create a Google Sheet named SleepWindDown_Log with the columns datum (date), naam (name), screen_time_vandaag (screen time today, hours), mood (1-5), stress (1-5), and notitie (note, optional), then fill in the Spreadsheet ID in both Google Sheets nodes. Set the Schedule Trigger to 21:30 local time using the cron expression 30 21 * * *. Activate the workflow and test it via the Form URL.

The workflow itself has 8 nodes: a Schedule Trigger firing daily at 21:30; a Form Trigger where the user enters screen time, mood, stress, and an optional note; a Google Sheets node that appends the form answers; an AI node (LLM) that analyzes the answers and generates a wind-down routine; an If/Condition node checking whether well-being is okay (mood >= 3 and stress <= 3); a "Good tip" branch with a standard supportive routine; a "Supportive tip" branch with an extra supportive message for low mood or high stress; and a Gmail node that sends the routine and tip to the user by email.
**Who did what?**
_Be honest about the split of work between you and your partner._

**Ethical reflection - what are the risks of your tool? Who could it harm?**
This tool collects sensitive data about screen time, mood, stress, and sleep habits. A key risk is privacy: if this data is not stored securely or is kept longer than necessary, it could be misused or reveal unwanted insights into someone's well-being. Therefore, we only collect data that is directly needed for the evening routine, store it in a single Google Sheet without sharing it with third parties, and clearly communicate that this is not a medical tool; users can stop using it at any time and delete their data by removing rows in the sheet. Another risk is that the system could incorrectly label normal screen use as unhealthy, for example a student may spend many hours on a laptop for studying rather than recreational use, so the AI prompt is designed so that high screen time is not automatically judged as negative but interpreted in context: studying is fine, but the user still gets a feasible tip to wind down. AI bias could also lead to less accurate recommendations for some users depending on how they phrase their notes, which we mitigate by using supportive, non-judgmental language and avoiding hard labels like "bad" or "unhealthy." Finally, the tool could create a false sense of security if someone with serious mental-health difficulties relies on it instead of seeking professional help, which is why every output explicitly states that this is not a medical or diagnostic service and users with low mood or high stress are actively encouraged to contact a GP or other professional. We would not trust this tool for a genuine mental-health crisis, and that is exactly where automation should stop and a human professional should take over; the tool is intended as support for awareness and small habits, not as a replacement for care.

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
