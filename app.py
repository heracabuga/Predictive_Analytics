from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # convert the submitted inputs into a DataFrame
        input_data = pd.DataFrame([
            {
                "Age": data["age"],
                "Income": data["income"],
                "Student": data["student"],
                "Credit_Rating": data["credit_rating"]
            }
        ])

        # generate the prediction
        raw_prediction = model.predict(input_data)[0]

        # convert prediction into Yes or No
        if str(raw_prediction).lower() in ["1", "yes", "true"]:
            prediction_result = "Yes"
        else:
            prediction_result = "No"

        # get the confidence of the predicted class
        probabilities = model.predict_proba(input_data)[0]
        classes = list(model.classes_)

        predicted_index = classes.index(raw_prediction)
        confidence = probabilities[predicted_index] * 100

        return jsonify(
            {
                
            }
        )





if __name__ == "__main__":
    app.run(debug=True)