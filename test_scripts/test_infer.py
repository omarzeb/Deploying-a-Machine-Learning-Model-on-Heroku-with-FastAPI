from src.model_infer import run_inference
import numpy as np

def test_run_inference_low(inference_data_low):
    prediction = run_inference(inference_data_low)

    assert prediction == " <=50K"


def test_run_inference_high(inference_data_high):

    prediction = run_inference(inference_data_high)
    print("prediction: ", prediction)
    
    assert prediction == " >50K"
