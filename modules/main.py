#!/usr/bin/env python

from flask import Flask, render_template

#create instance of Flask app
app = Flask(__name__)

#decorator
@app.route("/")
def hello():
    text = "Hello World"
    #note: the below html_page_text is probably not a variable I would use, but it
    # is intended to help you understand how render_template connects to index.html
    return render_template('index.html', html_page_text=text)

if __name__ == "__main__":
    app.run(debug=True)


