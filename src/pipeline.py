"""
Script: pipeline.py
Description: This script orchestrates the entire machine learning pipeline, 
including data preprocessing, model training, model evaluation, and inference.
"""

from loguru import logger

from config.variables import MODEL_PATH

from src.evaluate import evaluate_model
from src.inference import load_model, predict
from src.preprocessing import preprocess_data
from src.train import training


def main():
    """
    The main function that orchestrates the machine learning pipeline.
    """
    
    logger.info("Starting the machine learning pipeline...")

    # Load and preprocess data
    X_train, X_test, y_train, y_test = preprocess_data()
    logger.info("Data preprocessing completed.")

    # Train the model and save it
    training(X_train, y_train, MODEL_PATH)
    logger.info("Model training completed and saved to disk.")

    # Load the trained model
    model = load_model(MODEL_PATH)
    logger.info("Model loaded from disk.")

    # Make predictions (for demonstration, using the same data)
    predictions = predict(model, X_test)
    logger.info("Inference completed.")

    # Evaluate the model
    evaluate_model(y_test, predictions)
    logger.info("Model evaluation completed.")

    logger.info("Machine learning pipeline finished successfully.")


if __name__ == "__main__":
    main()
