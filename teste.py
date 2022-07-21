import streamlit as st
import time
from PIL import Image
 
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

Total = 0

text = st.text_input(
        label="Coloque o seu nome"
    )

escolha1 = st.selectbox('Você gosta do Hiroki?',('Sim','Não'))
if escolha1 == 'Sim':
    st.success('Que bom')
    Total = Total + 2
else:
    st.error('Estou triste')

escolha2 = st.selectbox("Quanto mais ou menos", ("Bastante", "Normal", "Mais ou menos", "Pouco", "Nada"))
if escolha2 == "Bastante":
    st.info("Então você deve gostar bastante do Hiroki")
    Total = Total + 16
elif escolha2 == "Normal":
    st.success("Tranquilo")
    Total = Total + 8
elif escolha2 == "Mais ou menos":
    st.success("Essa afirmativa me parece mais negativa")
    Total = Total + 4
elif escolha2 == "Pouco":
    st.warning("Que pena")
    Total = Total + 2
else:
    st.error("Talvez estou triste")
    Total = Total + 0

escolha3 = st.slider('De 0 a 100, quanto você gosta do Hiroki',  min_value=0, max_value=100, step=1, value=0)
if escolha3 <= 25:
    st.error("Você não deve gostar de mim")
elif escolha3 <=50 and escolha3 >25:
    st.warning("Você não deve gostar muito de mim")
elif escolha3 <= 75 and escolha3 > 50:
    st.success("Você deve gostar de mim razoavelmente")
elif escolha3 >75 and escolha3 <100:
    st.success("Você deve gostar bastante de mim")
else:
    st.info("Você deve me amar")
    
options = st.multiselect(
    'Coloque coisas que você gosta do Hiroki (Se não tiver, deixe em branco)',
    ['Rosto', 'Cabelo', 'Personalidade', 'Mãos','Voz', 'Olhos'],
    [])

with st.form("my_form", clear_on_submit=False):
    st.subheader('Preenche o formulário para enviar')
    name = st.text_input('Coloque seu nome')
    series = st.selectbox(label='Quanto tempo você conhece o Hiroki', options=["menos de um ano","dois anos","quase três anos"])
    description = st.text_area('Seu sentimento para/com Hiroki')
    submitted = st.form_submit_button("Enviar")
     
     
if submitted:
    with st.spinner("Enviando..."):
        time.sleep(3)
    st.success("Obrigado por envio, mas infelizmente esse é só um teste e não é enviado de verdade")