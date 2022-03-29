import streamlit as st
import pandas as pd
import env
import functions

st.header('My Food Application')
col1, col2 = st.columns(2)
with col1:
    st.image(functions.get_food_image('Orange fruit'), width=300)

with col2:
    st.write('Aplicações de informações nutricionais \n obs: eu sei q ta um lixo')
