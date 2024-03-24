from heart_disease_project.config.configuration import ConfigurationManager
from heart_disease_project import logger
from heart_disease_project.components.data_validation import DataValidation

STAGE_NAME='data validation stage'

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config= config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__=="__main__":
    try:   
        logger.info(f"<<<<<<<<<<running the {STAGE_NAME} pipeline>>>>>>>>>>>")
        object = DataValidationPipeline()
        object.main()
        logger.info(f"<<<<<<<<<<<<<<<<<finished running {STAGE_NAME} pipeline >>>>>>>>>>>>")

    except Exception as e:
        logger.exception(e)
        raise e