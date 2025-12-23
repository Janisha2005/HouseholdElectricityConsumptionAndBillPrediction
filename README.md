# ⚡ Household Electricity Consumption & Bill Prediction

An **end-to-end Machine Learning web application** that predicts **monthly household electricity consumption (kWh)** and estimates the **electricity bill (₹)** using historical power usage data.

This project focuses on **model performance, real-world relevance, and deployable UI design**.

---

## 🚀 Project Overview

Electricity consumption forecasting helps households and utilities:
- Understand usage patterns  
- Control energy costs  
- Improve demand planning  

This application uses a **Random Forest Regressor** to accurately predict energy usage and converts it into a **monthly electricity bill estimate**, delivered through an interactive **Streamlit web app**.

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Regressor  
- **Why Random Forest?**
  - Captures non-linear relationships
  - Reduces overfitting compared to single decision trees
  - Provides stable and reliable predictions

### 📊 Model Performance

| Metric | Train | Test |
|------|------|------|
| MAE | 35.75 | 31.25 |
| RMSE | 54.63 | 37.91 |
| R² | 0.95 | 0.94 |

✔ Strong generalization  
✔ Minimal overfitting  
✔ High predictive accuracy  

---

## 📂 Dataset

- **Source:** Household Power Consumption Dataset (Kaggle)  
- **Granularity:** Monthly aggregated data  
- **Key Features:**
  - Global Active Power  
  - Global Reactive Power  
  - Voltage  
  - Global Intensity  
  - Sub-metering (Kitchen, Laundry, Heating)

---

## 🛠 Tech Stack

- **Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn  
- **Model Persistence:** Joblib  
- **Web Framework:** Streamlit  
- **UI Styling:** Custom CSS (glass-morphism, blurred sidebar)

---

## ✨ Application Features

- Interactive sidebar inputs  
- Real-time prediction of:
  - Monthly electricity consumption (kWh)
  - Estimated electricity bill (₹)  
- Premium dark UI with **blurred transparent sidebar**  
- Clean, intuitive, and deployment-ready interface  
