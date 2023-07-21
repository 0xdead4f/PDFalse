import joblib
import pandas as pd
import sys
import xgboost as xgb
import dill

file = sys.argv[1]
# Load the model from the file
model = joblib.load('model_gb.pkl')

# xgb
# model = xgb.Booster()
# model.load_model("model.txt")

df = pd.read_csv(file)
result = model.predict(df)
print(result[0])
