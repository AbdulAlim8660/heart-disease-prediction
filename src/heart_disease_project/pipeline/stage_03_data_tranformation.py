from heart_disease_project.config.configuration import ConfigurationManager
from heart_disease_project import logger
from heart_disease_project.components.data_transformation import DataTransformation
from pathlib import Path

STAGE_NAME = 'Data Transformation Stage'

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'),'r') as f:
                status = f.read().split(" ")[-1]

            if status=='True':
                config = ConfigurationManager()
                data_transformation_config= config.get_data_transformation_config()
                data_transformation= DataTransformation(config=data_transformation_config)
                data_transformation.set_the_header(data_transformation_config.data_path)
                data_transformation.split_columns()
                data_transformation.map_categorical()
                data_transformation.convert_duration()
                data_transformation.drop_columns()
                data_transformation.convert_data_types()
                data_transformation.create_bins()
                data_transformation.one_hot_encode()
                data_transformation.scale_numerical()
                data_transformation.drop_na()
                data_transformation.train_test_split()
            else:
                raise Exception('Your data schema is not valid')
        except Exception as e:
            raise e
    
if __name__=='__main__':
    try:
        logger.info(f"<<<<<<<<<<<<<<<Pipeline {STAGE_NAME} running >>>>>>>>>>>>>>")
        object= DataTransformationPipeline()
        object.main()
        logger.info(f"<<<<<<<<<<<<<<<<<pipeline {STAGE_NAME} completed>>>>>>>>>>>")
    except Exception as e:
        raise e
        