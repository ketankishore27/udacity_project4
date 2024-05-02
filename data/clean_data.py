import logging
import pandas as pd


def load_data(path):
    try:
        df = pd.read_csv(path)
        logging.info('SUCCESS: Data succesfully imported')
        return df
    except BaseException:
        logging.info('ERROR: Data not imported')


def cleaned_data(df, destination):
    try:
        df.columns = df.columns.str.strip()
        df['income'] = df['income'].str.lstrip()
        df.drop("fnlwgt", axis="columns", inplace=True)
        df.drop("education.num", axis="columns", inplace=True)
        df.drop("capital.gain", axis="columns", inplace=True)
        df.drop("capital.loss", axis="columns", inplace=True)
        df.to_csv(destination)
        logging.info('SUCCESS:Data cleaned!')
        return df
    except Exception as e:
        logging.info('ERROR Data could not be cleaned')
        print(e)


if __name__ == '__main__':
    df = load_data("./data/census.csv")
    cleaned_data(df, "./data/census_cleaned.csv")