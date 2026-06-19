from config.variables import MODEL_PATH

from src.evaluate import evaluate_model
from src.inference import load_model, predict
from src.preprocessing import preprocess_data
from src.train import training


def main():
    # Load and preprocess data
    X_train, X_test, y_train, y_test  = preprocess_data()

    # Train the model and save it
    training(X_train, y_train, MODEL_PATH)

    # Load the trained model
    model = load_model(MODEL_PATH)

    # Make predictions (for demonstration, using the same data)
    predictions = predict(model, X_test)

    # Evaluate the model
    evaluate_model(y_test, predictions)


if __name__ == "__main__":
    main()
