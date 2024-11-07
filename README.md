## About

This repo is a fork from the original [Concrete](https://github.com/zama-ai/concrete) by [Zama](https://github.com/zama-ai). The main work has been implementing validity proofs to the predictions issued by all models from concrete-ml that come from sklearn.
### What is Concrete ML

**Concrete ML** is a Privacy-Preserving Machine Learning (PPML) open-source set of tools built on top of [Concrete](https://github.com/zama-ai/concrete) by [Zama](https://github.com/zama-ai).

It simplifies the use of fully homomorphic encryption (FHE) for data scientists so that they can automatically turn machine learning models into their homomorphic equivalents, and use them without knowledge of cryptography.

Concrete ML is designed with ease of use in mind. Data scientists can use models with APIs that are close to the frameworks they already know well, while additional options to those models allow them to run inference or training on encrypted data with FHE. The Concrete ML model classes are similar to those in scikit-learn and it is also possible to convert PyTorch models to FHE.
<br></br>
## Command to run the Docker Image
```console 
docker run -v $(pwd)/logistic_regression_model.json:/app/logistic_regression_model.json -v $(pwd)/x_test.csv:/app/x_test.csv inference_image /app/logistic_regression_model.json 1234 /app/x_test.csv
```

### Main features implemented

- **Validity Proofs**: On any ready-to-use FHE-friendly models with a user interface that is equivalent to their the scikit-learn and XGBoost counterparts a kind of predicition signature has been implemented to verify that the model is the one doing the predictions.
- **Inference Script**: A docker image that is able to run inference on a selected model and returning the predictions along with a validity proof.

### Docker 
```console
docker build -t inference_image .
docker run -v $(pwd)/logistic_regression_model.json:/app/logistic_regression_model.json -v $(pwd)/x_test.csv:/app/x_test.csv inference_image /app/logistic_regression_model.json 1234 /app/x_test.csv
```

*Learn more about Concrete ML features in the [documentation](https://docs.zama.ai/concrete-ml).*
<br></br>

### Use cases

By leveraging FHE, Concrete ML can unlock a myriad of new use cases for machine learning, such as enabling secure and private data collaboration, protecting sensitive data while still allowing for analysis, and facilitating machine learning on data-sets that are subject to strict data privacy regulations, for instance

- **Healthcare data analysis**: Improve patient care while maintaining privacy by allowing secure, confidential data sharing between healthcare providers.
- **Financial services**: Facilitate secure financial data analysis for risk management and fraud detection, keeping client information encrypted and safe.
- **Ad campaign tracking**: Create targeted advertising and campaign insights in a post-cookie era, ensuring user privacy through encrypted data analysis.
- **Industries:** Enable predictive maintenance in the cloud while keeping sensitive data confidential, enhancing efficiency and data security.
- **Biometrics:** Give the ability to create user authentication applications without having to reveal their identities.
- **Government:** Enable governments to create digitized versions of their services without having to trust cloud providers.

### Demos

Some demos have been implemented and can be found in the repo. They are a set of Jupyter Notebooks that showcase how models are trained and how predictions are returned. Demo data is under #demo-data
