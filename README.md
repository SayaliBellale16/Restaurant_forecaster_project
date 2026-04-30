# Restaurant ML Forecast System

## Setup
pip install -r requirements.txt

## Run
python app.py

## APIs

### Add Order
POST /add_order
{
  "customers": 10,
  "hour": 12
}

### Forecast
GET /forecast

### Feedback
POST /feedback
{
  "predicted": 100,
  "actual": 80,
  "reason": "rain"
}

## Tests
python -m unittest discover tests

* Include all required artifacts, especially the dataset, so the work can be fully evaluated. * Add automated tests (unit and integration) to validate functionality and improve reliability. * Improve documentation with clear setup steps, API details, input/output formats, and example workflows. * Ensure all acceptance criteria are fully met before submission. * Add proper error handling and input validation to make the application more robust. can you add this in to that code and give me full code

how to run project

git clone <repo>
cd project
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python app.py

2. API Details

👉 कोणते APIs आहेत


Example:

POST /add_order
GET /forecast
POST /feedback

3. Input / Output Format

👉 API ला काय द्यायचं + काय मिळणार

Example:

Add Order

Input:

{
  "customers": 10,
  "hour": 14
}

Output:

{
  "msg": "order added"
}

4. Example Workflow (VERY IMPORTANT 🔥)

👉 real use-case flow

Example:

Step 1:

POST /add_order

Step 2:

GET /forecast

Step 3:

POST /feedback

👉 म्हणजे system कसा वापरायचा ते दाखवायचं

5. Project Explanation

👉 2–3 lines:

ML use केलंय
prediction system आहे
feedback loop आहे




###real project workflow

# 🍽️ Restaurant ML Forecast System

A Flask-based Machine Learning system that predicts customer demand, optimizes staff planning, and manages inventory using historical order data and a feedback loop.

---

# 🚀 Features

* 📊 Hourly customer prediction using ML
* 👨‍🍳 Staff planning (chef, waiter, cashier)
* 📦 Inventory estimation (cheese, tomato, dough)
* 🔁 Feedback loop to improve prediction accuracy
* ✅ Input validation & error handling
* 🧪 Unit and integration tests included

---

# 🛠️ Tech Stack

* Python (Flask)
* SQLite (Database)
* SQLAlchemy (ORM)
* Scikit-learn (ML Model)

---

# ⚙️ Setup Instructions

## 1. Clone the Repository

```bash
git clone <your-repo-url>
cd restaurant_ml
```

## 2. Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate   # Windows
# source env/bin/activate  # Mac/Linux
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Application

```bash
python app.py
```

👉 App will run at:

```
http://127.0.0.1:5000
```

---

# 📡 API Endpoints

## 1. Add Order

**POST** `/add_order`

### Request:

```json
{
  "customers": 10,
  "hour": 14
}
```

### Response:

```json
{
  "msg": "order added"
}
```

---

## 2. Get Forecast

**GET** `/forecast`

### Response:

```json
{
  "hourly": {
    "9": 10,
    "10": 15
  },
  "total": 120,
  "staff": {
    "chef": 6,
    "waiter": 12,
    "cashier": 1
  },
  "inventory": {
    "cheese": {"required": 24.0},
    "tomato": {"required": 36.0},
    "dough": {"required": 30.0}
  },
  "adjustment_factor": 1.1
}
```

---

## 3. Submit Feedback

**POST** `/feedback`

### Request:

```json
{
  "predicted": 120,
  "actual": 90,
  "reason": "rain"
}
```

### Response:

```json
{
  "msg": "model updated"
}
```

---

# 🔄 Example Workflow

### Step 1: Add Orders

```bash
POST /add_order
```

### Step 2: Get Prediction

```bash
GET /forecast
```

### Step 3: Provide Feedback

```bash
POST /feedback
```

👉 System will adjust predictions based on real data.

---

# 🧠 How It Works

* Uses Linear Regression model to predict customer demand
* Considers:

  * Hour of the day
  * Day of the week
  * Weekend vs weekday
* Applies adjustment factor based on feedback
* Continuously improves using real-world corrections

---

# 🧪 Running Tests

```bash
python -m unittest discover tests
```

---

# 📁 Dataset

Sample dataset is included in:

```
sample_data.csv
```

---

# ⚠️ Error Handling

* Validates input data (customers, hour)
* Handles invalid API requests
* Prevents crashes using try-catch blocks

---

# 📌 Future Improvements

* Docker support
* CI/CD pipeline
* Frontend dashboard (React)
* Model persistence (save/load ML model)
* Authentication (JWT)

---

# 👩‍💻 Author

Sayali Bellale

---

# ⭐ Summary

This project demonstrates:

* Real-world ML integration
* REST API development
* Feedback-driven model improvement
* Production-ready backend design

