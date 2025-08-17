import streamlit as st
import sqlite3
from datetime import date

# Function to insert transaction
def add_transaction(date, description, amount, category):
    conn = sqlite3.connect("finance.db")
    c = conn.cursor()
    c.execute("INSERT INTO transactions (date, description, amount, category) VALUES (?, ?, ?, ?)",
              (date, description, amount, category))
    conn.commit()
    conn.close()

st.title("💰 Personal Finance Tracker")

def predict_category(description):
    desc = description.lower()
    if any(word in desc for word in ["pizza", "burger", "restaurant", "food", "dinner", "lunch"]):
        return "Food"
    elif any(word in desc for word in ["uber", "bus", "train", "metro", "cab", "taxi"]):
        return "Transport"
    elif any(word in desc for word in ["shirt", "shoes", "shopping", "clothes", "amazon"]):
        return "Shopping"
    elif any(word in desc for word in ["electricity", "water", "wifi", "rent", "bill"]):
        return "Bills"
    else:
        return "Other"


with st.form("transaction_form"):
    t_date = st.date_input("Date", date.today())
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    
    # Predict category if description is provided
    predicted_category = ""
    if description:
        predicted_category = predict_category(description)

    # Let user pick category (default = predicted one)
    category = st.selectbox(
        "Category (auto-suggested below 👇)",
        ["Food", "Transport", "Shopping", "Bills", "Other"],
        index=["Food", "Transport", "Shopping", "Bills", "Other"].index(predicted_category) if predicted_category else 4
    )

    # Show suggestion hint
    if predicted_category:
        st.info(f"💡 Suggested category: {predicted_category}")

    # Submit button
    submitted = st.form_submit_button("Add Transaction")

    if submitted:
        add_transaction(t_date, description, amount, category)
        st.success("Transaction added successfully!")

