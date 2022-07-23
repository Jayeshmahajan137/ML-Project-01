from flask import Flask
from housing.logger import logging

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    logging.info("we are testing logging module")
    return " Starting project in machine learning, simple project for practice"

   
if __name__== "__main__":
    app.run(debug=True)
    

   
