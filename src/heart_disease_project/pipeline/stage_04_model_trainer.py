from heart_disease_project import logger 
from heart_disease_project.config.configuration import ConfigurationManager
from pathlib import Path
from heart_disease_project.components.model_trainer import ModelTrainer

STAGE_NAME = 'Model trainer Stage'

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_training_config= config.get_model_trainer_config()
        model_training = ModelTrainer(config=model_training_config)
        model_training.train()
if __name__=='__main__':
    try:
        logger.info(f"<<<< pipeline {STAGE_NAME} started>>>>>>>>>")
        object = ModelTrainerPipeline()
        object.main()
        logger.info(f"<<<<<<<<<<pipeline {STAGE_NAME} completed successfully")
    except Exception as e:
        raise e
