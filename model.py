import joblib

# Load trained ML model
model = joblib.load("Models/investment_model.pkl")

def risk_mapping(risk):
    if risk == "Low":
        return 0
    elif risk == "Medium":
        return 1
    else:
        return 2

def financial_engine(income, expenses, risk, duration):

    surplus = income - expenses

    # 50-30-20 Rule
    recommended_needs = income * 0.5
    recommended_wants = income * 0.3
    recommended_savings = income * 0.2

    # Emergency Fund (6 months)
    emergency_required = expenses * 6

    # Risk mapping for ML
    risk_level = risk_mapping(risk)

    # ML Prediction
    future_value = model.predict([[income, expenses, duration, risk_level]])[0]

    # Financial Health Score
    savings_ratio = surplus / income if income > 0 else 0
    emergency_ratio = min(surplus / emergency_required, 1) if emergency_required > 0 else 0
    health_score = round((savings_ratio * 50) + (emergency_ratio * 50), 2)

    # Investment Allocation Logic
    if risk == "Low":
        allocation = {
            "Fixed Deposit": 40,
            "PPF": 30,
            "Gold": 20,
            "Emergency": 10
        }
    elif risk == "Medium":
        allocation = {
            "Mutual Funds": 45,
            "FD": 25,
            "Gold": 15,
            "Emergency": 15
        }
    else:
        allocation = {
            "Stocks": 60,
            "Mutual Funds": 25,
            "Gold": 10,
            "Emergency": 5
        }

    roadmap = []

    if surplus <= 0:
        roadmap.append("Reduce unnecessary expenses.")
    else:
        roadmap.append("Build emergency fund first.")
        roadmap.append("Start SIP ₹2000-5000.")
        roadmap.append("Increase investment 10% yearly.")
        roadmap.append("Diversify portfolio gradually.")

    return {
        "surplus": surplus,
        "recommended_needs": recommended_needs,
        "recommended_wants": recommended_wants,
        "recommended_savings": recommended_savings,
        "emergency_required": emergency_required,
        "future_value": round(future_value, 2),
        "health_score": health_score,
        "allocation": allocation,
        "roadmap": roadmap
    }