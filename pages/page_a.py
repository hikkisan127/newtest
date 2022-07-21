import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

image = Image.open('1.png')
st.set_page_config(
    page_title="Site teste", 
    page_icon=image, 
    layout="wide", 
    initial_sidebar_state="collapsed", 
    menu_items={
         'Get Help': 'https://www.google.com',
         'Report a bug': "https://www.google.com",
         'About': """
         # Este é o site teste.
         """
     })

st.title("Posso colocar algumas páginas aleatórias como esse")
st.header("A Isabela é muito linda")
st.subheader("Eu amo a Isabela")

def main():
    # ランダムな値でデータフレームを初期化する
    data = {
        'x': np.random.random(20),
        'y': np.random.random(20) - 0.5,
        'z': np.random.random(20) - 1.0,
    }
    df = pd.DataFrame(data)
    # 折れ線グラフ
    st.subheader('Line Chart')
    st.line_chart(df)
    # エリアチャート
    st.subheader('Area Chart')
    st.area_chart(df)
    # バーチャート
    st.subheader('Bar Chart')
    st.bar_chart(df)

btn = st.button(label='Ver gráfico')
if btn:
    with st.spinner("Carregando"):
        time.sleep(5)
    if __name__ == '__main__':
        main()