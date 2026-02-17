from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import  ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline

STAGE_01_NAME = "Data Ingestion stage"
STAGE_02_NAME = "Prepare base model"
STAGE_03_NAME = "Training"
STAGE_04_NAME = "Model Evaluation"

try:
    logger.info(f">>>>>> stage {STAGE_01_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_01_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



try:
    logger.info(f">>>>>> stage {STAGE_02_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_02_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f">>>>>> stage {STAGE_03_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_03_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


try:
    logger.info(f">>>>>> stage {STAGE_04_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_04_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e