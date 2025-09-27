# MLflow + Kubeflow for Traditional ML

這個專案展示如何整合 MLflow 與 Kubeflow 來建構傳統機器學習的 MLOps 流程。  
支援：
- ✅ MLflow 模型訓練與版本控制
- ✅ Kubeflow Pipeline 自動化任務
- ✅ GitHub Actions 自動部署

## 🚀 快速開始

```bash
python experiments/train_model.py          # 使用 MLflow 訓練
python pipelines/kubeflow_pipeline.py      # 產生 pipeline yaml
☁️ 部署 MLflow 到 Kubernetes
bash deploy/install_mlflow.sh


