
# MLflow + Kubeflow for Traditional ML

A production-ready MLOps project combining **MLflow** and **Kubeflow Pipelines** to manage the full lifecycle of traditional machine learning models, such as Logistic Regression, Random Forest, and Gradient Boosting. Designed for reproducibility, scalability, and CI/CD automation using GitHub Actions.

![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge\&logo=mlflow\&logoColor=white)
![Kubeflow](https://img.shields.io/badge/Kubeflow-326ce5?style=for-the-badge\&logo=kubeflow\&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge\&logo=github-actions\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

---

## 📖 Overview

This repository demonstrates how to integrate MLflow (for experiment tracking and model management) with Kubeflow Pipelines (for orchestration and automated deployment) for traditional ML projects. It uses scikit-learn models and logs them using MLflow flavors and artifacts.

---

## 🚀 Features

* 🧪 **MLflow Experiment Tracking**
* 🔄 **Kubeflow Pipeline Integration**
* 🧠 **Model Registry and Versioning**
* ☁️ **GitHub Actions CI/CD**
* 📦 **MLmodel Artifact Logging**
* 🐍 **Conda / Virtualenv Support**
* 🔧 **Custom PyFunc Wrapper (optional)**

---

## 🏗️ Project Structure

```
mlflow-kubeflow-traditional-ml/
├── .github/workflows/         # CI/CD GitHub Actions (auto-deploy)
│   └── deploy.yml
├── deploy/                    # Kubernetes manifest, model inference service
├── experiments/               # Local testing scripts for MLflow
├── pipelines/                 # Kubeflow pipeline definitions
│   └── kubeflow_pipeline.py
├── scripts/                   # Automation scripts
│   └── git_update.sh
├── src/                       # Source code for training/eval
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
├── data/                      # Sample data
├── requirements.txt
├── conda.yaml                 # MLflow environment definition
└── README.md
```

---

## ⚡ Quick Start

### 🧰 Prerequisites

* Python 3.9+
* Kubernetes cluster (local or cloud)
* Kubeflow Pipelines (v1 or v2)
* MLflow installed locally or remote server

---

### 🛠️ Installation

```bash
git clone https://github.com/RootInnovationTW/mlflow-kubeflow-traditional-ml.git
cd mlflow-kubeflow-traditional-ml
pip install -r requirements.txt
```

Or activate with conda:

```bash
conda env create -f conda.yaml
conda activate traditional-mlflow
```

---

## 🧪 Run Training Locally

```bash
python src/train.py
```

This will:

* Train a scikit-learn model
* Log it to `mlruns/`
* Create `MLmodel`, `model.pkl`, `conda.yaml`

---

## 🔁 Run Kubeflow Pipeline

Ensure you have `kfp` installed and connected:

```bash
pip install kfp
python pipelines/kubeflow_pipeline.py
```

This script:

* Compiles and submits pipeline
* Triggers training, evaluation
* Logs model to MLflow

---

## 🤖 GitHub Actions CI/CD

On every push to `main`, the GitHub Action will:

1. Check out the repo
2. Set up Python
3. Run `pip install`
4. Compile Kubeflow pipeline
5. (Future) Deploy to K8s

Update `deploy.yml` to match your cluster or secret config.

---

## 📁 MLflow Artifacts Structure

When models are logged, you'll see this structure:

```
model/
├── MLmodel
├── conda.yaml
├── python_env.yaml
├── model.pkl
└── code/
```

**MLmodel** example:

```yaml
flavors:
  python_function:
    model_path: model.pkl
    loader_module: mlflow.sklearn
    env:
      conda: conda.yaml
      virtualenv: python_env.yaml
    python_version: 3.9.13
  sklearn:
    pickled_model: model.pkl
    serialization_format: cloudpickle
```

---

## 🧠 Extend the Project

### ➕ Add Your Own Model

1. Modify `src/train.py`
2. Use `mlflow.log_model()`
3. Optionally write a `pyfunc` wrapper class

### 📤 Deploy to Kubernetes

1. Customize `deploy/` YAMLs
2. `kubectl apply -f deploy/`

---

## ✅ TODO / Next Steps

* [ ] Add KServe / Seldon Core for model serving
* [ ] Enable metadata tracking with MLflow + K8s
* [ ] Create `Dockerfile` for ML component container
* [ ] Auto-trigger pipeline from PR merge

---

## 📚 Resources

* [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
* [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/)
* [MLflow Flavor Spec](https://mlflow.org/docs/latest/models.html#model-serialization-format)
* [GitHub Actions Docs](https://docs.github.com/en/actions)

---

## 🧑‍💻 Maintained by Silvia

If you like this repo or find it useful, give it a ⭐ star!

