from database import db
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customers = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    predicted = db.Column(db.Integer)
    actual = db.Column(db.Integer)
    reason = db.Column(db.String(200))


class ModelConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adjustment_factor = db.Column(db.Float, default=1.0)