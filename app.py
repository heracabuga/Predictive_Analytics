from flask import Flask, jsonify, render_template, request
from pathlib import Path

import joblib
import pandas as pd

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "svm_pipeline.pkl"
if not MODEL_PATH.exists():
    MODEL_PATH = BASE_DIR / "models" / "buys_computer_model.pkl"

print(f"Loading trained model from {MODEL_PATH.name}... (this may take ~10-15s on startup)")
model = joblib.load(MODEL_PATH)
print("Model loaded successfully! Starting Flask server...")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Convert the submitted inputs into a DataFrame
        input_data = pd.DataFrame({
            "Age": [data["age"]],
            "Income": [data["income"]],
            "Student": [data["student"]],
            "Credit_Rating": [data["credit_rating"]]
        })

        # Generate the prediction
        raw_prediction = model.predict(input_data)[0]

        # Convert the prediction into Yes or No
        if str(raw_prediction).lower() in ["1", "yes", "true"]:
            prediction_result = "Yes"
        else:
            prediction_result = "No"

        # Get the confidence of the predicted class
        probabilities = model.predict_proba(input_data)[0]
        classes = list(model.classes_)

        predicted_index = classes.index(raw_prediction)
        confidence = probabilities[predicted_index] * 100

        return jsonify({
            "prediction": prediction_result,
            "confidence": round(float(confidence), 2)
        })

    except Exception as error:
        print("Prediction error:", error)

        return jsonify({
            "error": "Unable to generate a prediction."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)