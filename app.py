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

with st.form("transaction_form"):
    t_date = st.date_input("Date", date.today())
    description = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
    submitted = st.form_submit_button("Add Transaction")

    if submitted:
        add_transaction(t_date, description, amount, category)
        st.success("Transaction added successfully!")
