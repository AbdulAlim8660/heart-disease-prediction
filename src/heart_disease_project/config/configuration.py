## update the configuration manager
from heart_disease_project.constants import *
from heart_disease_project.utils.common import read_yaml,create_directories
from heart_disease_project.entity.config_entity import DataIngestionConfig
from heart_disease_project.entity.config_entity import DataValidationConfig
from heart_disease_project.entity.config_entity import DataTransformationConfig
from heart_disease_project.entity.config_entity import ModelTrainingConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        create_directories([self.config.data_validation.root_dir])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            source_URL=config.source_URL,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self)-> DataValidationConfig:
        config=self.config.data_validation
        schema= self.schema.COLUMNS
        data_validation_config=DataValidationConfig(
            root_dir= config.root_dir,
            unzip_data_dir= config.unzip_data_dir,
            STATUS_FILE= config.STATUS_FILE,
            all_schema= schema
            
        )

        return data_validation_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config=self.config.data_transformation

        create_directories([config.root_dir])
        data_transformation_config= DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformation_config
    
    def get_model_trainer_config(self)-> ModelTrainingConfig:
        config=self.config.model_trainer
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])

        model_trainer_config= ModelTrainingConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            l1_ratio=params.l1_ratio,
            alpha=params.alpha,
            target_column=schema.name

        )
        return model_trainer_config