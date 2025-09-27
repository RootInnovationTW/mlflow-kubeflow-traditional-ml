import kfp
from kfp import dsl

@dsl.pipeline(
    name='MLflow + Traditional ML Pipeline',
    description='使用 Kubeflow 執行 sklearn 訓練與 MLflow 紀錄'
)
def ml_pipeline():
    dsl.ContainerOp(
        name='Train Model',
        image='python:3.9',
        command=['sh', '-c'],
        arguments=[
            'pip install mlflow scikit-learn pandas && '
            'python -c "import sklearn; print(sklearn.__version__)"'
        ]
    )

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(ml_pipeline, 'ml_pipeline.yaml')
