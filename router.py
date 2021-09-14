from flask import Flask
from flask.templating import render_template
from requests.api import request
import movie_api as ma
import temperature as tem

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",  movies=ma.callMovieApi(), temp=tem.temp(), temp2=tem.temp2()) 


if __name__ == "__main__":
    app.run(debug=True)