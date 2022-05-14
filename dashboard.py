import pandas as pd
import numpy
import streamlit as st
import os
import pickle
from sklearn.preprocessing import StandardScaler
from PIL import Image
# setting path to file and folders
user_df= pd.read_csv("./data/teleco_user_sat_data.csv")

st.title("Satisfaction level?")

st.subheader("The Dataset")

st.write(
  user_df
)

model = pickle.load(open("./models/pridict_satisfaction_model.sav", 'rb'))
#result = loaded_model.score(x_test, y_test)
#result
st.subheader("This model will predict user satisfaction")

eng = st.number_input("eng_score")
exp= st.number_input("exp_score")

input_data = [eng, exp]
prediction = model.predict([input_data])

st.subheader("The satisfaction score is: {}".format ( "prediction"))

st.subheader("Top 3 Handset Manufacturers")
image2 = Image.open('./image/top3.png')
st.image(image2, caption='Top 3 Handset Manufacturers')
