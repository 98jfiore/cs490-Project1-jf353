# project1.py
import flask
import os
import random

foods = ["Tart", "Pie", "Cake", "Roll", "Donut", "Brittle", "Croissant", "Cupcake", "Fudge", "Creme"]

app = flask.Flask(__name__)

@app.route('/')
def index():
    rand_food = random.randint(0, len(foods)-1)
    return flask.render_template(
        "index.html",
        selected_food = foods[rand_food]
    )

app.run(
    port=(int(os.getenv('PORT', 8080))),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
