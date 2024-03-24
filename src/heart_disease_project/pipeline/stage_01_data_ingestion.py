from heart_disease_project.config.configuration import ConfigurationManager
from heart_disease_project.components.data_ingestion import DataIngestion
from heart_disease_project import logger

STAGE_NAME = 'Data ingestion stage'


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    
if __name__=='__main__':
    try:
        logger.info(f"the pipeline {STAGE_NAME} is running")
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'the pipeline {STAGE_NAME} is completed')
    except Exception as e:
        logger.exception(e)
