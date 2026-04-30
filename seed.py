from app import app
from database import db
from models import Order
import random

with app.app_context():
 for _ in range(100):
  db.session.add(Order(
    customers=random.randint(20, 100),
    hour=random.randint(10, 22)
))
  db.session.commit()
