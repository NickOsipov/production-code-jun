CREATE DATABASE IF NOT EXISTS mlops;

CREATE TABLE IF NOT EXISTS mlops.prediction_store (
    id             UInt64,
    sepal_length   Float32,
    sepal_width    Float32,
    petal_length   Float32,
    petal_width    Float32,
    predicted_class String,
    update_time    DateTime DEFAULT now(),
    create_time    DateTime DEFAULT now()
) ENGINE = MergeTree()
ORDER BY (id, create_time);
