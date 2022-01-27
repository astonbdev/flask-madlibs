from click import prompt
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story
base_story = silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

STORIES = [silly_story, excited_story]

@app.get("/")
@app.get("/questions")
def show_homepage():
    """Starts madlibs homepage"""
    
    return render_template("questions.html", prompts=base_story.prompts)

@app.get("/results")
def show_story():
    """displays story from questions.html form"""
    print(request.args["Story Select"])
    # new_story = base_story.generate(request.args["Story Select"])


    return render_template("questions.html", prompts=STORIES[int(request.args["Story Select"])].prompts)

@app.get("/selectStory")
def select_story():

    return render_template("storyPicker.html", stories = STORIES)


