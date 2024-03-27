#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return(render_template("index.html"))
    
@app.route("/result", methods=["GET", "POST"])
def result():
    input = request.form.get("input")
    result = TextBlob(input).sentiment
    return(render_template("result.html", result=result))

@app.route("/end", methods=["GET", "POST"])
def end():
    return(render_template("end.html"))

if __name__ == "__main__":
    app.run()

