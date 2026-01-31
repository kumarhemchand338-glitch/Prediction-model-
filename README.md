# Student Result Prediction Model (Machine Learning)

This project is a simple **Supervised Machine Learning model** that predicts whether a student will **Pass or Fail**
based on their study-related information.

The model is built using **Logistic Regression** and implemented in **Python** with the help of **scikit-learn**.

---

## 📊 Dataset Description

The dataset is created manually inside the code and includes the following features:

- **age** → Student age
- **studying** → Number of hours spent studying
- **gender** → Male / Female (encoded using LabelEncoder)
- **marks** → Student marks
- **result** → Pass or Fail (Target variable)

---

## 🧠 Machine Learning Concepts Used

- Supervised Learning
- Logistic Regression
- Label Encoding
- Train-Test Split
- Model Accuracy Evaluation

---

## 🛠️ Libraries Used

- Python
- Pandas
- scikit-learn

---

## ⚙️ How the Model Works

1. Student data is converted into a Pandas DataFrame  
2. Categorical data (gender and result) is encoded using `LabelEncoder`  
3. Features and target variables are separated  
4. Data is split into training and testing sets  
5. Logistic Regression model is trained  
6. Model accuracy is calculated  
7. User inputs are taken to predict Pass or Fail result  

---

## ▶️ How to Run the Code

1. Install required libraries:
   ```bash
   pip install pandas scikit-learn