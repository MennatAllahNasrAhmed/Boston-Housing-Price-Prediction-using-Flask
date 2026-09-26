# Boston Housing Price Prediction using Flask

## 📌 Project Overview

This project is a **Machine Learning Web Application** for predicting house prices using the **Boston Housing Dataset**.

The project combines **Data Analysis, Machine Learning, and Flask** to create a simple web application where the user can enter the required housing-related features and receive a predicted house price.

The main idea of the project is:

```text
Housing Data
     ↓
Data Preprocessing
     ↓
Exploratory Data Analysis (EDA)
     ↓
Machine Learning Model
     ↓
Save Trained Model
     ↓
Flask Web Application
     ↓
User Input
     ↓
Predicted House Price
```

---

## 🎯 Project Objectives

* Understand and explore the Boston Housing dataset.
* Clean and preprocess the data.
* Perform Exploratory Data Analysis (EDA).
* Visualize important relationships and patterns in the data.
* Train and evaluate Machine Learning models.
* Select an appropriate model for house price prediction.
* Save the trained model for later use.
* Build a web application using Flask.
* Connect the Machine Learning model to the Flask application.
* Allow users to enter housing features and get a predicted price.

---

## 📊 Dataset

The project uses the **Boston Housing Dataset**.

The dataset contains information about housing-related characteristics and a target value representing the house price.

Each row represents an observation, while the columns represent different features used by the Machine Learning model.

The dataset is stored in:

```text
housing.csv
```

> The exact features and target column are defined according to the provided dataset.

---

## 🔍 Exploratory Data Analysis

Before building the Machine Learning model, the dataset is explored to understand its structure and relationships.

The EDA includes:

* Dataset structure
* Data types
* Missing values
* Duplicate values
* Statistical summary
* Feature distributions
* Correlation analysis
* Relationships between features and the target
* Data visualizations
* Important insights from the dataset

EDA files:

```text
eda.ipynb
visuals.py
```

---

## 🧹 Data Preprocessing

The preprocessing stage prepares the raw dataset for Machine Learning.

The preprocessing may include:

* Handling missing values
* Handling duplicate records
* Checking data types
* Separating features and target
* Feature scaling when required
* Preparing the final dataset for model training

Main file:

```text
data_preprocessing.py
```

Processed data:

```text
processed_data.csv
```

---

## 🤖 Machine Learning

After preprocessing, Machine Learning models are trained using the prepared data.

The general workflow is:

```text
Features + Target
       ↓
Train/Test Split
       ↓
Model Training
       ↓
Prediction
       ↓
Model Evaluation
       ↓
Model Selection
```

The selected trained model is saved and later loaded by the Flask application.

Main files:

```text
model.py
train_model.py
model.pkl
```

If feature scaling is used, the scaler is also saved:

```text
scaler.pkl
```

---

## 🌐 Flask Web Application

Flask is used to convert the Machine Learning model into a web application.

The application allows the user to:

1. Open the web application.
2. Enter the required housing features.
3. Submit the form.
4. Send the inputs to the Flask backend.
5. Preprocess the inputs.
6. Pass them to the trained Machine Learning model.
7. Generate the prediction.
8. Display the predicted house price.

### Application Flow

```text
User
 ↓
Web Form
 ↓
Flask
 ↓
Input Processing
 ↓
ML Model
 ↓
Prediction
 ↓
Result
```

---

## 📁 Project Structure

```text
Boston-Housing-Flask/
│
├── app.py
├── requirements.txt
├── README.md
│
├── housing.csv
│
├── data_preprocessing.py
├── processed_data.csv
│
├── eda.ipynb
├── visuals.py
│
├── model.py
├── train_model.py
├── model.pkl
├── scaler.pkl
│
├── routes.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Joblib

### Web Development

* Flask
* HTML
* CSS

### Development Environment

* Jupyter Notebook
* Visual Studio Code
* Git & GitHub

---

## 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move to the project directory:

```bash
cd Boston-Housing-Flask
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

After installing the required packages, run:

```bash
python app.py
```

The Flask application will start locally.

Open the URL displayed in the terminal, usually:

```text
http://127.0.0.1:5000/
```

---

## 📈 Model Prediction

The trained Machine Learning model is loaded by the Flask application using the saved model file:

```text
model.pkl
```

The application receives the user's input, applies the same preprocessing used during training, and sends the processed values to the model.

The final prediction is then displayed on the web page.

---

## 👥 Team Contributions

The project is divided into six main responsibilities:

### Member 1 — Team Leader

* Project integration
* Flask application
* Project management
* Testing
* Documentation

### Member 2 — Data Preprocessing

* Data cleaning
* Missing values
* Duplicate checking
* Feature/target preparation
* Processed dataset

### Member 3 — EDA & Visualization

* Exploratory Data Analysis
* Data visualization
* Correlation analysis
* Dataset insights

### Member 4 — Machine Learning

* Model training
* Model evaluation
* Model selection
* Saving the trained model

### Member 5 — Flask Backend

* Flask routes
* Receiving user inputs
* Connecting backend with the ML model
* Prediction logic

### Member 6 — Frontend

* HTML interface
* CSS styling
* Input form
* Displaying prediction results

---

## 🔄 Complete Project Workflow

```text
                 ┌─────────────────┐
                 │   housing.csv   │
                 └────────┬────────┘
                          ↓
                ┌───────────────────┐
                │ Data Preprocessing│
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │       EDA         │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │ Machine Learning  │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │    model.pkl      │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │ Flask Application  │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │   User Interface  │
                └─────────┬─────────┘
                          ↓
                ┌───────────────────┐
                │ Predicted Price   │
                └───────────────────┘
```

---

## 📌 Future Improvements

Possible future improvements include:

* Improving the web interface.
* Adding more visualizations.
* Comparing additional Machine Learning models.
* Improving prediction performance.
* Adding input validation.
* Deploying the Flask application online.

---

## 👩‍💻 Project Team

**Boston Housing Price Prediction — Machine Learning & Flask Project**

Built as a team project combining:

**Data Analysis + Machine Learning + Flask Web Development**
