from h2o import h2o

h2o.init()
h2o.remove_all()

fraud_data_frame = h2o.import_file(path="/Users/yalcin.yenigun/Documents/GDG/creditcard.csv")

random_forest_model = h2o.H2ORandomForestEstimator(
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

h2o.download_pojo(random_forest_model, '../java/com/iyzipay/h2o/', get_jar=False)
