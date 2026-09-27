import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")


def predict_price(rm, lstat, ptratio):
    input_data = pd.DataFrame(
        [[rm, lstat, ptratio]],
        columns=["RM", "LSTAT", "PTRATIO"]
    )

    prediction = model.predict(input_data)

    return prediction[0]


# Test prediction
if __name__ == "__main__":
    result = predict_price(6.575, 4.98, 15.3)

    print(f"Predicted House Price: {result:.2f}")