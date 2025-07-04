import streamlit as st
import pandas as pd
from PIL import Image

# Título da aplicação
st.title("🎉 Soltando Balões com Streamlit!")

# Botão de ação
if st.button("Clique aqui para soltar balões 🎈"):
    st.balloons()
