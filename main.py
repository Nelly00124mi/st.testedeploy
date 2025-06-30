import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config("Sistema de Vida das Células", layout="wide")

#Título
st.title("Carta Vegetal e Animal")

#Separação em colunas
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader("Envie uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True, caption="Imagem enviada")

with col2:
    st.subheader("❤️ Vida & ⚡ Energia")
    
    vida = st.slider("Vida", min_value=0, max_value=100, value=100, step=1)
    energia = st.slider("Energia", min_value=0, max_value=100, value=100, step=1)

    # Cor personalizada da energia conforme o valor
    def cor_energia(valor):
        if valor > 70:
            return "green"
        elif valor > 30:
            return "orange"
        else:
            return "red"

    # Exibição das barras
    st.markdown(f"**Vida: {vida}%**")
    st.progress(vida / 100)

    st.markdown(f"<span style='color:{cor_energia(energia)}'><strong>Energia: {energia}%</strong></span>", unsafe_allow_html=True)
    st.progress(energia / 100)
