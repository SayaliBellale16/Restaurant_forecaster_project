from flask import Flask, request, jsonify
from database import db
from models import Order, Feedback
from forecast import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/add_order', methods=['POST'])
def add_order():

     data = request.json
     order = Order(customers=data['customers'], hour=data['hour'])
     db.session.add(order)
     db.session.commit()
     return jsonify({"msg": "order added"})


@app.route('/forecast', methods=['GET'])
def forecast():
    orders = Order.query.all()

    factor = get_adjustment(db)
    hourly = predict_hourly_ml(orders, factor)
    total = total_customers(hourly)
    staff = predict_staff_roles(total)
    inventory = predict_inventory(total)

    return jsonify({
            "hourly": hourly,
             "total": total,
             "staff": staff,
              "inventory": inventory,
              "adjustment_factor": factor
            })


@app.route('/feedback', methods=['POST'])
def feedback():
  data = request.json

  fb = Feedback(
    predicted=data['predicted'],
    actual=data['actual'],
    reason=data.get('reason', '')
)
  db.session.add(fb)
  db.session.commit()

  apply_feedback(
    data['predicted'],
    data['actual'],
    data.get('reason', ''),
    db
)

  return jsonify({"msg": "model updated"})


if __name__ == '__main__':
 app.run(debug=True)
