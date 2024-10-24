import numpy as np
import scipy.sparse
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def train_model(X: scipy.sparse.csr_matrix, y: np.ndarray) -> LinearRegression:
    """Trains a Linear Regression model taking as input the training set and target, returns the model fitted"""
    lr = LinearRegression()
    lr.fit(X, y)
    return lr


def predict(X: scipy.sparse.csr_matrix, model: LinearRegression) -> np.ndarray:
    """Takes as input the model previously fitted in train_model and the test set, returns the predictions"""
    y_pred = model.predict(X)
    return y_pred


def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Takes as input the predictions array and the true target, returns the root mean squared error between the two"""
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    return rmse
