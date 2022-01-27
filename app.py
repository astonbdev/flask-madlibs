from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

story = silly_story

@app.get("/")
@app.get("/questions")
def show_homepage():
    """Starts homepage"""
    
    return render_template("questions.html", prompts=story.prompts)


