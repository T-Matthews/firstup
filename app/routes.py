from app import app
from flask import render_template
import random


@app.route('/')
def home():
    #THE PLAYER WHO

# random.sample(population, k, *, counts=None)
# Return a k length list of unique elements chosen from the population sequence. Used for random sampling without replacement.


    starter = ["most recently wrote a letter", "was born closest to June 22nd", "most recently went swimming","most recently visited a national park",
    "most recently left their home country","most recently was sick","most quickly loses a game of rock/paper/scissors","takes a turn first",
    "most recently ate nuts of any kind","is wearing the most colorful clothing","most recently sacrificed something",
    "is wearing the most jewelry","most closely guesses the time of day prior to looking at a clock",
    "most recently aquired a board game","most recently played a team sport","most recently ate dessert food",
    "most recently slept outside","has a photo displayed closest to themselves", "had the lowest high-school GPA",
    "has the highest charge on their phone", "has the most cash in their wallet","has done a good deed most recently",
    "has most recently had their hair cut", "the player with the least hair", "most recently slew a dragon in any way",
    "woke up earliest today","has traveled to the most countries"
    ]

    final = random.choice(starter)

    return render_template('index.html',w=final)