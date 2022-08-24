# Model Card
For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Used Random forest classifier for prediction. Default configuration were used for training.

## Intended Use
This model can be used to predict the salary class of a person based on his financials situtation.

## Training Data
Data was sourced from https://archive.ics.uci.edu/ml/datasets/census+income ; Using Sklean train test split 80% data was used for training.

## Evaluation Data
Using the same source as above; 20% of the split data was used for validation.

## Metrics
The model was evaluated using Accuracy score, F1 beta score, Precision and Recall. The model F1 score is around 82%

## Ethical Considerations
The metics were also calculated on data slices. Due to data imbalance the model may potentially discriminate people.

## Caveats and Recommendations
The data has a gender biased. The data needs to be balanced.