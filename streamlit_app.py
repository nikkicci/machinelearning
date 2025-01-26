import streamlit as st
import pandas as pd

st.title('🪄 Machine Learning App')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df
  st.write('**x**')
  x_raw = df.drop('species', axis=1)
  x_raw
  st.write('**y**')
  y_raw = df.species
  y_raw

with st.expander('Data visualization'):
    st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Data preparations
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9) # min value, max value, average value
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2) # min value, max value, average value
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0) # min value, max value, average value
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0) # min value, max value, average value
  gender = st.selectbox('Gender', ('male', 'female'))
  
  # Create a DataFrame for the input features
  data = {'island': island,
       'bill_length_mm': bill_length_mm,
       'bill_depth_mm': bill_depth_mm,
      'flipper_length_mm': flipper_length_mm,
      'body_mass_g': body_mass_g,
      'sex': gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, x_raw], axis=0)

# Encode x
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode) # convert each of the value in the column into a unique column-name, where the tick in the box means value 1 and no tick means the value 0. Combining the column-name with the column-value. 
input_row = df_penguins[:1] # first row only

# Encode y
target_mapper = {'Adelie': 0,
                'Chinstrap': 1,
                'Gentoo': 2}
def target_encode(val):
  return target_mapper[val]

with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**Combined penguins data**')
  input_penguins
  st.write('**Encoded input penguin**')
  input_row





