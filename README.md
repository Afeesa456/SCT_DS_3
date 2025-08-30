# SCT_DS_3

# 🌐 Bank Marketing - Decision Tree Classifier

This project uses the **Bank Marketing Dataset** from the **UCI Machine Learning Repository** to build a **Decision Tree Classifier** that predicts whether a customer will subscribe to a term deposit (purchase a product/service) based on their **demographic** and **behavioral** data.

---

## 📌 Project Overview
- **Objective**: Predict customer purchase decisions (Yes/No).  
- **Dataset**: `bank-full.csv` (UCI ML Repository).  
- **Approach**:
  1. Load and explore the dataset
  2. Data preprocessing (handle categorical variables, missing values, etc.)
  3. Train a **Decision Tree Classifier**
  4. Evaluate performance using accuracy, confusion matrix, and classification report

---

## 📂 Dataset Information
The dataset contains information about customers contacted during a direct marketing campaign.  

**Features include:**
- Demographic: `age`, `job`, `marital`, `education`
- Financial: `balance`, `housing`, `loan`
- Campaign-related: `contact`, `day`, `month`, `duration`, `campaign`, `pdays`, `previous`, `poutcome`
- **Target variable**: `y` (Yes = purchased, No = not purchased)

---

## 🛠️ Technologies Used
- **Python**  
- **Pandas** (data manipulation)  
- **Scikit-learn** (machine learning model)  
- **Matplotlib / Seaborn** (visualizations
