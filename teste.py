import streamlit as st
import time
import plotly.express as px
from PIL import Image
import numpy as np
import pandas as pd
from matplotlib import pyplot as pyp
 
image = Image.open('1.png')
st.set_page_config(
    page_title="Site teste", 
    page_icon=image, 
    layout="centered", 
    initial_sidebar_state="collapsed", 
    menu_items={
         'Get Help': 'https://www.google.com',
         'Report a bug': "https://www.google.com",
         'About': """
         # Este é o site teste.
         """
     })

st.title('Web App de teste')

Var = st.slider('De 0 a 100, quanto você gosta do Hiroki',  min_value=0.01, max_value=0.5, step=0.001, value=0)
 
Var2 = [5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,10500,11000,11500,12000,12500,13000,13500,14000,14500,15000,15500,16000,16500,17000,17500,18000,18500,19000,19500,20000]
Var3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Var4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

a = 0

If a < 31
     Var3[a] = Var2[a]*Var
     a = a + 1
 
a = 0

If a < 31
     Var4[a] = Var2[a]-Var3[a]
     a = a + 1
  
fig = go.Figure()
fig.add_traces(go.Scatter(x=np.linspace(0, 2000, 20000),
                          y=Var2,
                          marker_color='royalblue',
                          line_width=3,
                          name='Valor original')
                )
fig.add_traces(go.Scatter(x=np.linspace(0, 2000, 20000),
                          y=Var3,
                          line_width=3,
                          marker_color='lightgrey',
                          name='Porcentagem')
                )
fig.add_traces(go.Scatter(x=np.linspace(0, 2000, 20000),
                          y=Var4,
                          line_width=3,
                          marker_color='grey',
                          name='Original menos porcentagem')
                )
fig.update_layout(plot_bgcolor='white',
                  legend=dict(x=0.02, y=0.9, 
                              orientation='h'),
                  xaxis=dict(tickfont_color='grey',
                             showline=True,
                             linewidth=1,
                             linecolor='lightgrey'),
                  yaxis=dict(tickfont_color='grey',
                             showline=True,
                             linewidth=1,
                             linecolor='lightgrey'),
)
 
st.subheader('2021年の株価推移の比較')
st.plotly_chart(fig)
