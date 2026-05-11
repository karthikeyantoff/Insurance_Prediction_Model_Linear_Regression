Insurance Prediction using Linear Regression

Project Overview

This project uses:

Linear Regression

to predict whether a person may buy insurance based on their age.

The project demonstrates:

* Linear Regression Training
* Best Fit Line Visualization
* Prediction using Age
* Data Visualization with Matplotlib

---

Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

Dataset Information

Dataset File:

```text id="87uvvf"
insurance_data.csv
```

Dataset Columns:

| Column           | Description               |
| ---------------- | ------------------------- |
| age              | Person age                |
| bought_insurance | Insurance purchase status |

---

# Project Workflow

```text id="bn2vr3"
Load Dataset
    ↓
Feature Selection
    ↓
Train-Test Split
    ↓
Create Linear Regression Model
    ↓
Train Model
    ↓
Prediction
    ↓
Best Fit Line Visualization
```

---

# Machine Learning Algorithm

## Linear Regression

This project uses:

# Linear Regression

Linear Regression predicts continuous numerical values using a straight-line equation.

Main equation:

genui{"math_block_widget_always_prefetch_v2":{"content":"y = mx + b"}}

Where:

* `x` = input feature
* `y` = predicted value
* `m` = slope
* `b` = intercept

---

# Dataset Logic

Input Feature:

```text id="f7m5g8"
age
```

Output:

```text id="92oztu"
bought_insurance
```

The model learns the relationship between:

```text id="5k6bkh"
Age → Insurance Purchase
```

---

# Model Training

The model is trained using:

```python id="qhctfy"
model.fit(X_train, y_train)
```

During training, Linear Regression creates the:

# Best Fit Line

which minimizes prediction error.

---

# Prediction

Example prediction:

```python id="owwsn2"
model.predict([[35]])
```

Meaning:

```text id="jlwm2x"
Predict insurance value for age 35
```

---

# Data Visualization

The project visualizes:

* Actual dataset points using scatter plot
* Linear Regression Best Fit Line

Scatter Plot:

```python id="ywry32"
plt.scatter(X, y)
```

Best Fit Line:

```python id="pfw5w5"
plt.plot(X, model.predict(X))
```

---

# Graph Output

The graph contains:

| Graph Element | Description                     |
| ------------- | ------------------------------- |
| Blue Dots     | Actual dataset values           |
| Red Line      | Linear Regression Best Fit Line |

---

# Learning Outcomes

Through this project, you can learn:

* Machine Learning basics
* Linear Regression
* Model training
* Train-test splitting
* Prediction using ML models
* Best fit line concept
* Data visualization with Matplotlib

---

# Important Note

The dataset output contains:

```text id="qlngys"
0 or 1
```

which is generally better suited for:

# Logistic Regression

This project is created mainly for learning:

* Linear Regression workflow
* Best fit line visualization

---

# Future Improvements

* Use Logistic Regression for better classification
* Add more input features
* Build Flask web application
* Compare multiple ML algorithms
* Use real-world insurance datasets

---

# Author
TEAM:
    Nexus Forge
