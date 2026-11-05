# Buy Computer Prediction

A beginner-friendly predictive analytics project that estimates whether a customer
will buy a computer from four categorical attributes:

- Age group
- Income level
- Student status
- Credit rating

The project is designed around a machine-learning workflow in Google Colab and a
Flask web interface for submitting predictions. The model target is
`Buys_Computer`, encoded as `0` (`No`) or `1` (`Yes`).

> **Project status:** The repository currently contains the Flask page, frontend
> assets, and the Colab activity instructions. The trained model file, dataset,
> Python dependency file, and a completed Flask prediction endpoint are not yet
> checked in. Follow the setup notes below before running the web app.

## Features

- Web form for entering customer information.
- JSON request flow from the browser to the `/predict` endpoint.
- One-hot encoding for categorical predictors.
- Model-comparison workflow for:
  - k-nearest neighbors (`n_neighbors=3`)
  - Logistic Regression
  - Gaussian Naive Bayes
  - Random Forest
  - Support Vector Machine
  - Decision Tree
- Repeated stratified cross-validation.
- Evaluation using accuracy, balanced accuracy, precision, recall, F1-score,
  ROC-AUC, confusion matrices, and classification reports.
- Export of the selected complete scikit-learn pipeline with Joblib.

## How the project works

The intended machine-learning workflow is:

1. Upload `buys_computer.csv` in Google Colab.
2. Clean column names and text values.
3. Correct the known `31...10` age-value typo when present.
4. Remove the identifier column, `Record`.
5. Use `Age`, `Income`, `Student`, and `Credit_Rating` as predictors.
6. Encode `Buys_Computer` as `No = 0` and `Yes = 1`.
7. Build preprocessing and model steps with scikit-learn pipelines.
8. Compare models using a stratified train/test split and repeated stratified
   cross-validation.
9. Select a model, train its complete pipeline on all available data, and save
   it as `svm_pipeline.pkl` or another chosen `.pkl` filename.
10. Load that artifact from the Flask application to serve predictions.

The dataset is intentionally very small. Evaluation scores are educational
demonstrations and should not be treated as evidence of production-level model
performance.

## Repository structure

```text
.
├── app.py                       # Flask application and prediction route
├── documentation/
│   ├── code.txt                # Recorded setup commands and model checks
│   └── model_prompt.txt        # Complete Colab activity specification
├── static/
│   ├── css/style.css            # Web interface styling
│   └── js/script.js             # Form submission and result display
├── templates/
│   └── index.html               # Prediction form
└── README.md
```

## Requirements

- Python 3.10 or newer
- Flask
- pandas
- scikit-learn
- Joblib
- A trained model pipeline saved with Joblib
- The `buys_computer.csv` dataset for model training

The project was originally tested with Python 3.13 and Flask 3.1.3. No
`requirements.txt` is currently included, so install the dependencies manually
or create one for repeatable deployments.

## Installation

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/heracabuga/SIA102-Project1-Predictive_Analytics.git
cd SIA102-Project1-Predictive_Analytics

python -m venv .venv
```

Activate the environment:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
python -m pip install --upgrade pip
python -m pip install Flask pandas joblib scikit-learn
```

## Train and export a model

The complete, ordered Colab activity is specified in
[`documentation/model_prompt.txt`](documentation/model_prompt.txt). It is
intended to:

1. Upload `buys_computer.csv`.
2. Compare all six models.
3. Set a selected model, for example:

   ```python
   SELECTED_MODEL = "Random Forest"
   ```

4. Fit the selected pipeline on the full dataset.
5. Save the complete pipeline with Joblib.
6. Test it with a sample customer.
7. Download the `.pkl` file.

Place the downloaded model artifact in the repository's `models/` directory:

```text
models/
└── svm_pipeline.pkl
```

The filename and location must match the path configured in `app.py`. A
production project should commit only reproducible training code and obtain
large or sensitive model artifacts from a controlled artifact store.

## Run the Flask application

From the repository root, run:

```bash
python app.py
```

Then open <http://127.0.0.1:5000> in a browser.

For development, Flask debug mode can be enabled through the application
configuration. Do not use Flask's development server as a production server.

## Web interface

The page provides four required dropdowns:

| Field | Accepted values |
|---|---|
| `age` | `<=30`, `31...40`, `>40` |
| `income` | `High`, `Medium`, `Low` |
| `student` | `Yes`, `No` |
| `credit_rating` | `Fair`, `Excellent` |

When the form is submitted, `static/js/script.js` sends JSON to
`POST /predict`:

```json
{
  "age": "<=30",
  "income": "High",
  "student": "No",
  "credit_rating": "Fair"
}
```

The intended successful response is:

```json
{
  "prediction": "Yes",
  "confidence": 82.5
}
```

The frontend displays both the text prediction and confidence percentage. The
endpoint should return a JSON error object and an appropriate HTTP status for
invalid input or prediction failures.

## Current implementation notes

Before the web application can make predictions, `app.py` needs to be completed
for the selected model artifact and environment. In particular:

- Import `request`, `jsonify`, pandas, and the model-loading library.
- Load the trained pipeline when the application starts.
- Configure the actual `.pkl` path.
- Return `prediction` and `confidence` from the `/predict` route.
- Add validation for missing or invalid JSON fields.
- Close the route's exception and response handling.

The HTML and JavaScript already expect the response keys `prediction`,
`confidence`, and `error`.

## Example prediction pipeline

A saved pipeline should include all preprocessing required by the estimator,
rather than saving only the final model. Conceptually, a prediction call should
look like this:

```python
sample_input = pd.DataFrame([{
    "Age": "<=30",
    "Income": "High",
    "Student": "No",
    "Credit_Rating": "Fair",
}])

prediction = model.predict(sample_input)[0]
probability_yes = model.predict_proba(sample_input)[0][1]
```

Keeping preprocessing inside the pipeline ensures that the web application
applies the same encoding and feature ordering used during training.

## Validation and testing

After installing dependencies, verify the environment:

```bash
python -c "import flask, pandas, joblib, sklearn; print('Dependencies are ready.')"
```

Once `app.py` and the model artifact are available, manually verify:

1. The home page loads at `/`.
2. The form rejects empty selections.
3. A valid submission returns a prediction and confidence value.
4. Invalid JSON or unsupported categories return a clear error response.
5. The predict button is re-enabled after both success and failure.

## Limitations

- The dataset is very small, so metrics can vary substantially between splits.
- The model is intended for classroom demonstration, not automated purchasing
  decisions or production use.
- No authentication, persistence, rate limiting, or deployment configuration is
  included.
- No dataset or trained model artifact is currently stored in this repository.
- The Flask endpoint requires completion before the browser can receive a
  successful prediction.

## Possible improvements

- Add `requirements.txt` or `pyproject.toml`.
- Add the completed model-loading and prediction endpoint.
- Add automated tests for preprocessing and `/predict`.
- Add input validation and structured error responses.
- Add a reproducible training script and versioned model metadata.
- Add deployment instructions for a production WSGI server.

## License

No license file is currently included. Add a license before redistributing this
project or incorporating third-party datasets and code.
