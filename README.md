# 📊 Student Package Predictor — ML Dashboard

🚀 An interactive **Machine Learning web application** that predicts student placement packages based on CGPA and provides full model evaluation, analytics, and visual insights using Streamlit.

---

## 🌐 Live Demo

👉 [https://student-package-predictor-qgzssj57f9wqwpnampwdmq.streamlit.app/](https://student-package-predictor-qgzssj57f9wqwpnampwdmq.streamlit.app/)

---

## 📸 Project Preview

> Add screenshots here (recommended for LinkedIn & recruiters)

```
📊 Dashboard Overview
🎯 CGPA Input Prediction
📈 Actual vs Predicted Graph
📉 Error Distribution
```

---

## ✨ Key Features

✔ 📂 Upload your own dataset (no local file dependency)
✔ 🎯 Real-time CGPA → Package prediction
✔ 📊 Model evaluation (R² Score, MAE, RMSE)
✔ 📈 Actual vs Predicted visualization
✔ 📉 Error distribution analysis
✔ 📂 Prediction history tracking
✔ 💾 Download results as CSV report
✔ 🧠 AI-based career insights
✔ 🌗 Clean Dark/Light UI support

---

## 🧠 Problem Statement

Students often struggle to estimate their expected placement package based on academic performance.
This project solves that by using **Machine Learning regression models** to provide data-driven predictions.

---

## ⚙️ Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Core programming     |
| Streamlit    | Web app framework    |
| Pandas       | Data handling        |
| NumPy        | Numerical operations |
| Scikit-learn | Machine Learning     |
| Matplotlib   | Data visualization   |

---

## 🏗️ Project Workflow

```
Data Upload → Preprocessing → Model Prediction → Evaluation → Visualization → Insights
```

---

## 📊 Machine Learning Model

* Model Type: Linear Regression (can be upgraded to Random Forest)
* Input Feature: CGPA
* Output: Expected Placement Package (LPA)

---

## 📁 Project Structure

```
Student-Package-Predictor/
│
├── app.py                  # Streamlit application
├── lr.pkl                 # Trained ML model
├── placement_data.csv     # Dataset
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/shakshimalvi/student-package-predictor.git
cd student-package-predictor
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Example Output

| CGPA | Predicted Package (LPA) |
| ---- | ----------------------- |
| 7.0  | 11.5                    |
| 8.0  | 13.2                    |
| 9.0  | 15.0                    |

---

## 🧠 Key Learnings

✔ End-to-end ML pipeline development
✔ Model evaluation techniques
✔ Streamlit deployment
✔ Data visualization & storytelling
✔ Real-world ML application design

---

## 🚀 Future Improvements

* 🔥 Replace Linear Regression with Random Forest / XGBoost
* 📊 Add Plotly interactive dashboards
* 🧠 Add multi-feature prediction (CGPA + Projects + Skills)
* 🤖 AI-based career recommendation system
* 🌐 Deploy on cloud (AWS / HuggingFace / Render)

---

## 👨‍💻 Author

**Shakshi Malvi**
🎓 Aspiring Data Scientist | Python Developer

---

## 📌 Tags

`#MachineLearning` `#DataScience` `#Python` `#Streamlit` `#AI` `#MLProject` `#DataAnalytics`
