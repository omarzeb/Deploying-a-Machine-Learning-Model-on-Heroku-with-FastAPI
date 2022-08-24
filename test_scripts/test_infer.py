from src.model_infer import run_inference
import numpy as np

def test_run_inference(inference_data):
    prediction = run_inference(inference_data)

    assert prediction == " <=50K"
