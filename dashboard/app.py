import streamlit as st
import sqlite3

# Connect to database
conn = sqlite3.connect('data/demo.db')
c = conn.cursor()

st.title("📊 Demo Dashboard")

# Example: Show number of users (if table exists)
try:
    c.execute("SELECT COUNT(*) FROM users")
    count = c.fetchone()[0]
    st.success(f"Total users in database: {count}")
except:
    st.warning("Users table not found. Please initialize the database.")

conn.close()
