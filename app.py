import streamlit as st
import pandas as pd

st.title("💰 Personal Expense Tracker")

# This will hold our expenses in memory while the app runs
if "expenses" not in st.session_state:
    st.session_state.expenses = []

with st.form("expense_form"):
    col1, col2 = st.columns(2)
    with col1:
        amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
        category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
    with col2:
        date = st.date_input("Date")
        note = st.text_input("Note (optional)")
    
    submitted = st.form_submit_button("Add Expense")
    if submitted:
        st.session_state.expenses.append({
            "Date": date, "Category": category, "Amount": amount, "Note": note
        })
        st.success("Expense added!")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.subheader("All Expenses")
    st.dataframe(df, use_container_width=True)
    total = df["Amount"].sum()
    st.metric("Total Spent", f"₹{total:,.2f}")

    st.subheader("Spending by Category")
    category_totals = df.groupby("Category")["Amount"].sum()
    st.bar_chart(category_totals)
        