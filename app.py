import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="ML Dashboard Pro", layout="wide")

st.title("📊 Student Package Predictor PRO")

# -----------------------------
# SESSION STATE (HISTORY STORE)
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["CGPA", "Predicted Package"])

# -----------------------------
# LOAD DATA
# -----------------------------
st.sidebar.subheader("📂 Upload Dataset")
file_path = st.sidebar.text_input("Enter CSV Path")

df = None

if file_path:
    try:
        df = pd.read_csv(file_path)
        st.success("Dataset Loaded")
    except:
        st.error("Invalid file path")

if df is None:
    st.stop()

st.dataframe(df, use_container_width=True)

# -----------------------------
# SPLIT DATA (Actual vs Predicted)
# -----------------------------
y_test = df.iloc[:, 0]
y_pred = df.iloc[:, 1]

# -----------------------------
# METRICS
# -----------------------------
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

st.subheader("📊 Model Performance")

c1, c2, c3 = st.columns(3)
c1.metric("R² Score", f"{r2:.2f}")
c2.metric("MAE", f"{mae:.2f}")
c3.metric("RMSE", f"{rmse:.2f}")

# -----------------------------
# 📈 PLOT 1: ACTUAL VS PREDICTED
# -----------------------------
st.subheader("📈 Actual vs Predicted")

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.plot([y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()],
        'r--')

st.pyplot(fig)

# -----------------------------
# 🎯 PREDICTION INPUT
# -----------------------------
st.subheader("🎯 Predict Package")

cgpa = st.number_input("Enter CGPA", 0.0, 10.0, 7.0)

# simple demo model (replace with your ML model)
predicted = 1.8 * cgpa + 2

if st.button("Predict"):
    st.success(f"🎯 Predicted Package: {predicted:.2f} LPA")

    # save history
    new_row = pd.DataFrame([[cgpa, predicted]], columns=["CGPA", "Predicted Package"])
    st.session_state.history = pd.concat([st.session_state.history, new_row], ignore_index=True)

# -----------------------------
# 📊 HISTORY TABLE
# -----------------------------
st.subheader("📂 Prediction History")
st.dataframe(st.session_state.history, use_container_width=True)

# -----------------------------
# 📊 CGPA vs PACKAGE TREND
# -----------------------------
if len(st.session_state.history) > 1:
    st.subheader("📊 CGPA vs Package Trend")

    fig2, ax2 = plt.subplots()
    ax2.scatter(st.session_state.history["CGPA"],
                st.session_state.history["Predicted Package"])

    ax2.set_xlabel("CGPA")
    ax2.set_ylabel("Package (LPA)")
    ax2.set_title("Trend Analysis")

    st.pyplot(fig2)

# -----------------------------
# 💾 DOWNLOAD REPORT
# -----------------------------
st.subheader("💾 Download Report")

csv = st.session_state.history.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download CSV",
    csv,
    "prediction_history.csv",
    "text/csv"
)

# -----------------------------
# 🧠 AI EXPLANATION
# -----------------------------
st.subheader("🧠 AI Insight")

if cgpa >= 8:
    st.info("High CGPA strongly increases chances of higher package due to better academic performance + skills.")
elif cgpa >= 6:
    st.info("Moderate CGPA → Focus on projects + skills to improve package.")
else:
    st.warning("Low CGPA → Improve skills, DSA, and projects for better placement opportunities.")