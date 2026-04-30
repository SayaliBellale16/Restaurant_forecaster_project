import numpy as np
from sklearn.linear_model import LinearRegression
import datetime
from models import ModelConfig

model = LinearRegression()


def get_adjustment(db):
    config = db.session.query(ModelConfig).first()
    return config.adjustment_factor if config else 1.0


def train_model(orders):
    X, y = [], []

    for o in orders:
        day = o.created_at.weekday()
        is_weekend = 1 if day >= 5 else 0

        X.append([o.hour, day, is_weekend])
        y.append(o.customers)

    if len(X) > 5:
        model.fit(X, y)


def predict_ml(hour, day):
    is_weekend = 1 if day >= 5 else 0
    return int(model.predict([[hour, day, is_weekend]])[0])


def predict_hourly_ml(orders, factor):
    train_model(orders)

    hourly = {}
    today = datetime.datetime.now().weekday()

    for h in range(24):
        try:
            pred = predict_ml(h, today)
            hourly[h] = max(0, int(pred * factor))
        except Exception:
            hourly[h] = 0

    return hourly


def total_customers(hourly):
    return sum(hourly.values())


def predict_staff_roles(total):
    return {
        "chef": max(1, total // 20),
        "waiter": max(1, total // 10),
        "cashier": 1
    }


def predict_inventory(total):
    return {
        "cheese": {"required": round(total * 0.2, 2)},
        "tomato": {"required": round(total * 0.3, 2)},
        "dough": {"required": round(total * 0.25, 2)}
    }


def adjust_reason(reason, factor):
    if not reason:
        return factor

    r = reason.lower()
    if "rain" in r:
        return factor * 0.9
    elif "holiday" in r:
        return factor * 1.2
    return factor


def apply_feedback(predicted, actual, reason, db):
    config = db.session.query(ModelConfig).first()

    if not config:
        config = ModelConfig(adjustment_factor=1.0)
        db.session.add(config)

    error = actual - predicted
    factor = adjust_reason(reason, config.adjustment_factor)

    if predicted > 0:
        factor += (error / predicted) * 0.1

    config.adjustment_factor = factor
    db.session.commit()