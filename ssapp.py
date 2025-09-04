import streamlit as st
import pandas as pd
from ai_providers import ask_watson
from data_store import update_user
from insights import spending_summary
from gamification import assign_badge, progress_message
from storytelling import story_from_data

st.set_page_config(page_title="💸 Personal Finance Chatbot", layout="centered")

st.title("💸 Personal Finance Chatbot")
st.write("Your AI-powered financial guide!")

# --- User ID ---
user_id = st.text_input("Enter your name", "guest")

# --- Session State for Transactions ---
if "transactions" not in st.session_state:
    st.session_state["transactions"] = []

# --- Option 1: Manual Input ---
st.subheader("✍ Add Transaction Manually")
category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
amount = st.number_input("Amount", min_value=1, step=1)

if st.button("Add Transaction"):
    st.session_state["transactions"].append({"category": category, "amount": amount})
    update_user(user_id, "transactions", st.session_state["transactions"])
    st.success("Transaction added ✅")

# --- Option 2: Upload Bank Statement (Optional) ---
st.subheader("📂 Upload Bank Statement (Optional)")
uploaded_file = st.file_uploader("Upload your bank statement (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("✅ Statement uploaded!")

    if "Category" in df.columns and "Amount" in df.columns:
        transactions = df[["Category", "Amount"]].dropna().to_dict(orient="records")
        st.session_state["transactions"].extend(transactions)
        update_user(user_id, "transactions", st.session_state["transactions"])
        st.success(f"Added {len(transactions)} transactions from statement ✅")
    else:
        st.error("❌ CSV must have 'Category' and 'Amount' columns.")

# --- Insights ---
if st.button("Show Spending Insights"):
    if st.session_state["transactions"]:
        summary = spending_summary(st.session_state["transactions"])
        st.text(summary)
        st.text(story_from_data(user_id, summary))
    else:
        st.info("No transactions yet. Add manually or upload a statement.")

# --- AI Chatbot ---
query = st.text_input("Ask AI about your finances")
if st.button("Ask AI") and query:
    with st.spinner("Thinking..."):
        response = ask_watson(query)
    st.write("🤖 Watson says:")
    st.write(response if response else "Sorry, I couldn’t generate a response.")

# --- Gamification ---
st.subheader("🏆 Savings Tracker")
income = st.number_input("Monthly Income", min_value=0)
savings = st.number_input("Monthly Savings", min_value=0)

if income > 0:
    rate = min(savings / income, 1.0)  # clamp to 100%
    st.write(assign_badge(rate))
    st.write(progress_message(savings, income * 0.3))
