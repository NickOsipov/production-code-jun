"""
Module: preprocessing.py
Description: This module contains functions for data preprocessing,
including loading, splitting, saving, and preprocessing
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def load_data() -> pd.DataFrame:
    """
    Load the Iris dataset and return it as a DataFrame.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the Iris dataset with renamed columns.
    """
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Create a DataFrame from the loaded data
    df = pd.DataFrame(X, columns=iris.feature_names)
    df["target"] = y

    # Rename columns for better readability
    df = df.rename(
        columns={
            "sepal length (cm)": "sepal_length",
            "sepal width (cm)": "sepal_width",
            "petal length (cm)": "petal_length",
            "petal width (cm)": "petal_width",
        }
    )

    return df


def split_data(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42
) -> tuple:
    """
    Split the DataFrame into training and testing sets.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame to be split.
    test_size : float, optional
        The proportion of the dataset to include in the test split (default is 0.2).
    random_state : int, optional
        Controls the randomness of the split (default is 42).

    Returns
    -------
    tuple
        A tuple containing the training and testing DataFrames.
    """
    X = df.drop("target", axis=1)
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test


def save_data(df: pd.DataFrame, filename: str) -> None:
    """
    Save the DataFrame to a Parquet file.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to be saved.
    filename : str
        The name of the file to save the DataFrame to.
    """
    df.to_parquet(filename, index=False)


def preprocess_data() -> tuple:
    """
    Load, split, and save the Iris dataset.

    This function orchestrates the data preprocessing steps by loading the
    dataset, splitting it into training and testing sets, and saving the
    resulting DataFrames to Parquet files.
    """
    # Load the data
    df = load_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(df)

    return X_train, X_test, y_train, y_test
