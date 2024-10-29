import streamlit as st
import pandas as pd  
import time
from views import View

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Customer Registration")
        tab1, tab2, tab3, tab4 = st.tabs(["List", "Insert", "Update", "Delete"])

        with tab1:
            ManterClienteUI.list()
        with tab2:
            ManterClienteUI.insert()
        with tab3:
            ManterClienteUI.update()
        with tab4:
            ManterClienteUI.delete()
        
    @staticmethod
    def list():
        clients = View.clients_list()
        if len(clients) == 0:
            st.write("No clients registered.")
        else:
            dic = [obj.__dict__ for obj in clients]
            df = pd.DataFrame(dic)
            st.dataframe(df)
            
    @staticmethod
    def insert():
        name = st.text_input("Enter your name:")
        email = st.text_input("Enter your email:")
        phone = st.text_input("Enter your phone:")
        if st.button("Insert"):
            View.clients_insert(name, email, phone)
            st.success("Client inserted!")
            time.sleep(2)
            st.experimental_rerun()

    @staticmethod
    def update():
        clients = View.clients_list()
        if len(clients) == 0:
            st.write("No clients registered.")
        else:
            op = st.selectbox("Select client to update", clients)
            name = st.text_input("Enter new name", op.name)
            email = st.text_input("Enter new email", op.email)  
            phone = st.text_input("Enter new phone", op.phone)  
            if st.button("Update"):
                View.clients_update(op.id, name, email, phone)  
                st.success("Client updated!")
                time.sleep(2)
                st.experimental_rerun()

    @staticmethod
    def delete():
        clients = View.clients_list()
        if len(clients) == 0:
            st.write("No clients registered.")
        else:
            op = st.selectbox("Select client to delete", clients)
            if st.button("Delete"):
                View.clients_delete(op.id)
                st.success("Client deleted successfully!")
                time.sleep(2)
                st.experimental_rerun()
