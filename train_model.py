import os
print(os.getcwd())
print(os.listdir())

from sklearn.model_selection import train_test_split
import logging
from data.clean_data import load_data
from model.model_function import train_model, compute_model_metrics, \
                                 model_predictions, process_data
from joblib import dump

logging.basicConfig(
    filename='./log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

def split_data(data):
    try:
        train, test = train_test_split(data, test_size=0.20, random_state=0)
        logging.info('SUCCESS!:Data split successfully')
        return train, test
    except BaseException:
        logging.info('Error!:Error whiles splitting data')


cat_features = [
    "workclass",
    "education",
    "marital.status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native.country",
]


def model_slicing(data):
    """
    Slice model for categorical features
    """
    slice_values = []

    for cat in cat_features:
        for cls in test[cat].unique():
            df_temp = test[test[cat] == cls]
            X_test_temp, y_test_temp, _, _ = process_data(
                df_temp, categorical_features=cat_features,
                label="income", encoder=encoder, lb=lb, training=False)
            y_preds = model.predict(X_test_temp)
            precision_temp, recall_temp, fbeta_temp = compute_model_metrics(
                y_test_temp, y_preds)
            results = "[%s->%s] Precision: %s " \
                "Recall: %s FBeta: %s" % (
                    cat,
                    cls,
                    precision_temp,
                    recall_temp,
                    fbeta_temp)
            slice_values.append(results)

    with open('slice_model_output.txt', 'w') as out:
        for slice_value in slice_values:
            out.write(slice_value + '\n')
if __name__ == "__main__":
    df = load_data('./data/census_cleaned.csv')
    train, test = split_data(df)
    test.to_csv('./data/testings.csv')
    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features,
        label="income", training=True)
    X_test, y_test, encoder_t, lb_t = process_data(
        test, categorical_features=cat_features,
        label="income", training=False, encoder=encoder, lb=lb)
    dump(encoder_t, './model/encoder.joblib')
    dump(lb_t, './model/lb.joblib')
    model = train_model(X_train, y_train)
    dump(model, './model/model.joblib')
    predictions = model_predictions(X_test, model)
    precision, recall, fbeta = compute_model_metrics(y_test, predictions)
    model_slicing(df)
    print("Model Training Complete")