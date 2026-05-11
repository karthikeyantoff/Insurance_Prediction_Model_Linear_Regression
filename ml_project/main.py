import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# -------------------------------------------------
# STEP 1 : Load dataset
# -------------------------------------------------

df = pd.read_csv("data_sets/insurance_data.csv")

print(df)

# -------------------------------------------------
# STEP 2 : Input and Output
# -------------------------------------------------

X = df[['age']]

y = df['bought_insurance']

# -------------------------------------------------
# STEP 3 : Split dataset
# -------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -------------------------------------------------
# STEP 4 : Create Linear Regression model
# -------------------------------------------------

model = LinearRegression()

# -------------------------------------------------
# STEP 5 : Train model
# -------------------------------------------------

model.fit(X_train, y_train)

print("Model Training Completed")

# -------------------------------------------------
# STEP 6 : Prediction
# -------------------------------------------------

prediction = model.predict([[35]])

print("Prediction :", prediction)

# -------------------------------------------------
# STEP 7 : Scatter Plot
# -------------------------------------------------

plt.scatter(X, y)

# -------------------------------------------------
# STEP 8 : Best Fit Line
# -------------------------------------------------

plt.plot(X, model.predict(X))

# -------------------------------------------------
# STEP 9 : Labels
# -------------------------------------------------

plt.xlabel("Age")

plt.ylabel("Bought Insurance")

plt.title("Linear Regression Best Fit Line")

# -------------------------------------------------
# STEP 10 : Show Graph
# -------------------------------------------------

plt.show()