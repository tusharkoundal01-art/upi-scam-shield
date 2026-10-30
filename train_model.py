import joblib
from xgboost import XGBClassifier
import numpy as np

X = np.array([
    [150.0, 14, 120, 1],
    [10000.0, 3, 2, 8],
    [500.0, 10, 45, 0],
    [25000.0, 23, 1, 15]
])
y = np.array([0, 1, 0, 1])

model = XGBClassifier()
model.fit(X, y)

joblib.dump(model, 'upi_fraud_model.pkl')
print("Success! upi_fraud_model.pkl has been created.")