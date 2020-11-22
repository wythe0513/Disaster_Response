# Disaster Response Web Application
Udacity Data Scientist Nanodegree Project

## Table of Contents
1. Installation
2. Project Motovation
3. File Description
4. Results
5. Licensing, Authors and Acknoledgement

## Installation
This code runs with Python version 3 and requires some libraries(NumPy, Pandas, Matplotlib, Json
Plotly, Nltk, Flask, Sklearn, Sqlalchemy, Sys, Re, Pickle).<br>

Download [app](https://github.com/wythe0513/Disaster_Response/tree/master/app), [data](https://github.com/wythe0513/Disaster_Response/tree/master/data)  and [models](https://github.com/wythe0513/Disaster_Response/tree/master/models) folder belw.


## Project Motivation

For the purpose to analyze disaster data from [Figure Eight](https://appen.com/) to build a maschine leranig pipeline model for an API that classifies disaster messages so that you can send the messages to an appropriate disaster relief agency.

A data set contains real messages that were sent during disaster events.

## File Description
Following is the file structure of the project:

1. [app](https://github.com/wythe0513/Disaster_Response/tree/master/app) folder:<br>
> run.py : Flask file that runs app<br>
> templates folder:<br>
>- master.html : main page of web app<br>
>- go.html : classification result page of web app<br>


2. [data](https://github.com/wythe0513/Disaster_Response/tree/master/data) folder

>- disaster_categories.csv : data to process
>- disaster_messages.csv : data to process
>- process_data.py : model to process data
>- InsertDatabaseName.db : database to save clean data to

3. [models](https://github.com/wythe0513/Disaster_Response/tree/master/models) holder
> - train_classifier.py : model to train and store classifier
> - classifier.pkl : saved model


## Results

Run `python run.py` in the directory where app is downloaded.<br>
Go to http://0.0.0.0:3001/ (if facing problems try http://localhost:3001 in a browser)

## Licensing, Authors, Acknowledgements

Must give credit to Figure Eight for the data. You can find the Licensing for the data and other descriptive information [here](https://appen.com/).
