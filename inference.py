import os
import json
import numpy as np
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
        raise ValueError(f"Error: {str(e)}")


def main():
    try:
        # Get the file name and ID from environment variables
        json_file = os.getenv('MODEL_FILE')
        id = os.getenv('PREDICTION_ID', '1234')

        with open(json_file, 'r') as j:
            contents = json.loads(j.read())

        model_name = contents['type_name']
        serialized_value = np.array(contents['serialized_value']['_q_weights']['serialized_value'])

        # Load the model
        loaded_model = load_model(json_file)

        # Assume X_test is passed, loaded, or predefined somewhere
        X_test = np.array([...])  # Replace with actual test data

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
