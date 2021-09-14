from flask import Flask
from flask.templating import render_template
import movie_api as ma

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",  movies=ma.callMovieApi()) #템플릿 폴더 안에 있으면 해석함

if __name__ == "__main__":
    app.run(debug=True)