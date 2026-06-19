"""
Module: inference.py
Description: This module contains functions for loading the trained model and making predictions.
"""

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def load_model(model_path: str):
    """
    Load the trained model from the specified path.

    Parameters
    ----------
    model_path : str
        The file path where the trained model is saved.

    Returns
    -------
    The loaded model.
    """
    try:
        return joblib.load(model_path)
    except FileNotFoundError:
        print(f"Model file not found at {model_path}")
        return None
    

def predict(model: RandomForestClassifier, X: pd.DataFrame) -> pd.Series:
    """
    Make predictions using the loaded model.

    Parameters
    ----------
    model : RandomForestClassifier
        The loaded model to be used for making predictions.
    X : pd.DataFrame
        The input features for which to make predictions.

    Returns
    -------
    pd.Series
        The predicted classes or values.
    """

    return pd.Series(model.predict(X))
    