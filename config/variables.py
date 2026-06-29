"""
Module: variables.py
Description: This module contains configuration variables for the application,
including database connection details, model path, and class labels.
"""

import os

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

MODEL_PATH = os.path.join("models", "model.joblib")
IRIS_CLASSES = ["setosa", "versicolor", "virginica"]

