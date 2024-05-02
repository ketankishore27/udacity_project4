import numpy as np
from sklearn.preprocessing import LabelBinarizer, OneHotEncoder
from sklearn.metrics import fbeta_score, precision_score, recall_score
import logging
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE


# Optional: implement hyperparameter tuning.
def train_model(X_train, y_train):
    try:
        model = RandomForestClassifier()
        smote = SMOTE(random_state=0)
        X_train, y_train = smote.fit_resample(X_train, y_train)
        model.fit(X_train, y_train)
        logging.info('SUCCESS!:Model trained and saved')
        return model
    except BaseException:
        logging.info('ERROR!:Model not trained and not saved')


def model_predictions(X_test, model):
    try:
        predictions = model.predict(X_test)
        logging.info('SUCCESS!:Model predictions generated')
        return predictions
    except BaseException:
        logging.info('ERROR!:Model predictions not generated')


def compute_model_metrics(y, preds):
    try:
        fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
        precision = precision_score(y, preds, zero_division=1)
        recall = recall_score(y, preds, zero_division=1)
        logging.info('SUCCESS: Model scoring completed')
        return precision, recall, fbeta
    except BaseException:
        logging.info('ERROR: Error occurred when scoring Models')


def inference(model, X):
    preds = model.predict(X)
    return preds


def process_data(X, categorical_features=[], label=None, training=True, encoder=None, lb=None):
    
    if label is not None:
        y = X[label]
        X = X.drop([label], axis=1)
    else:
        y = np.array([])

    X_categorical = X[categorical_features].values
    X_continuous = X.drop(*[categorical_features], axis=1)

    if training is True:
        encoder = OneHotEncoder(sparse=False, handle_unknown="ignore")
        lb = LabelBinarizer()
        X_categorical = encoder.fit_transform(X_categorical)
        y = lb.fit_transform(y.values).ravel()
    else:
        X_categorical = encoder.transform(X_categorical)
        try:
            y = lb.transform(y.values).ravel()
        except AttributeError:
            pass

    X = np.concatenate([X_continuous, X_categorical], axis=1)
    return X, y, encoder, lb