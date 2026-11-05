# Buy Computer Prediction

A simple predictive analytics project that estimates whether a customer
will buy a computer from four categorical attributes:

- Age group
- Income level
- Student status
- Credit rating

The project is designed around a machine-learning workflow in Google Colab and a
Flask web interface for submitting predictions. The model target is
`Buys_Computer`, encoded as `0` (`No`) or `1` (`Yes`).

## To Run
In terminal, run:

python --version  
python -m venv venv  
.\venv\Scripts\activate  
python -m pip install Flask  
python -m flask --version   
python -m pip install pandas joblib scikit-learn==1.6.1  


## Repository structure

```text
.
├── app.py                       # Flask application and prediction route
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


## Limitations

- The dataset is very small, so metrics can vary substantially between splits.
- The model is intended for classroom demonstration, not for automated purchasing
  decisions or production use.
- No authentication, persistence, rate limiting, or deployment configuration is
  included.
- No dataset or trained model artifact is currently stored in this repository.
- The Flask endpoint requires completion before the browser can receive a
  successful prediction.
