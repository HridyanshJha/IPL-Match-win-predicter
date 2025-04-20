import streamlit as st
import pandas as pd
import pickle

# Setting up page config
st.set_page_config(page_title='IPL Win Predictor', page_icon='🏏', layout='centered')

# Apply enhanced styling with background image and text colors
st.markdown("""
    <style>
        .stApp {
            background: url('https://www.shutterstock.com/shutterstock/videos/3447451967/thumb/1.jpg?ip=x480') no-repeat center center fixed;
            background-size: cover;
            color: #E0E0E0;
        }
        .css-18e3th9 {
            background-color: #FF5733 !important;
            color: #FFFFFF !important;
            font-weight: bold !important;
            border-radius: 10px;
        }
        .css-1cpxqw2 {
            background-color: #FF5733 !important;
            color: #FFFFFF !important;
        }
        .stButton>button {
            background-color: #28A745 !important;
            color: #FFFFFF !important;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #218838 !important;
        }
        .stMarkdown h1 {
            font-size: 2.5rem;
            color: #FFD700;
        }
        .stMarkdown h2, label {
            color: #F8F9FA !important;
            font-weight: bold;
        }
        hr {
            border: 2px solid #FF5733;
        }
    </style>
""", unsafe_allow_html=True)

# Declaring the teams
teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Kings XI Punjab',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals']

# Declaring the venues
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl', 'rb'))

# Title with style
st.markdown("""
    <h1 style='text-align: center; color: #FF5733;'>IPL Win Predictor 🏏</h1>
    <hr style='border: 2px solid #FF5733;'>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    battingteam = st.selectbox('🏏 Select the Batting Team', sorted(teams))

with col2:
    bowlingteam = st.selectbox('🎯 Select the Bowling Team', sorted(teams))

city = st.selectbox('📍 Select Match Venue', sorted(cities))

target = st.number_input('🎯 Target Score', min_value=1, step=1)

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('🏏 Current Score', min_value=0, step=1)

with col4:
    overs = st.number_input('⏳ Overs Completed', min_value=0.0, max_value=20.0, step=0.1)

with col5:
    wickets = st.number_input('⚡ Wickets Fallen', min_value=0, max_value=10, step=1)

if st.button('📊 Predict Probability', help='Click to get win probability'):
    
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    currentrunrate = score / overs if overs > 0 else 0
    requiredrunrate = (runs_left * 6) / balls_left if balls_left > 0 else 0

    input_df = pd.DataFrame({
        'batting_team': [battingteam],
        'bowling_team': [bowlingteam],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs_x': [target],
        'cur_run_rate': [currentrunrate],
        'req_run_rate': [requiredrunrate]
    })

    result = pipe.predict_proba(input_df)
    lossprob = result[0][0]
    winprob = result[0][1]

    st.markdown(f"""
        <h2 style='text-align: center; color: #28A745;'>{battingteam} - {round(winprob*100)}%</h2>
        <h2 style='text-align: center; color: #DC3545;'>{bowlingteam} - {round(lossprob*100)}%</h2>
    """, unsafe_allow_html=True)
