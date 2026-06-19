import pandas as pd

from src.preprocessing import load_data


def test_load_data():
    df = load_data()

    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert set(df.columns) == {
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "target",
    }
