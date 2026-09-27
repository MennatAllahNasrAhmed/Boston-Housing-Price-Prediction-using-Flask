from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get input values from the form
        rm = float(request.form["RM"])
        lstat = float(request.form["LSTAT"])
        ptratio = float(request.form["PTRATIO"])

        # Create DataFrame with the same feature names
        input_data = pd.DataFrame(
            [[rm, lstat, ptratio]],
            columns=["RM", "LSTAT", "PTRATIO"]
        )

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Return result to the HTML page
        return render_template(
            "index.html",
            prediction=f"{prediction:.2f}"
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)