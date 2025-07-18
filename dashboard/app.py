import streamlit as st
import sqlite3

# Page title
st.title("📊 Demo Dashboard")

# Connect to SQLite database
def get_connection():
    try:
        conn = sqlite3.connect('data/demo.db')
        return conn
    except sqlite3.Error as e:
        st.error(f"Database connection failed: {e}")
        return None

# Main logic
def show_user_count():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            st.success(f"✅ Total users in database: {count}")
        except sqlite3.OperationalError:
            st.warning("⚠️ 'users' table not found. Please initialize the database.")
        finally:
            conn.close()

# Run the function
show_user_count()
