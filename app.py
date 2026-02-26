from flask import Flask, render_template, request
from model import financial_engine

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    income = float(request.form["income"])
    savings = float(request.form["savings"])
    age = int(request.form["age"])
    dependents = int(request.form["dependents"])
    risk = request.form["risk"]
    existing_investments = float(request.form["existing_investments"])

    rent = float(request.form.get("rent", 0) or 0)
    utilities = float(request.form.get("utilities", 0) or 0)
    food = float(request.form.get("food", 0) or 0)
    transport = float(request.form.get("transport", 0) or 0)
    emi = float(request.form.get("emi", 0) or 0)
    entertainment = float(request.form.get("entertainment", 0) or 0)
    misc = float(request.form.get("misc", 0) or 0)

    goal_name = request.form.get("goal_name")
    goal_amount = float(request.form.get("goal_amount") or 0)
    goal_years = int(request.form.get("goal_years") or 1)

    total_expenses = rent + utilities + food + transport + emi + entertainment + misc

    result = financial_engine(
        income, total_expenses, risk, goal_years
    )

    # Calculate percentages
    needs = rent + utilities + food + transport + emi
    wants = entertainment + misc
    savings_percent = (income - total_expenses) / income * 100 if income > 0 else 0
    needs_percent = needs / income * 100 if income > 0 else 0
    wants_percent = wants / income * 100 if income > 0 else 0

    warning = None
    if needs_percent > 60:
        warning = "Warning: Your essential expenses exceed 60% of income."

    return render_template(
        "result.html",
        result=result,
        needs_percent=round(needs_percent, 2),
        wants_percent=round(wants_percent, 2),
        savings_percent=round(savings_percent, 2),
        warning=warning,
        goal_name=goal_name,
        goal_amount=goal_amount,
        goal_years=goal_years
    )

if __name__ == "__main__":
    app.run(debug=True)