# Smart-Lead-Ai
This repository is for practicing Ai/Ml Project.


# 🚀 Smart Lead AI: End-to-End Machine Learning Project

### *Predicting Customer Conversion with 91% Accuracy*

Welcome to **Smart Lead AI**, a full-stack machine learning application designed to help businesses identify high-potential customers. 

I built this project from scratch—starting from generating my own dataset, training a predictive model, and deploying it as a live web application. It demonstrates the complete lifecycle of an AI project, from raw data to a user-friendly product.

---

## 🗺️ The Journey: How I Built It

This wasn't just about writing code; it was about solving a business problem. Here is the roadmap of how I took this from an idea to a deployed app:

### Phase 1: Data Generation (The "Architect" Phase)
I didn't want to rely on a clean, pre-made Kaggle dataset. I wanted to simulate real-world chaos.
* **What I did:** I wrote a Python script using `Faker` and `NumPy` to generate **1,000 synthetic leads**.
* **The Logic:** I engineered realistic patterns (e.g., "Users who spend more time on the site and open emails are more likely to convert").
* **Outcome:** A raw dataset (`lead_data.csv`) mimicking real user behavior.

### Phase 2: Data Detective (EDA & Preprocessing)
Before modeling, I needed to understand the data.
* **Cleaning:** I handled categorical data (like Country and Lead Source) using **One-Hot Encoding**.
* **Exploration:** I used Seaborn/Matplotlib to visualize correlations. I confirmed that features like `Interaction Score` and `Previous Purchases` were strong indicators of conversion.
* **Outcome:** A clean, numerical dataset ready for the algorithm.

### Phase 3: Model Training (The "Brain")
This is where the magic happens.
* **Algorithm:** I chose **Logistic Regression** for its efficiency and interpretability in binary classification tasks.
* **Validation:** I split the data (80% train / 20% test) to ensure the model wasn't just memorizing answers.
* **Result:** The model achieved **91% Accuracy** on unseen data.
* **Saving:** I serialized the trained model using `joblib` so it could be reused without retraining.

### Phase 4: Deployment (The Web App)
A model inside a notebook is useless to a marketing team. I needed an interface.
* **Backend:** I built a lightweight server using **Flask** to handle requests and load the trained model.
* **Frontend:** I designed a clean HTML/CSS form where users can input lead details.
* **Feature:** The app returns not just a "Yes/No" prediction, but an exact **Probability Score** (e.g., "92.5% Chance").

---

## 🛠️ Tech Stack

* **Language:** Python 3.10
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Logistic Regression)
* **Web Framework:** Flask
* **Serialization:** Joblib
* **Version Control:** Git & GitHub

---

## 💻 How to Run This Project

Want to try it out on your own machine? Follow these steps:

**1. Clone the Repository**
```bash
git clone [https://github.com/Mridul010/Smart-Lead-Ai.git](https://github.com/Mridul010/Smart-Lead-Ai.git)
cd Smart-Lead-Ai

2. Create a Virtual Environment
python -m venv venv
# Windows:
.\venv\Scripts\Activate.ps1
# Mac/Linux:
source venv/bin/activate

3. Install Dependencies
pip install pandas numpy scikit-learn flask joblib faker


4. Run the App
python app.py


Project Structure
Smart Lead AI/
├── app.py                 # The Flask Application (Backend)
├── requirements.txt       # List of dependencies
├── README.md              # Project Documentation
├── data/
│   ├── lead_data.csv            # Raw generated data
│   └── lead_data_processed.csv  # Cleaned data for training
├── model/
│   └── model.pkl          # The saved machine learning model
├── notebooks/
│   ├── data_generation.ipynb    # Script to create synthetic data
│   ├── data_prep.ipynb          # EDA and Preprocessing
│   └── model_training.ipynb     # Training and Evaluation
└── templates/
    └── index.html         # The Frontend User Interface



Author: Mridul

Aspiring AI/ML Engineer
