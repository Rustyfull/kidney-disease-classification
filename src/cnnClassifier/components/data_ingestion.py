import  os
import urllib.request as request
import zipfile
import gdown
from cnnClassifier import  logger
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.utils.common import read_yaml

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        '''
        Fetch data from the url
        '''
        try:
            data_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir,exist_ok=True)
            logger.info(f"Downloading data from {data_url} into file {zip_download_dir}")

            file_id = data_url.split('/')[-2]
            prefix = f'https://drive.google.com/uc?/export=download&id={file_id}'
            gdown.download(prefix,zip_download_dir)

            logger.info(f"Download data from {data_url} into file {zip_download_dir}")
        except Exception as e:
            logger.info(f"Dowload file from {self.config.source_URL} failed")
            raise e


    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)

