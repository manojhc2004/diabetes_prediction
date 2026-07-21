# 🩺 Diabetes Prediction System using Machine Learning

## 📌 Project Overview

This project predicts whether a patient is likely to have diabetes using Machine Learning. The model is trained on the Pima Indians Diabetes Dataset and compares multiple classification algorithms to identify the best-performing model.

The final deployed model is a **Random Forest Classifier** selected after extensive experimentation and hyperparameter tuning.

---

## 🎯 Objectives

- Predict diabetes based on patient health information.
- Compare multiple machine learning algorithms.
- Reduce False Negatives to improve diabetic patient detection.
- Perform hyperparameter tuning for better model performance.
- Save the best model for future predictions.

---

## 📂 Dataset

**Dataset:** Pima Indians Diabetes Dataset

### Features

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

### Target

- **0** → Non-Diabetic
- **1** → Diabetic

---

## 🛠️ Data Preprocessing

The following preprocessing techniques were applied:

- Missing value handling
- KNN Imputation
- Exploratory Data Analysis (EDA)
- Outlier Detection
- Feature Scaling (for Logistic Regression and SVM)
- Train-Test Split

---

## 📊 Exploratory Data Analysis

Performed:

 **Distribution Analysis**
- 
![Age Distribution](visualizations/data_distribution/age_histo.png)

- Boxplots
- Histograms
- Missing Value Analysis
- Outlier Analysis

---

## 🤖 Machine Learning Models Used

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

---

## 🚀 Ensemble Learning Models

### Bagging

- Bagging Classifier
- Random Forest

### Boosting

- AdaBoost
- Gradient Boosting
- XGBoost

### Voting

- Hard Voting
- Soft Voting
- Weighted Voting

---

## ⚙️ Hyperparameter Tuning

Performed using:

- GridSearchCV
- RandomizedSearchCV

---

## 📈 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve
- ROC-AUC Score

Special attention was given to **False Negatives**, as missing diabetic patients is more critical than predicting healthy patients as diabetic.

---

## 🏆 Final Selected Model

**Random Forest Classifier**

Reason for selection:

- Best overall performance
- Better Recall
- Reduced False Negatives
- Good balance between Accuracy and Precision

The trained model is saved using **Joblib**.

---

## 📁 Project Structure

```
diabetes_prediction_system/
│
├── best_model/notebooks
│   │               └──bagging.ipynb
│   └── random_forest_diabetes_model.joblib
│
├── dataset/
│   └── diabetes_cleanned_data_set.csv  
│   └── diabetes_interim_1.csv            # stage - 1
│   └── diabetes_interim_2.csv            # stage - 2
│   └── diabetes.csv                      # raw data  
│
├── predict_diabetes/
│   ├── predict_diabetes.py
│   └── config.py
│
├──visualization/
│   └── bivariate
│   └── data distribution
│   └── density by outcome
│   └── multivariate
│   └── target analysis
│    
├──EDA.ipynb  - notebook
├── data_cleaning.ipynb - notebook

│
├── data_cleaning.py
├── basic_inspection
├── biavariate analysis
├── multivariate analysis
├── target analysis
│  
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 💻 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Joblib

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/diabetes_prediction_system.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Prediction

```bash
python predict_diabetes.py
```

Enter the required patient information when prompted.

---

## 📌 Future Improvements

- Streamlit Web Application
- Flask/FastAPI REST API
- Docker Deployment
- Cloud Deployment
---

## 👨‍💻 Author

**Manoj H C**

## ⭐ If you found this project useful, consider giving it a star!
