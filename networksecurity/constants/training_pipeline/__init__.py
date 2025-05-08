
import os
import numpy as np
"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN="Result"
PIPELINE_NAME:str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "PhishingData.csv" #file name for the raw data
TRAIN_FILE_NAME: str = "train.csv" # for the training data
TEST_FILE_NAME: str = "test.csv" # for the testing data

SCHEMA_FILE_PATH= os.path.join("data_schema", "schema.yaml")


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "Ajalae"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float= 0.2


"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = 'data_validation'
DATA_VALIDATION_VALID_DIR:str = 'validated'
DATA_VALIDATION_INVALID_DIR: str = 'invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR: str = 'drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = 'report.yaml'


"""
Data Transformation related constants start with DATA_VALIDATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME:str = 'data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DIR:str = 'transformed'
DATA_TRANSFORMATION_TRANSFORMED_OBJ_DIR:str = 'transformed_obj'
DATA_TRANSFORMATION_TRAINED_FILE_PATH:str = 'train.npr'
DATA_TRANSFORMATION_TEST_FILE_PATH:str = 'test.npr'
PREPROCESSING_OBJ_FILE_PATH:str = 'preprocessing.pkl'

## kkn imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}