import h2o
from h2o.estimators import H2ORandomForestEstimator

h2o.init()
h2o.remove_all()
# Kaggle: https://www.kaggle.com/mlg-ulb/creditcardfraud

fraud_data_frame = h2o.import_file(path="")

random_forest_model = H2ORandomForestEstimator(
    model_id="FraudDetectionModel",
    ntrees=10,
    max_depth=5,
    min_rows=4,
    nfolds=5
)

# categorical features
categorical_feature_columns = [
    'Class'
]

fraud_data_frame[categorical_feature_columns] = fraud_data_frame[categorical_feature_columns].asfactor()

# continuous features
continuous_feature_columns = [
    'V1',
    'V2',
    'V3',
    'V4',
    'V5',
    'V6',
    'V7',
    'V8',
    'V9',
    'V10',
    'Amount'
]

random_forest_model.train(x=continuous_feature_columns,
                          y='Class',
                          training_frame=fraud_data_frame)

h2o.download_pojo(random_forest_model, '../java/com/mymodel/h2o/', get_jar=False)
