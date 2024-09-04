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

def predict_with_model(loaded_model, X_test, model_name, serialized_value, id):
    try:
        y_pred_fhe_loaded, proof = loaded_model.predict(
            X_test, model_name, serialized_value, fhe="execute", id=id
        )
        return y_pred_fhe_loaded, proof
    except Exception as e:
        raise ValueError(f"Error during prediction: {str(e)}")

def main():
    try:
        # Get the file name, ID, and X_test from command-line arguments
        json_file = sys.argv[1]  # Path to model JSON file
        id = sys.argv[2]  # ID
        x_test_path = sys.argv[3]  # Path to X_test file

        with open(json_file, 'r') as j:
            contents = json.loads(j.read())
        
        with open(x_test_path, 'r') as f:
            reader = csv.reader(f)
            X_test_vals = list(reader)

        model_name = contents['type_name']
        serialized_value = np.array(contents['serialized_value']['_q_weights']['serialized_value'])

        # Load X_test from the file
        X_test = np.load(X_test_vals)  

        # Load the model
        loaded_model = load_model(json_file)

        # Make predictions
        y_pred_fhe_loaded, proof = predict_with_model(
            loaded_model, X_test, model_name, serialized_value, id
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
