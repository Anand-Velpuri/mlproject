from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation_obj = DataTransformation()
    train_arr, test_arr, _ = data_transformation_obj.initiate_data_transformation(train_data, test_data)
    model_trainer_obj = ModelTrainer()
    print(model_trainer_obj.initiate_model_trainer(train_arr, test_arr))