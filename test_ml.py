import os
import pytest
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# User file imports
from ml.data import process_data
from ml.model import train_model



# Import file and split the dataset for testing
project_path = os.getcwd()
data_path = os.path.join(project_path, "data", "census.csv")
print(data_path)
data = pd.read_csv(data_path)
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Setting up up repeated variables
cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
    ]
label = "salary"

# Processing data for model
X, y, encoder, lb = process_data(
        X=test,
        categorical_features=cat_features,
        label=label,
        training=True
    )

# Training the model
model = train_model(X, y)

# TODO: implement the first test. Change the function name and input as needed
def test_process_data_shapes():
    """
    Test that the process_data function correctly processes and returns the expected shapes. This is
    based on the previously verified shape.
    """
    assert X.shape == (6513, 105)
    assert y.shape == (6513,)
    assert isinstance(encoder, OneHotEncoder)
    assert isinstance(lb, LabelBinarizer)

# TODO: implement the second test. Change the function name and input as needed
def test_ModelAndEncoder():
    """
    Test that the model is trained with RandomForestClassifier and uses OneHotEncoder.
    """
    assert isinstance(model, RandomForestClassifier), "Model is not a RandomForestClassifier"
    assert isinstance(encoder, OneHotEncoder), "Encoder is not OneHotEncoder"


# TODO: implement the third test. Change the function name and input as needed
def test_process_data_encoding():
    
    # Check the encoding of categorical features
    encoded_features = encoder.transform(test[cat_features]).toarray()
    assert encoded_features.shape[1] == 99  # Number of unique values in categorical features
    assert np.all(np.isfinite(encoded_features))  # Ensure there are no NaNs
    
    # Check the encoding of labels
    encoded_labels = lb.transform(test[label])
    assert np.all(np.isin(encoded_labels, [0, 1]))  # Binary encoding
