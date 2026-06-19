"""
Module: train.py
Description: This module contains functions for training the machine learning model,
"""

import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    """
    Train a Random Forest Classifier on the provided training data.

    Parameters
    ----------
    X_train : pd.DataFrame
        The training features.
    y_train : pd.Series
        The training target variable.

    Returns
    -------
    RandomForestClassifier
        The trained Random Forest Classifier model.
    """
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model


def save_model(model: RandomForestClassifier, model_path: str) -> None:
    """
    Save the trained model to the specified path.

    Parameters
    ----------
    model : RandomForestClassifier
        The trained model to be saved.
    model_path : str
        The file path where the model will be saved.
    """
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)


def training(X_train: pd.DataFrame, y_train: pd.Series, model_path: str) -> None:
    """
    Train the model and save it to the specified path.

    Parameters
    ----------
    X_train : pd.DataFrame
        The training features.
    y_train : pd.Series
        The training target variable.
    model_path : str
        The file path where the trained model will be saved.

    Returns
    -------
    None
    """
    model = train_model(X_train, y_train)
    save_model(model, model_path)
