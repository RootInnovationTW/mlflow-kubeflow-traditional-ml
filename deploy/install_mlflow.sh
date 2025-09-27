#!/bin/bash
echo "🚀 部署 MLflow Tracking Server 到 Kubernetes..."
kubectl create namespace mlflow
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install mlflow bitnami/mlflow --namespace mlflow
