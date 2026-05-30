from sklearn.linear_model import LinearRegression
import numpy as np

def train_model():
    # بيانات تجريبية بسيطة
    X = np.array([[30, 40], [35, 60], [40, 70], [45, 80]])
    y = np.array([80, 70, 60, 50])

    model = LinearRegression()
    model.fit(X, y)

    return model


def predict(model, temp, humidity):
    return model.predict([[temp, humidity]])[0]