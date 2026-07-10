"""
Module: variables.py
Description: This module contains configuration variables for the application,
including database connection details, model path, and class labels.
"""

import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# MySQL
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASS = os.getenv("MYSQL_PASS")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_DBNAME = os.getenv("MYSQL_DBNAME")

# ClickHouse
CH_USER = os.getenv("CH_USER")
CH_PASS = os.getenv("CH_PASS")
CH_HOST = os.getenv("CH_HOST")
CH_PORT = os.getenv("CH_PORT")
CH_DBNAME = os.getenv("CH_DBNAME")

MODEL_PATH = os.path.join("models", "model.joblib")
IRIS_CLASSES = ["setosa", "versicolor", "virginica"]

REGISTRY_USER = "nickosipov"
IMAGE_NAME = "flask-app"
CONTAINER_NAME = "flask-app"

REMOTE_HOST = os.getenv("REMOTE_HOST")
REMOTE_PATH = os.getenv("REMOTE_PATH")

SSH_KEY_PATH = os.getenv("SSH_KEY_PATH")
SSH_USER = os.getenv("SSH_USER", "ubuntu")  # Default to 'ubuntu' if not set
