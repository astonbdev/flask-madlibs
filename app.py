from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
base_story = silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)



@app.get("/")
@app.get("/questions")
def show_homepage():
    """Starts madlibs homepage"""
    
    return render_template("questions.html", prompts=base_story.prompts)

@app.get("/results")
def show_story():
    """displays story from questions.html form"""

    new_story = base_story.generate(request.args)

    return render_template("story.html", story=new_story)


