import os
from sklearn.model_selection import train_test_split
from heart_disease_project import logger
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from heart_disease_project.entity.config_entity import DataTransformationConfig

import os
from sklearn.model_selection import train_test_split
from heart_disease_project import logger
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.df = None  # Initialize df attribute

    def set_the_header(self, data_path):
        self.df = pd.read_csv(data_path)
        self.df = self.df.iloc[1:]
        self.df.columns = self.df.iloc[0]
        self.df = self.df.drop(self.df.index[0])
        self.df.reset_index(drop=True, inplace=True)
        return self.df

    def split_columns(self):
        self.df[['job', 'education']] = self.df['jobedu'].str.split(',', expand=True)
        self.df[['months', 'years']] = self.df['month'].str.split(",", expand=True)
        self.df.drop(['jobedu', 'month', 'years'], axis=1, inplace=True)
        return self.df

    def map_categorical(self):
        self.df['targeted'] = self.df['targeted'].map({'yes': 1, 'no': 0})
        self.df['default'] = self.df['default'].map({'yes': 1, 'no': 0})
        self.df['loan'] = self.df['loan'].map({'yes': 1, 'no': 0})
        self.df['housing'] = self.df['housing'].map({'yes': 1, 'no': 0})
        return self.df

    def convert_duration(self):
        self.df['duration'] = self.df['duration'].str.replace('sec', '').str.replace('min', '').astype(float) / 60
        return self.df

    def drop_columns(self):
        self.df.drop(['customerid', 'poutcome'], axis=1, inplace=True)
        return self.df

    def convert_data_types(self):
        self.df['day'] = self.df['day'].astype('int64')
        self.df = self.df.dropna(subset=['age'])
        self.df['age'] = self.df['age'].astype('int64')
        self.df['salary'] = self.df['salary'].astype(float)
        self.df['balance'] = self.df['balance'].astype(float)
        self.df['pdays'] = self.df['pdays'].astype('int64')
        self.df = self.df[self.df['pdays'] < 500]
        self.df['previous'] = self.df['previous'].astype('int64')
        self.df = self.df[self.df['previous'] < 100]
        return self.df

    def create_bins(self):
        bins_pdays = [-1, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
        labels_pdays = ['never-reached', '0-50', '50-100', '100-150', '150-200', '200-250', '250-300',
                        '300-350', '350-400', '400-450', '450-500']
        self.df['pdays-bin'] = pd.cut(self.df['pdays'], bins=bins_pdays, labels=labels_pdays, right=False)
        self.df.drop('pdays', axis=1, inplace=True)

        bins_previous = [0, 10, 30, 60, 90, 120]
        labels_previous = ['never answered', '10-30', '30-60', '60-90', '90+']
        self.df['previous-bin'] = pd.cut(self.df['previous'], bins=bins_previous, labels=labels_previous, right=False)
        self.df.drop('previous', axis=1, inplace=True)

        return self.df

    def one_hot_encode(self):
        list_of_categorical = ['marital', 'contact', 'day', 'campaign', 'job', 'education', 'months', 'pdays-bin',
                                'previous-bin']
        dummy = pd.get_dummies(self.df[list_of_categorical], drop_first=True)
        dummy = dummy.astype(int)
        self.df.drop(list_of_categorical, axis=1, inplace=True)
        self.df = pd.concat([self.df, dummy], axis=1)
        return self.df

    def scale_numerical(self):
        list_of_numerical = ['age', 'salary', 'balance', 'duration']
        scaler = MinMaxScaler()
        df_scaled = pd.DataFrame(scaler.fit_transform(self.df[list_of_numerical]),
                                 columns=[f'{col}_scaled' for col in list_of_numerical])
        self.df.drop(list_of_numerical, axis=1, inplace=True)
        self.df = pd.concat([self.df, df_scaled], axis=1)
        return self.df
    
    def train_test_split(self):
        train, test = train_test_split(self.df, test_size=0.2, random_state=42)
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info('Data split into train and test')
        logger.info(f'Train shape: {train.shape}')
        logger.info(f'Test shape: {test.shape}')
        return train, test

