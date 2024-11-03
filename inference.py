import os
import json
import numpy as np
import sys
import csv
from pathlib import Path
import hashlib
from src.concrete.ml.common.serialization.loaders import load

def load_model(model_path):
    with open(model_path, 'r') as f:
        return load(f)

def predict_with_model(loaded_model, X_test, model_name, serialized_value):
    try:
        y_pred_fhe_loaded, proof = loaded_model.predict(
            X_test, model_name, serialized_value, fhe="execute"
        )
        return y_pred_fhe_loaded, proof
    except Exception as e:
        raise ValueError(f"Error during prediction: {str(e)}")

def validate(proof, hashed_value):
    return proof == hashed_value

def main():
    try:
        # Get the file name, ID, and X_test from command-line arguments
        json_file = sys.argv[1]  # Path to model JSON file
        x_train_path = sys.argv[2] #Path to X_test file
        x_test_path = sys.argv[3]  # Path to X_test file

        with open(json_file, 'r') as j:
            contents = json.loads(j.read())
        
        model_name = contents['type_name']
        serialized_value = np.array(contents['serialized_value']['_q_weights']['serialized_value'])
        X_train = np.loadtxt(x_train_path, delimiter=',')

        # Load X_test from the file
        X_test = np.loadtxt(x_test_path, delimiter=',')  

        value_str = str(X_test.reshape(1,-1)) + str(model_name)
        value_hash = hashlib.sha256()
        value_hash.update(value_str.encode('utf-8'))
        value = value_hash.hexdigest()

        # Load the model
        loaded_model = load_model(json_file)
        loaded_model.compile(X_train)
        # Make predictions
        y_pred_fhe_loaded, proof = predict_with_model(
            loaded_model, X_test, model_name, serialized_value )

        if validate(proof, value):
            # Output the result
            result = {
                "predictions": y_pred_fhe_loaded.tolist(),
                "proof": proof
            }
            print(json.dumps(result))
        else: 
            print("Predictions might be corrupted, the model predicting is not the selected one.")
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
