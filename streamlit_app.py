import streamlit as st
import pandas as pd

st.title('🪄 Machine Learning App')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
  st.write('**x**')
  x = df.drop('species', axis=1)
  x
  st.write('**y**')
  y = df.species
  y

with st.expander('Data visualization'):
    st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Data preparations
with st.sidebar:
  st.header('Input features')
