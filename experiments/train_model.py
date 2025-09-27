import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn

data = load_iris()
X, y = data.data, data.target

model = RandomForestClassifier(n_estimators=100, max_depth=5)

with mlflow.start_run():
    model.fit(X, y)
    acc = model.score(X, y)
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 5)
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")
