import streamlit as st
from bhaskara import Bhaskara

class bhaskaraUI:
    def main():
        st.header("Cálculo equação do segundo grau")
        a = st.text_input("a")
        b = st.text_input("b")
        c = st.text_input("c")
        if st.button("Calcular"):
            r = Bhaskara(float(a), float(b), float(c))
            st.write(r)
            st.write(f'delta = {r.Delta}')
            st.write(f'x1 = {r.raiz1}')
            st.write(f'x2 = {r.raiz2}')
