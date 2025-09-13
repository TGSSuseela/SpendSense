# gamification.py
def assign_badge(rate: float) -> str:
    if rate >= 0.3:
        return "🏅 Smart Saver Badge – You’re saving more than 30% of your income!"
    elif rate >= 0.2:
        return "🎖️ Budget Balancer Badge – You’re doing well!"
    else:
        return "💡 Try to increase your savings to earn a badge!"

def progress_message(savings: float, target: float) -> str:
    if savings >= target:
        return f"🔥 Great job! You reached your savings target of ₹{target}."
    else:
        return f"👉 You’ve saved ₹{savings}. Try reaching ₹{target} next time!"
