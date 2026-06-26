"""
Module: app.py
Description: This module contains the main application logic for loading 
the model and making predictions.  
"""

import pandas as pd
from flask import Flask, jsonify, request
from loguru import logger

from config.variables import MODEL_PATH, IRIS_CLASSES
from src.inference import load_model, predict


app = Flask(__name__)

logger.info("Loading the trained model...")
MODEL = load_model(MODEL_PATH)
logger.info("Model loaded successfully.")


@app.route("/", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify that the application is running.

    Returns
    -------
    JSON response indicating the health status of the application.
    """
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def make_prediction():
    """
    Endpoint to make predictions using the trained model.

    Expects a JSON payload with input features.

    Returns
    -------
    JSON response containing the predicted classes or values.
    """
    try:
        input_data = request.get_json()
        logger.info(f"Received input data: {input_data}")

        # Convert input data to DataFrame
        X = pd.DataFrame([input_data])

        # Make predictions
        predictions = predict(MODEL, X)

        # Map predictions to class labels
        prediction = IRIS_CLASSES[predictions.iloc[0]]

        # Return predictions as JSON
        return jsonify({"predictions": prediction})

    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 400
