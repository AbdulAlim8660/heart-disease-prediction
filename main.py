from heart_disease_project import logger
from heart_disease_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from heart_disease_project.pipeline.stage_02_data_validation import DataValidationPipeline
from heart_disease_project.pipeline.stage_03_data_tranformation import DataTransformationPipeline
STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info('running the data ingestion stage pipeline')
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info('the data ingestion training pipeline is completed')
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data validation Stage"

try:
    logger.info('running the data validation pipeline')
    data_validation_pipeline=DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info("the data validation pipeline was successful")
except Exception as e:
     raise e


STAGE_NAME='Data Transformation Stage'

try:
     logger.info('running the transformation pipeline')
     data_transformation_pipeline = DataTransformationPipeline()
     data_transformation_pipeline.main()
     logger.info("the data transformation pipeline was successful")
except Exception as e:
     raise e
