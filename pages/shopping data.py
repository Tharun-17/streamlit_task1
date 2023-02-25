import streamlit as st
import plotly.express as px
import os
import pandas as pd

data = pd.read_csv('Customers.csv')

st.title('SHOPPING DASHBOARD')

st.subheader('Which age people are spending :green[more often?]')
fig_1 = px.histogram(data,x='Age',color='Gender')
st.plotly_chart(fig_1,use_container_width=True)

st.subheader('How can annual income differ with :red[profession and gender? ]')
Profession = st.selectbox('Select a profession: ',data['Profession'].unique())

fig_2 = px.bar(data[data['Profession']==Profession],x = 'Gender',y='Annual Income ($)',color='Annual Income ($)')
st.plotly_chart(fig_2,use_container_width=True)

st.subheader('Families of which size are spending more often?')
fig_3 = px.box(data, y='Family Size')
st.plotly_chart(fig_3,use_container_width=True)

st.subheader('How Annual Income, Spending score differs and family size are related ')
fig_4 = px.scatter(data,x='Annual Income ($)',y='Spending Score (1-100)',hover_data=['Gender'],color='Family Size')
st.plotly_chart(fig_4,use_container_width=True)