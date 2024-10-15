import streamlit as st
from bhaskara import Bhaskara

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
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")

# To run the app, you would call:
if __name__ == "__main__":
    BhaskaraUI.main()
