import sys
import sqlite3
import os
from sqlalchemy import create_engine
import pandas as pd
import numpy as np

def load_data(messages_filepath, categories_filepath):

    """
    Function to load data from two csvs as df(panda dataframe) and merge together
    Input: messages_filepath, categories_filepath
    Output: df
    """
    messages = pd.read_csv('disaster_messages.csv')
    categories = pd.read_csv('disaster_categories.csv')
    df = messages.merge(categories, on='id')

    return df


def clean_data(df):
    """
    Function to clean df
    Input: df
    Output df(cleaned)
    """
    # split categories.columns into 36 columns
    categories = df.categories.str.split(';', expand=True)
    # extract 1st row of all columns
    row = pd.Series(categories.loc[0,:].values)
    # extract name of columns(exclude last 2 words) and store them to
    # category_names
    category_colnames = row.apply(lambda x: x[:-2])
    categories.columns = category_colnames

    for column in categories:
    # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1]

    # convert column from string to numeric
        categories[column] = categories[column].astype(int)

    # replace 2 to mode value of 1 of related column
    categories.related=categories.related.replace(2, 1)
    # drop original categories colum
    df=df.drop('categories', axis=1)
    # concat df without original categories colum with categories dataframe
    df=pd.concat([df, categories], axis=1)
    # drop drop_duplicates
    df=df.drop_duplicates()

    return df



def save_data(df, database_filename):
    """
    Function to save cleaned df to sql database
    Input: df(cleaned), database_filename(df to be stored)
    Output: None
    """
    engine = create_engine('sqlite:///DisasterResponse.db')
    df.to_sql('df', engine, index=False, if_exists='replace')

    return


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
