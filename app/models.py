from app import db

class Thought(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quotation = db.Column(db.Text(), index=True)
    metaphor = db.Column(db.Text(), index=True)
    comment = db.Column(db.Text())

    def __repr__(self):
        return '<Thought {}: {}>'.format(self.id, self.quotation)