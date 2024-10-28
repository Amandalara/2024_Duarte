import streamlit as st
from views import view
import panda as pd

class ManterClienteUI:
    def main():
        st.header("Costumer registration")
        tab1, tab2, tab3, tab4 = st.tabs(["List"]["Insert"]["Update"]["Delete"])