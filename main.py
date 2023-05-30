import base64

import streamlit as st
from PIL import Image

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('fon.png')

st.title("⁠*⁠.⁠✧HaNd_MaDe_poli⁠*⁠.⁠✧")

genre = st.radio(
    "**сережки ручной работы**",
    ('арбузик', 'круглый лединец', 'сердечко лединец', 'металлические цветы', 'птички', 'чернушки', 'звездочки',
     'ракушка с жемчуженной', 'морковка', 'узелок', 'апельсинки', 'половинки апельсинок', 'листочек', 'месяц с звездочкой'))

if genre == 'арбузик':
    st.image(Image.open('watermelon.jpg'), "Делаю на заказ")
elif genre == 'чернушки':
    st.image(Image.open('chernushki.jpg'), "Делаю на заказ")
elif genre == 'круглый лединец':
    st.image(Image.open('ledine1.jpg'), "Делаю на заказ")
elif genre == 'сердечко лединец':
    st.image(Image.open('ledin2.jpg'), "Делаю на заказ")
elif genre == 'металлические цветы':
    st.image(Image.open('fla.jpg'), "Делаю на заказ")
elif genre == 'птички':
    st.image(Image.open('bird.jpg'), "Делаю на заказ")
elif genre == 'звездочки':
    st.image(Image.open('star.jpg'), "Делаю на заказ")
elif genre == 'ракушка с жемчуженной':
    st.image(Image.open('rak2.jpg'), "Делаю на заказ")
elif genre == 'морковка':
    st.image(Image.open('mor.jpg'), "Делаю на заказ")
elif genre == 'узелок':
    st.image(Image.open('j2.jpg'), "Делаю на заказ")
elif genre == 'апельсинки':
    st.image(Image.open('oreng.jpg'), "Делаю на заказ")
elif genre == 'половинки апельсинок':
    st.image(Image.open('or2.jpg'), "Делаю на заказ")
elif genre == 'листочек':
    st.image(Image.open('l1.jpg'), "Делаю на заказ")
elif genre == 'месяц с звездочкой':
    st.image(Image.open('v2.jpg'), "Делаю на заказ")

url = 'https://www.avito.ru/draft/744204787'

st.markdown(f'''
<a href={url}><button style="background-color:GreenYellow;">Приобрести можно тут</button></a>
''',
            unsafe_allow_html=True)