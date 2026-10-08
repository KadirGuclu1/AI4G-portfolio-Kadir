# Ethical Reflection: Income-Threshold Screening

This project examines whether machine learning can be used to flag subsidy applicants who may earn more than USD 50,000 per year. A flagged applicant would be referred for **manual document verification**, not automatically rejected.

The main evaluation metric is **precision**, because a false positive can place an additional burden on an eligible low-income applicant. However, model performance alone cannot determine whether such a system is ethically acceptable.

## Context

The project uses the [UCI Adult dataset](https://archive.ics.uci.edu/dataset/2/adult), which contains **48,842 records** and **14 raw features**. The data were extracted from the 1994 United States Census database and are intended to predict whether a person’s annual income exceeds USD 50,000.

Because the dataset is historical, based on the United States, and contains unequal group representation, it should not be treated as direct evidence about subsidy applicants in the Netherlands today. The USD 50,000 threshold is also historical and does not represent current Dutch eligibility rules, income standards, or living costs.

Therefore, this project demonstrates a possible machine-learning workflow. It does **not** prove that a real subsidy-screening policy would be accurate, fair, lawful, or appropriate.

## Project goal

The goal is to identify applicants whose predicted income profile suggests they may earn more than USD 50,000

| Outcome | Intended action |
|---|---|
| Flagged by the model | Manual verification of income documents |
| Not flagged | Normal application process |

A false positive is treated as the most important individual harm because an eligible applicant could face unnecessary checks, delays, stress, or loss of support.

## Dataset

- **Source:** [UCI Machine Learning Repository — Adult](https://archive.ics.uci.edu/dataset/2/adult)
- **Records:** 48,842
- **Raw features:** 14
- **Original purpose:** Predict whether annual income exceeds USD 50,000
- **Data origin:** 1994 United States Census database
- **Important limitation:** The data are outdated, geographically specific, and not representative of the current Dutch population. 

## Ethical assessment

### Harm and proportionality

A false positive is the clearest individual harm in this scenario. Someone who genuinely qualifies for support may face delay, stress, extra paperwork, suspicion, or loss of assistance because the model associates them with a higher-income profile.

These effects may affect some applicants more than others. People with limited time, limited digital skills, disabilities, language barriers, or insecure employment may have more difficulty completing additional verification requirements.

A false negative has a different cost because an ineligible applicant may receive limited public funds. This is important, but it does not justify treating every applicant as a potential fraud case. The response must remain reasonable and proportionate.

A prediction should never be treated as proof that someone is dishonest. Before using a model, the organisation should first consider simpler methods, such as requesting recent income documents or checking official records where there is a legal basis to do so.

### Fairness

The results show that a model can achieve strong overall performance while still treating groups unequally.

| Model | Test precision | Overall recall | Female recall | Male recall | Observation |
|---|---:|---:|---:|---:|---|
| Random Forest | 0.906 | 0.287 | 0.063 | 0.331 | Very large sex-based recall gap |
| Logistic Regression | — | — | 0.198 | 0.545 | Substantial sex-based recall gap |
| KNN | — | Best overall recall and F1 | 0.475 | 0.653 | Smallest tested sex-based gap, but still unequal |

KNN is the least problematic of the three tested models, but that does **not** mean it is fair. Female recall remains substantially below male recall.

The evaluation only examines broad sex and country groups. It does not establish fairness across race, age, disability, household type, migration background, or intersections such as older migrant women. Small subgroups can also make performance estimates unstable.

The binary sex field and the coarse “United States / Other” country category erase important differences between people. More detailed and context-specific evaluation would be needed before drawing conclusions about fairness.

### Sensitive attributes and proxies

Using sex and race as model inputs is especially difficult to justify in a benefits context. These attributes may be useful for auditing unequal outcomes, but using them to decide who receives extra scrutiny risks direct discrimination.

Removing sex and race from the feature set would be necessary to evaluate, but it would not solve the problem by itself. Features such as occupation, education, relationship status, and working hours can act as proxies for protected characteristics.

A responsible system would need:

- Clear rules on which features may be used
- A documented justification for every feature
- Fairness testing on the final model and decision process
- Monitoring for indirect discrimination caused by proxy variables

## Autonomy and transparency

Applicants should know when an automated system is used as part of the verification process, what information is used, and what happens after a flag is raised.

Applicants should be able to:

- Correct inaccurate personal data
- Provide relevant context
- Request meaningful human review
- Challenge the result without losing support during a slow appeal process

KNN creates an additional explanation challenge. Its prediction depends on the labels of nearby training records after preprocessing, but similarity does not necessarily mean ethical relevance.

A caseworker needs more information than a probability score. The system should show prediction uncertainty, data limitations, and the fact that the output is only a recommendation—not proof of fraud or dishonest intent.

## Legal considerations

The EU AI Act treats systems used by public authorities to evaluate eligibility for essential public benefits and services as high-risk. See the [European Commission AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/essential-services).

GDPR Article 22 also protects people from certain solely automated decisions with legal or similarly significant effects. It requires safeguards such as human intervention, the ability to express a point of view, and the ability to contest a decision. See [GDPR Article 22](https://gdpr-info.eu/art-22-gdpr/).

A nominal human reviewer is not enough if that person routinely accepts the model score without independent judgement.

## Privacy and security

The principle of data minimisation requires collecting only information necessary for a clearly defined purpose.

This project uses demographic and employment variables to infer income, even though recent evidence of income would usually be more relevant. In a real system, collecting this much personal information could be unnecessary and could expose sensitive data without making the decision more reliable.

A real deployment would require:

- A clear legal basis for processing
- A Data Protection Impact Assessment (DPIA)
- Access controls and encryption
- Limits on data-retention periods
- Audit logs
- A security-incident response plan
- Restrictions on using data for unrelated investigations

Training data, predictions, explanations, reviewer actions, and appeal outcomes should all be governed as personal data. Public reporting should use aggregated results and protect small groups against re-identification.

## Accountability

The public organisation remains responsible for decisions made with the help of the model. Responsibility should not be shifted to the model or its developer.

The organisation should define:

- Who can approve a flag
- Who investigates complaints
- Which errors trigger suspension of the system
- How affected applicants receive a remedy

The organisation should record both model recommendations and final human decisions. This makes it possible to detect automation bias and unequal reviewer behaviour.

Before any pilot, the system should be independently reviewed using current local data. Evaluation should include:

- Subgroup precision and recall
- False-positive rates
- Calibration
- Error severity
- Waiting time caused by verification
- Override rates
- Appeal outcomes

Monitoring must continue after deployment because policy, labour markets, populations, and data quality can change. There should be a clear process to stop using the model if it becomes unreliable or causes unacceptable harm.

## Final position

The best ethical choice is not simply to use the model with the highest score.

In this experiment, choosing KNN over Random Forest is more defensible because the decision considered recall, F1 score, and differences between groups rather than precision alone. However, the remaining disparities, outdated dataset, proxy variables, weak geographic relevance, and high-stakes context mean that none of the models is ready for real-world use.

The most responsible position is to treat this project as a **learning exercise**.

If the idea is explored further, the model should only support carefully designed human review after a necessity-and-proportionality assessment. Applicants must be informed about the system and must be able to request an explanation, correct incorrect information, and appeal a decision.

The organisation should also demonstrate that the system is more accurate, fair, and secure than a simpler process based on actual income evidence.

## Sources

- UCI Machine Learning Repository. (1996). *Adult*. [https://archive.ics.uci.edu/dataset/2/adult](https://archive.ics.uci.edu/dataset/2/adult)

- European Commission, AI Act Service Desk. *Essential services: eligibility for public assistance benefits and services*. [https://ai-act-service-desk.ec.europa.eu/en/essential-services](https://ai-act-service-desk.ec.europa.eu/en/essential-services)

- European Union. *General Data Protection Regulation, Article 22: Automated individual decision-making, including profiling*. [https://gdpr-info.eu/art-22-gdpr/](https://gdpr-info.eu/art-22-gdpr/)

