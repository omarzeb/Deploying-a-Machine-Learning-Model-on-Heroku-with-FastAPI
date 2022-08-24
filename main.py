import os

from fastapi import FastAPI
from src.schema import ModelInput
import pandas as pd
from src.model_infer import run_inference

if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")

app = FastAPI()

@app.get("/")
async def get_items():
    return {"message": "Welcome to the FAST API Inference!"}

@app.post("/")
async def inference(input_data: ModelInput):

    input_data = input_data.dict()

    columns=[ 
      'age',
      'workclass',
      'fnlgt',
      'education',
      'marital-status',
      'occupation',
      'relationship',
      'race',
      'sex',
      'hours-per-week',
      'native-country'
    ]

    change_keys = [
      ["marital-status","marital_status"],
      ["hours-per-week","hours_per_week"],
      ["native-country","native_country"]
    ]

    for new_key, old_key in change_keys:
        input_data[new_key] = input_data.pop(old_key)
    print("input_data")
    print(input_data)
    input_df = pd.DataFrame(data=input_data.values(), index=input_data.keys()).T
    input_df = input_df[columns]

    preds = run_inference(input_df)

    return {"prediction": preds}