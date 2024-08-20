# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was created by Lucas Boyd. The model is trained on the RandomForestClassifier method from
sklearn/ensemble.  

## Intended Use
The intended use of this data is to be able to predict whether or not someone makes over $50k a year based on census data.

## Training Data
The training data is split from the base data and comprises 80% of the data. For consistency, a seed value of 42 is used to be able to reproduce the results.

## Evaluation Data
The evaluation, or test, data consists of the remaining 20% of the data. 

## Metrics
The model was trained on an F1 score of 0.6827 with a precision of 0.7431

## Ethical Considerations
There may be valid ethical concerns on how this predictive data may be used. It may be used amorally to merely collect data for analysis purpose, but that data can then be used potentially to target people of different income brackets. Some examples of targeted use would be to target them for selling stuff, or target them to reject them from services.

## Caveats and Recommendations
While this dataset does have quite a few features, 14 to be exact, and may be relatively accurate, there are always variables that will not be accounted for. For example, a worthwile feature may be a boolean value that tracks whether or not a person has ever opened a business. While it is beyond the scope of the project to collect the data, the lack of data will have an effect on the subsequent model, and so we cannot rely on the model with 100% confidence. 