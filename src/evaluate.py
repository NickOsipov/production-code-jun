"""
Module: evaluate.py
Description: This module contains functions for evaluating the performance of the trained model.
"""

import pandas as pd
from sklearn.metrics import accuracy_score


def evaluate_model(y_true: pd.Series, y_pred: pd.Series) -> float:
    """
    Evaluate the performance of the model using accuracy score.

    Parameters
    ----------
    y_true : pd.Series
        The true labels.
    y_pred : pd.Series
        The predicted labels.

    Returns
    -------
    float
        The accuracy score of the model.
    """
    metric = accuracy_score(y_true, y_pred)
    print(f"Model Accuracy: {metric:.4f}")
    return metric
