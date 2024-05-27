import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
 
data = {
    '呼叫次數': [1427, 1427, 1429, 1418, 1427, 1428, 1428, 1428, 1428, 1425, 1426, 1427, 1426],
    '數據傳輸量': [6575, 462, 3046, 422, 6449, 845, 2825, 681, 323, 645248, 24665, 1660, 106968],
    '點數': [1.487, 1.427, 1.449, 1.418, 1.487, 1.428, 1.448, 1.428, 1.428, 7.725, 1.666, 1.437, 2.466]
}
 
# Create DataFrame
df = pd.DataFrame(data)
 
X = df[['呼叫次數', '數據傳輸量']]
y = df['點數']

highest_r2 = 0
highest_score = -1
random_state_var = 0

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=650)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

 
print(highest_r2, highest_score)
 
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")
 
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)