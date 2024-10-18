import streamlit as st
from bhaskara import Bhaskara
import pandas as pd

class BhaskaraUI:
    @staticmethod
    def main():
        st.header("Cálculo da equação do segundo grau")
        
        a = st.text_input("a")
        b = st.text_input("b")
        c = st.text_input("c")
        
        if st.button("Calcular"):
            try:
                a = float(a)
                b = float(b)
                c = float(c)
                r = Bhaskara(a, b, c)
                
                st.write(r)
                st.write(f'delta = {r.Delta()}') 
                
                if r.TemRaizesReais():
                    st.write(f'x1 = {r.raiz1()}')  
                    st.write(f'x2 = {r.raiz2()}') 
                else:
                    st.write("A equação não possui raízes reais.")
                    
            except ValueError:
                st.error("Por favor, insira valores numéricos válidos para a, b e c.")
    def grafico():
        st.header("Gráfico da equação do segundo grau")
        a = float(a)
        b = float(b)
        c = float(c)
        r = Bhaskara(a, b, c)
        st.write(r)
        xmin = (r.raiz1()) - 1
        xmax = (r.raiz2()) + 1
        n = 100
        d = (xmax - xmin)/n
        x = xmin
        px = []
        py = []
        while x < xmax:
            px.append(x)
            py.append(x**2 - r.b*x + r.c)
            x = x + d
        x = xmax
        px.append(x)
        py.append(x**2 - r.b*x + r.c) 
        dic = { "x" : px, "y" : py }
        chart_data = pd.DataFrame(dic)
        st.line_chart(chart_data, x = "x", y = "y")    


