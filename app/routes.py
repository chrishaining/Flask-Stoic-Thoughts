from app import app, db
from app.models import Thought
from flask import render_template, redirect, request
import random
from sqlalchemy import update

# create index page, and show a random thought
@app.route('/')
def index():
    thoughts = Thought.query.all()
    thought = random.choice(thoughts)
    return render_template('index.html', thoughts=thoughts, thought=thought)


# show all thoughts
@app.route('/thoughts_controller')
def show_all_thoughts():
    thoughts = Thought.query.all()
    return render_template('thoughts_controller.html', thoughts=thoughts)


# add a Thought
@app.route('/thoughts_controller', methods=['POST'])
def add_thought():
    quotation = request.form['quotation']
    metaphor = request.form['metaphor']
    comment = request.form['comment']
    newThought = Thought(quotation=quotation, metaphor=metaphor, comment=comment)
    db.session.add(newThought)
    db.session.commit()
    return redirect('/thoughts_controller')

# edit a Thought


# delete a Thought


# a carousel view of the thoughts. 
@app.route('/carousel')
def show_carousel():
    thoughts = Thought.query.all()
    return render_template('carousel.html', thoughts=thoughts)

