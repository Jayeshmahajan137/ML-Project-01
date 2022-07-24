from flask import Flask


app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    
    return " Starting project in machine learning, simple project for practice"

   
if __name__== "__main__":
    app.run(debug=True)
    

   
