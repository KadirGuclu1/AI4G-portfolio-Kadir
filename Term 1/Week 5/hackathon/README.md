## Research question

Which of KNN, Logistic Regression, and Random Forest performs best when identifying people with an income above $50,000 while also considering fairness?

## Method

1. Combine the original UCI train and test files, normalise the labels, and remove 52 exact duplicate rows.
2. Drop `fnlwgt` because it is a census sampling weight. `education` is also dropped because `education_num` contains the same information.
3. Combine `native_country` into `United-States` and `Other` because some of the original categories have very few records.
4. Use a stratified 80/20 train-test split with `random_state=42`.
5. Build a preprocessing pipeline that imputes numeric values with the median, labels missing categorical values as `Missing`, standardises numeric features, and one-hot encodes categories.
6. Tune the models using five-fold stratified cross-validation, with precision for the positive class as the main metric.
7. Test each tuned model on the test set that was kept separate during training.
8. Inspect errors and compare precision, recall, and false-positive rate by sex and country group.

## Results

Random Forest had the highest precision, but it only detected 28.7% of the actual high-income cases. KNN had a lower precision, but it had the highest recall and F1 score. Based on these results, KNN was the most suitable model for our experiment.

The subgroup analysis also showed that KNN had the smallest difference in recall between women and men. Its recall was 0.475 for women and 0.653 for men. There is still a noticeable difference, but it was smaller than the differences for Logistic Regression and Random Forest.

## Recommendation

KNN is recommended **for this classroom experiment only** because it gave the best overall results:

- Test precision: 0.728
- Test recall: 0.624
- Test F1: 0.672
- Smaller sex-based recall gap than the alternatives

This recommendation is only for our classroom experiment. The model should not be used directly in a real public-benefits system. In a real situation, income should be checked using reliable information instead of only using demographic and employment data. A person should always review the model's result, and applicants should be able to understand and challenge the result.

## Ethical use

The dataset contains sensitive attributes and reflects social patterns from the past. `sex` and `race` should not be used as reasons to delay someone's access to support. Using these attributes in a model could lead to discrimination. However, removing them does not automatically remove bias because other variables can still be related to them.

For any realistic follow-up:

- Use recent and relevant data that fits the purpose of the system.
- Keep protected attributes available for fairness checks, but be careful when using them as model inputs.
- Check how well the model performs for different groups.
- Set minimum requirements for model performance before using it in practice.
- Make sure a person reviews the model's result instead of blindly accepting the prediction.
- Tell applicants when the model is used and give them a way to correct mistakes or appeal the result.
- Protect the data with access controls, limited storage time, logging, and regular monitoring.



See [Ethical reflection](https://github.com/KadirGuclu1/AI4G-portfolio-Kadir/blob/main/Term%201/Week%205/hackathon/ETHICAL_REFLECTION.md) for the full discussion.

