C:\Users\ACER\Pictures\Screenshot (16).png

# 🌾 Paddy Yield Prediction System using Machine Learning

A complete end-to-end Machine Learning Regression project for predicting **Paddy Yield (Kg)** using agricultural, environmental, weather, and fertilizer-related parameters.

The project includes:

- Data preprocessing pipeline
- Model training pipeline
- Prediction pipeline
- Flask web application
- Modern responsive UI
- Production-ready project structure

---

# 🚀 Project Demo

## Home Page
- Modern AI-powered landing page

## Prediction Form
- Agriculture input form
- Weather & environmental features
- Fertilizer details
- Wind & humidity details

## Prediction Result
- Predicts Paddy Yield in **Kilograms (Kg)**

---

# 📂 Project Structure

```bash
paddy_dataset/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│
├── src/
│   ├── components/
│   ├── pipeline/
│   │   └── prediction_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   ├── form.html
│   └── results.html
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

# 📊 Features Used

The model uses the following agricultural and environmental features:

- Hectares
- Agriblock
- Variety
- Soil Types
- Seedrate
- Fertilizer Information
- Nursery Information
- Rainfall Data
- Artificial Irrigation
- Temperature Data
- Wind Speed
- Wind Direction
- Relative Humidity
- Trash Bundles

---

# 🧠 Machine Learning Workflow

## 1. Data Ingestion
- Read dataset
- Split train/test data

## 2. Data Transformation
- Missing value handling
- Encoding categorical columns
- Feature scaling

## 3. Model Training
Regression models used:
- Linear Regression
- Random Forest Regressor
- Decision Tree Regressor
- XGBoost Regressor
- CatBoost Regressor

## 4. Model Evaluation
Metrics:
- R² Score
- MAE
- MSE
- RMSE

## 5. Model Deployment
- Flask web application
- Real-time prediction

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/paddy-yield-prediction.git
```

---

## Create Virtual Environment

```bash
conda create -p venv python=3.10 -y
```

Activate Environment:

```bash
conda activate venv/
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
python app.py
```

Application runs on:

```bash
http://127.0.0.1:5000
```

---

# 🖥️ Flask Application

The Flask app performs:

- User input collection
- Data conversion into DataFrame
- Data preprocessing
- Model prediction
- Result rendering

---

# 📌 Example Prediction

## Input

| Feature | Value |
|---|---|
| Hectares | 2.5 |
| Seedrate | 45 |
| Rainfall | 120 |
| Humidity | 78 |

## Output

```bash
Predicted Paddy Yield: 4520.76 Kg
```

---

# 🛠️ Technologies Used

## Programming Language
- Python

## Libraries
- Pandas
- NumPy
- Scikit-learn
- CatBoost
- XGBoost
- Flask
- Pickle

## Frontend
- HTML
- CSS
- Responsive UI

---

# 📈 Future Improvements

- Docker Deployment
- AWS Deployment
- CI/CD Pipeline
- MLOps Integration
- Streamlit Dashboard
- Model Monitoring

---

# 👨‍💻 Author

Developed by:

**Your Name**

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.

---

# 📧 Contact

For queries or collaboration:

- Email: your_email@gmail.com
- LinkedIn: your_linkedin_profile