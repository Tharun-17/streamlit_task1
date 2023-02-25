import streamlit as st
import plotly.express as px
import os
import pandas as pd

data = pd.read_csv('cereal.csv')

st.title('CEREALS DASHBOARD')

st.header(':orange[calories in different types of cereals]')
fig_1 = px.bar(data,x='name',y='calories')
st.plotly_chart(fig_1,use_container_width=True)

st.header(':red[calories box plot]')
fig_2 = px.box(data,y='calories')
st.plotly_chart(fig_2,use_container_width=True)

st.header('how different manufacturers are varying when it comes to :green[carbs vs sugar]')
mfr = st.selectbox('Select a manufacturer: ',data['mfr'].unique())
fig_3 = px.scatter(data[data['mfr']==mfr],x='carbo',y='sugars')
st.plotly_chart(fig_3,use_container_width=True)


