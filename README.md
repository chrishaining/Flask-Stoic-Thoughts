# Flask Stoic Quotations App
A web app of quotations/thoughts. It allows users to:
* view a randomly-selected thought, displayed in a flip-card format
* view a randomly-select thought, displayed in a collapsible card format
* view a list of all the thoughts
* add, edit and delete thoughts
* view thoughts in a carousel format

## Features/skills I developed
* Bootstrap's Carousel feature
* Bootstrap's collapse feature

## Languages, Packages, Frameworks
* Python3
* pip3 for installing packages
* flask 
* flask-sqlalchemy
* flask-migrate

## Some things I would change and/or things to explore further
I've hard-coded the items to be displayed in the carousel, by listing the first five items by index. I tried to iterate through all the items, but it didn't work and it wasn't important enough to keep trying. However, it would be nice to have a way to display all the items in a carousel. Since I have only a limited number of images to add to the cards, it would be necessary to work out how to assign images (perhaps by randomly assigning one of the images).

<p>
<img src="/app/static/storm.jpg" alt="Stormy seas" width="400" height="300">
<img src="/app/static/calm.jpeg" alt="Calm seas" width="400" height="300">
</p>

