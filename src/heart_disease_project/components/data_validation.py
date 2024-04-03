##update the component
import os 
from heart_disease_project import logger 
from heart_disease_project.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config= config
        
    def validate_all_columns(self)-> bool:
        try: 
            validation_status:None
            data = pd.read_csv(self.config.unzip_data_dir)
            data = data.iloc[1:]
            data.columns=data.iloc[0]
            all_cols= list(data.columns)
            all_schema = self.config.all_schema.keys()
            validation_status=True
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break
                #     with open(self.config.STATUS_FILE,'w') as f:
                #         f.write(f"validation status: {validation_status}")
                # if col in all_schema:
                #     validation_status=True
            with open(self.config.STATUS_FILE,'w')as f:
                f.write(f"validation_status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e