# train_model.py
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib

# 1. Create a dummy training dataset (Simulating UPI transactions)
np.random.seed(42)
n_samples = 2000

data = {
    'amount': np.random.uniform(10, 50000, n_samples),
    'hour_of_day': np.random.randint(0, 24, n_samples),
    'vpa_age_days': np.random.randint(0, 365, n_samples),
    'tx_count_last_10m': np.random.poisson(1, n_samples),
    'is_fraud': np.random.choice([0, 1], size=n_samples, p=[0.95, 0.05])
}

df = pd.DataFrame(data)

# Force fraud conditions on dummy data for realistic training
df.loc[(df['hour_of_day'] < 5) & (df['vpa_age_days'] < 5) & (df['amount'] > 10000), 'is_fraud'] = 1

X = df[['amount', 'hour_of_day', 'vpa_age_days', 'tx_count_last_10m']]
y = df['is_fraud']

# 2. Train Model with Class Imbalance Weighting
scale_weight = (len(y) - sum(y)) / sum(y)
model = xgb.XGBClassifier(scale_pos_weight=scale_weight, max_depth=4, n_estimators=100)
model.fit(X, y)

# 3. Save Model to file
joblib.dump(model, 'upi_fraud_model.pkl')
print("Model trained and saved as 'upi_fraud_model.pkl'")
