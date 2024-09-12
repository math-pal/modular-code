# from fastapi import FastAPI
from flask import Flask
from src.logger import logging
from src.exception import custom_exception
import os, sys  # os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    try:
        raise Exception("We are testing our Exception file")  # error_message
    except Exception as e:
        ML = custom_exception(e, sys)
        logging.info(ML.error_message)
        logging.info("We are testing our logging file")

        return "Welcome to FYP chatbot inside except block"  # Engineering wala Bhaiya put it over here

    # return "Welcome to FYP chatbot"

if __name__ == "__main__":
    app.run(debug=True) # default port is 5000