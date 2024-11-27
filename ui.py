import streamlit as st
from models.verifica import Verifica

class InicioUI:
    def main():
        st.header("Identificador de Mesma Rede")
        a = st.text_input("IP 1")
        b = st.text_input("IP 2")
        c = st.text_input("Máscara")
        if st.button("Verificar"):
            v = Verifica(a, b, c)
            st.write(v)