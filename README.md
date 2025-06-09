# 🏏 IPL Win Probability Predictor

![IPL Predictor Screenshot](/Images/IPL%20Predicter.png)

This web app predicts the win probability of IPL teams during a live match based on real-time parameters like runs, wickets, overs, and more. It is built using **Python**, **Streamlit**, and a trained **machine learning model** for classification.

---

## 🚀 Features

- Predict live win probability for either team.
- Input-based interface (team, target, score, overs, wickets).
- Interactive and mobile-responsive UI.
- Machine Learning model (Logistic Regression/Random Forest via `pipe.pkl`) trained on IPL historical data.
- Based on `matches.csv` and `deliveries.csv` datasets.

---

## 📁 Project Structure
```sh
📦 IPL-Win-Probability-Predictor
├── app.py
├── IPL Win Probability Predictor.ipynb
├── pipe.pkl
├── deliveries.csv
├── matches.csv
├── Images/
│ └── IPL Predicter.png # Your app screenshot
└── README.md
```
## 🛠️ How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/IPL-Win-Probability-Predictor.git
   cd IPL-Win-Probability-Predictor
   ```
   Install dependencies:
   ```sh
pip install -r requirements.txt
```
Run the app
```sh
streamlit run app.py
```
## 📊 Model Details
Trained on IPL ball-by-ball data (deliveries.csv) and match-level data (matches.csv), the app uses:

Custom features like current run rate, wickets in hand, overs left, etc.

A pipeline stored in pipe.pkl built in the Jupyter Notebook file.

## 👨‍💻 Author
Hridyansh Jha
