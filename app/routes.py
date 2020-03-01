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
@app.route('/thoughts_controller/<int:thought_id>/edit', methods=['POST'])
def edit(thought_id):
    new_quotation = request.form.get("new_quotation")
    new_metaphor = request.form.get("new_metaphor")
    new_comment = request.form.get("new_comment")
    thought_id = request.form.get("thought_id")
    thought = Thought.query.filter_by(id=thought_id).first()
    thought.quotation = new_quotation
    thought.metaphor = new_metaphor
    thought.comment = new_comment
    db.session.commit()
    return redirect('/thoughts_controller')

# delete a Thought
@app.route('/thoughts_controller/<int:thought_id>/delete', methods=['POST'])
def delete(thought_id):
    thought = Thought.query.get(thought_id)
    db.session.delete(thought)
    db.session.commit()
    return redirect('/thoughts_controller')

# a carousel view of the thoughts. 
@app.route('/carousel')
def show_carousel():
    thoughts = Thought.query.all()
    return render_template('carousel.html', thoughts=thoughts)


# show an accordion view. 
@app.route('/accordion')
def show_accordion():
    thoughts = Thought.query.all()
    thought = random.choice(thoughts)
    return render_template('accordion.html', thoughts=thoughts, thought=thought)
