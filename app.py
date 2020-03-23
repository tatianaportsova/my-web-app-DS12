
# app.py

from flask import Flask
app = Flask(__name__)
# print (__name__) # if __name__ == main (same thing)

@app.route("/")
def hello():
    print("VISIT THE HELLO PAGE")
    return "Hello World!"

@app.route("/about")
def about():
    print("VISITED THE ABOUT ME PAGE")
    return "About Me!"