# 🛠️ OB/UB Classification Tool

This repository contains a **Streamlit-based GUI prototype** for classifying underground drillholes as:

- ✅ **Balanced**
- 🚧 **Overbreak-Prone**
- 🪨 **Underbreak-Prone**

using a trained **Optimised LR** , developed from operational, geotechnical, and design data.

---

## 📦 How to Run

> These instructions assume Python is installed. Use [python.org](https://www.python.org/downloads/) if needed.

### 1. Clone the Repository

```bash
git clone https://github.com/sina30nat/OB-UB-classifier.git
cd gp-logit-classifier


2. Install Requirements:
pip install -r requirements.txt

3. Launch the App
streamlit run gui_classifier.py
It will open automatically in your default browser at: http://localhost:8501

🎯 Features
Input Form: Enter 16 drill and blast design parameters

Real-time Prediction: Uses a pre-trained Logistic Regression model

Design Warnings: Examples (e.g., excessive DFE, short holes, primer location)

Lightweight GUI: Built with Streamlit for accessibility

📁 Repository Structure
gp-logit-classifier/
│
├── gui_classifier.py             # Streamlit app script
├── requirements.txt              # List of required Python packages
├── models/
│   └── logistic_regression_tuned_fitted.joblib  # Trained model
└── README.md                     # in addition to this file


🔬 Model Info
Base model: Logistic Regression (sklearn)

Tuned via: GridSearchCV with cross-validation

Features: 16 operational, design, and geotechnical parameters

Use case: Supports prediction of OB UB classification for stope design evaluation in underground mining

📄 Citation
If used in academic work, please cite the associated publication
GitHub repository: https://github.com/sina30nat/gp-logit-OB-UB-classifier

This prototype is provided for research and demonstration purposes. It is not intended for direct production use without further validation.
