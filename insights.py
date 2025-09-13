# insights.py
from collections import defaultdict

def spending_summary(transactions):
    totals = defaultdict(int)
    for t in transactions:
        totals[t["category"]] += t["amount"]

    summary_lines = [f"{cat}: ₹{amt}" for cat, amt in totals.items()]
    total_spent = sum(totals.values())
    summary_lines.append(f"Total Spent: ₹{total_spent}")
    return "\n".join(summary_lines)
