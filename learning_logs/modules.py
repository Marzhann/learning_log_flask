from learning_log_flask.extentions import db

from datetime import datetime


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    time_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    owner_id = db.Column(db.String(64), db.ForeignKey('user.id'))
    owner = db.relationship('User', backref=db.backref('topics', lazy=True))

    def __repr__(self):
        return f'<Topic {self.name}>'

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    time_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    topic = db.relationship('Topic', backref=db.backref('entries', lazy=True))

    def __repr__(self):
        return f'<Entry {self.text}>'
     

