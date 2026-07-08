"""
Module: variables.py
Description: This module contains configuration variables for the application,
including database connection details, model path, and class labels.
"""

import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

MODEL_PATH = os.path.join("models", "model.joblib")
IRIS_CLASSES = ["setosa", "versicolor", "virginica"]

REGISTRY_USER = "nickosipov"
IMAGE_NAME = "flask-app"
CONTAINER_NAME = "flask-app"

REMOTE_HOST = os.getenv("REMOTE_HOST")
REMOTE_PATH = os.getenv("REMOTE_PATH")

SSH_KEY_PATH = os.getenv("SSH_KEY_PATH")
SSH_USER = os.getenv("SSH_USER", "ubuntu")  # Default to 'ubuntu' if not set
