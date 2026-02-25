from flask import Flask, render_template, request

app = Flask(__name__)

def financial_engine(income, expenses, risk, duration):

    # Basic calculations
    surplus = income - expenses

    # 50-30-20 Rule Recommendation
    recommended_needs = income * 0.5
    recommended_wants = income * 0.3
    recommended_savings = income * 0.2

    # Emergency Fund (6 months expenses)
    emergency_required = expenses * 6

    # Investment Allocation Based on Risk
    if risk == "Low":
        allocation = {
            "Fixed Deposit": 40,
            "PPF": 30,
            "Gold": 15,
            "Emergency": 15
        }
        expected_return = 0.06

    elif risk == "Medium":
        allocation = {
            "Mutual Funds": 45,
            "Fixed Deposit": 25,
            "Gold": 10,
            "Emergency": 20
        }
        expected_return = 0.10

    else:
        allocation = {
            "Stocks": 60,
            "Mutual Funds": 20,
            "Gold": 10,
            "Emergency": 10
        }
        expected_return = 0.15

    # Suggested Investment Amount
    invest_amount = surplus * 0.75
    emergency_allocation = surplus * 0.25

    # Inflation adjusted return
    inflation = 0.06
    real_return = expected_return - inflation

    yearly_investment = invest_amount * 12

    if real_return > 0:
        future_value = yearly_investment * (((1 + real_return) ** duration - 1) / real_return)
    else:
        future_value = yearly_investment * duration

    # Financial Health Score
    savings_ratio = surplus / income if income > 0 else 0
    emergency_ratio = min(emergency_allocation / emergency_required, 1) if emergency_required > 0 else 0

    health_score = round((savings_ratio * 50) + (emergency_ratio * 50), 2)

    # Beginner Investment Roadmap
    roadmap = []

    if surplus <= 0:
        roadmap.append("Reduce expenses before investing.")
    else:
        roadmap.append("Step 1: Build 6 months emergency fund.")
        roadmap.append("Step 2: Start SIP in Mutual Funds (₹2000-5000).")
        roadmap.append("Step 3: Diversify into Gold or FD.")
        roadmap.append("Step 4: Increase investment by 10% yearly.")

    return {
        "surplus": surplus,
        "recommended_needs": recommended_needs,
        "recommended_wants": recommended_wants,
        "recommended_savings": recommended_savings,
        "emergency_required": emergency_required,
        "allocation": allocation,
        "invest_amount": invest_amount,
        "future_value": round(future_value, 2),
        "health_score": health_score,
        "roadmap": roadmap
    }


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    income = float(request.form['income'])
    expenses = float(request.form['expenses'])
    risk = request.form['risk']
    duration = int(request.form['duration'])

    result = financial_engine(income, expenses, risk, duration)

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)