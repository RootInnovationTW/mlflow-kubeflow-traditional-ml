# MLflow for Traditional Machine Learning

A comprehensive project demonstrating how to use MLflow to manage the complete machine learning lifecycle for traditional ML models, with integration to Databricks and Unity Catalog.

![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📖 Overview

This project provides a complete implementation of MLflow workflows for traditional machine learning, following best practices for experiment tracking, model management, and deployment preparation. It demonstrates a real-world hotel booking price prediction use case with full MLOps capabilities.

## 🚀 Features

- **📊 Experiment Tracking** - Comprehensive MLflow experiment management
- **🔧 Hyperparameter Tuning** - Ray Tune integration with nested MLflow runs
- **📝 Model Registry** - Unity Catalog integration for model versioning
- **🔍 Model Evaluation** - Automated model comparison and validation
- **🔄 Reproducibility** - Data versioning with Delta Lake time travel
- **🎯 PyFunc Models** - Custom model packaging for deployment
- **📈 Synthetic Data** - Data generation for model testing

## 🏗️ Project Structure

```
mlflow-traditional-ml/
├── scripts/                 # Automation scripts
│   ├── setup_environment.sh
│   ├── set_mlflow_tracking.sh
│   ├── run_training.sh
│   └── hyperparameter_tuning.sh
├── src/                    # Source code
│   ├── utils/              # Utility functions
│   │   └── common.py
│   ├── data/               # Data processing
│   │   └── data_loader.py
│   ├── models/             # Model definitions
│   │   ├── lightgbm_model.py
│   │   └── pyfunc_model_wrapper.py
│   └── config/             # Configuration
│       └── project_config.py
├── notebooks/              # Jupyter notebooks (optional)
├── data/                   # Sample datasets
├── demo_artifacts/         # Generated artifacts
├── requirements.txt        # Python dependencies
└── README.md
```

## ⚡ Quick Start

### Prerequisites

- Python 3.8+
- Databricks account (for full functionality)
- Access to Unity Catalog (for model registry)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/RootInnovationTW/mlflow-traditional-ml.git
cd mlflow-traditional-ml
```

2. **Set up environment**
```bash
bash scripts/setup_environment.sh
```

3. **Configure Databricks connection**
```bash
# Edit .env file with your Databricks credentials
cp .env.example .env
# Update with your actual Databricks profile information
```

### Basic Usage

1. **Set up MLflow tracking**
```bash
bash scripts/set_mlflow_tracking.sh
```

2. **Run model training**
```bash
bash scripts/run_training.sh
```

3. **Perform hyperparameter tuning**
```bash
bash scripts/hyperparameter_tuning.sh
```

## 🎯 Key Components

### Experiment Tracking
- Automatic logging of parameters, metrics, and artifacts
- Nested runs for hyperparameter tuning
- Experiment comparison and visualization

### Model Management
```python
# Log model with full traceability
model_info = mlflow.sklearn.log_model(
    sk_model=pipeline,
    artifact_path="lightgbm-pipeline",
    signature=infer_signature(X_test, predictions),
    input_example=X_test.iloc[0:1]
)
```

### Data Versioning
- Delta Lake integration for data lineage
- Time travel capabilities for reproducibility
- Automatic version tracking of training data

### Model Evaluation
```python
# Automated model evaluation
result = mlflow.evaluate(
    model_info.model_uri,
    eval_data,
    targets="price",
    model_type="regressor",
    evaluators=["default"]
)
```

## 🔧 Configuration

Update `src/config/project_config.yaml` to match your environment:

```yaml
catalog_name: mlflow_demo
schema_name: hotel_booking
target: price
num_features:
  - lead_time
  - adults
  - children
  - babies
cat_features:
  - hotel
  - meal
  - country
  - market_segment
parameters:
  n_estimators: 100
  max_depth: 5
  learning_rate: 0.1
```

## 📊 Model Architecture

The project implements a complete ML pipeline:

1. **Data Loading** - Time-based splits with Delta Lake versioning
2. **Feature Engineering** - Categorical encoding for LightGBM
3. **Model Training** - Scikit-learn pipeline with LightGBM
4. **Evaluation** - Comprehensive metrics logging
5. **Registry** - Unity Catalog integration
6. **Packaging** - PyFunc wrapper for custom logic

## 🚀 Advanced Features

### Hyperparameter Tuning with Ray Tune
```python
param_space = {
    "n_estimators": tune.choice([50, 100, 200, 300, 400]),
    "max_depth": tune.choice([3, 5, 10, 15]),
    "learning_rate": tune.choice([0.01, 0.03, 0.05, 0.1, 0.15])
}
```

### Custom PyFunc Models
```python
class HotelBookingModelWrapper(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input):
        predictions = self.model.predict(model_input)
        return {"Total price per night": [adjust_price(pred) for pred in predictions]}
```

### Synthetic Data Generation
```python
# Generate synthetic data for model testing
data_processor.generate_synthetic_df(n=1000, max_date=None)
```

## 📈 Results and Artifacts

The project automatically generates:
- Experiment runs with detailed metadata
- Model artifacts and dependencies
- Evaluation metrics and comparisons
- Data lineage information

## 🔍 Monitoring and Debugging

- **MLflow UI** - Visualize experiments and compare runs
- **Databricks Workspace** - Integrated model registry and monitoring
- **Custom Logging** - Extended logging for debugging and audit

## 🛠️ Development

### Adding New Models
1. Extend the base model class in `src/models/`
2. Implement training and logging methods
3. Update configuration as needed

### Custom Evaluators
```python
def custom_evaluator(model, eval_data):
    # Implement custom evaluation logic
    return metrics
```

### Environment Setup for Development
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 TODO / Roadmap

- [ ] Add more model types (XGBoost, Random Forest)
- [ ] Implement advanced feature engineering
- [ ] Add automated model monitoring
- [ ] Expand deployment examples
- [ ] Add CI/CD pipeline examples

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- MLflow team for the excellent MLOps platform
- Databricks for Unity Catalog integration
- Ray project for hyperparameter tuning capabilities

## 📞 Support

If you have any questions or run into issues, please:
1. Check the [Issues](https://github.com/your-username/mlflow-traditional-ml/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers if needed

## 📚 Additional Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [Databricks MLflow Guide](https://docs.databricks.com/mlflow/index.html)
- [Ray Tune Documentation](https://docs.ray.io/en/latest/tune/index.html)

---

**⭐ If you find this project useful, please give it a star on GitHub!**

---

*This project is maintained by Silvia and contributors.*
