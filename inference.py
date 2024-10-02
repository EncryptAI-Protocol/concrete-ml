import os
import json
import numpy as np
import sys
import csv
from pathlib import Path
from src.concrete.ml.common.serialization.loaders import load

def load_model(model_path):
    with open(model_path, 'r') as f:
        return load(f)

def predict_with_model(loaded_model, X_test, model_name, serialized_value, model_id):
    try:
        y_pred_fhe_loaded, proof = loaded_model.predict(
            X_test, model_name, serialized_value, model_id, fhe="execute"
        )
        return y_pred_fhe_loaded, proof
    except Exception as e:
        raise ValueError(f"Error during prediction: {str(e)}")

def main():
    try:
        # Get the file name, ID, and X_test from command-line arguments
        json_file = sys.argv[1]  # Path to model JSON file
        model_id = sys.argv[2]  # ID
        x_test_path = sys.argv[3]  # Path to X_test file

        with open(json_file, 'r') as j:
            contents = json.loads(j.read())
        
        model_name = contents['type_name']
        serialized_value = np.array(contents['serialized_value']['_q_weights']['serialized_value'])
        X_train = np.loadtxt('concrete-ml/x_train.csv', delimiter=',')  

        # Load X_test from the file
        X_test = np.loadtxt(x_test_path, delimiter=',')  

        # Load the model
        loaded_model = load_model(json_file)
        loaded_model.compile(X_train)
        # Make predictions
        y_pred_fhe_loaded, proof = predict_with_model(
            loaded_model, X_test, model_name, serialized_value, model_id
        )

        # Output the result
        result = {
            "predictions": y_pred_fhe_loaded.tolist(),
            "proof": proof
        }
        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
