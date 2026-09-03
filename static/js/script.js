const predictionForm = document.getElementById("prediction-form");
const resultContainer = document.getElementById("result-container");
const resultMessage = document.getElementById("result-message");
const predictButton = predictionForm.querySelector("button");


predictionForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const inputData = {
        age: document.getElementById("age").value,
        income: document.getElementById("income").value,
        student: document.getElementById("student").value,
        credit_rating: document.getElementById("credit_rating").value
    };

    resultContainer.classList.add("active");
    resultMessage.textContent = "Generating prediction...";

    predictButton.disabled = true;
    predictButton.textContent = "Predicting...";

    try {
        const response = await fetch("/predict", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(inputData)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error);
        }

        resultMessage.textContent =
            `Prediction: ${data.prediction} | ` +
            `Confidence: ${data.confidence}%`;

    } catch (error) {
        resultMessage.textContent =
            "An error occurred while generating the prediction.";

        console.error(error);

    } finally {
        predictButton.disabled = false;
        predictButton.textContent = "Predict";
    }
});