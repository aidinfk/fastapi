import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


df = pd.read_csv("breast-cancer.csv")
features = df[["radius_mean", "texture_mean"]]
target = df["diagnosis"]


xtrain, xtest, ytrain, ytest = train_test_split(features.values, target, test_size=0.33)

log_reg = LogisticRegression()
log_reg.fit(xtrain, ytrain)

joblib.dump(log_reg, "cancer_model.joblib")