from heart_disease_project import logger
from heart_disease_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info('running the data ingestion stage pipeline')
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info('the data ingestion training pipeline is completed')
except Exception as e:
    logger.exception(e)
    raise e