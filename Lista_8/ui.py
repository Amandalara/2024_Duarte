import streamlit as st
from cliente import Cliente,Clientes
class UI:
    @classmethod
    def main(cls):
        st.header("Cadastro de Clientes")
        tab_listar, tab_inserir, tab_atualizar, tab_deletar = st.tabs(["Listar", "Inserir", "Atualizar", "Deletar"])

        with tab_inserir:
            cls.cliente_inserir()

        with tab_listar:
            cls.cliente_listar()

        with tab_atualizar:
            cls.cliente_atualizar()

        with tab_deletar:
            cls.cliente_excluir()
    @classmethod
    def cliente_inserir(cls):
        st.title("Inserir Cliente")
        with st.form("Inserir clientes"):
            nome = st.text_input("Nome")
            email = st.text_input("Email")
            fone = st.text_input("Telefone")
            enviar = st.form_submit_button("Inserir")

            if enviar:
                if nome and email and fone:
                    try:
                        novo_cliente = Cliente(0, nome, email, fone)
                        Clientes.inserir(novo_cliente)
                        st.success("Cliente inserido!")
                    except ValueError:
                        st.error("Dado inválido!")
                else:
                    st.warning("Todos os campos são obrigatórios.")

    @classmethod
    def cliente_listar(cls):
        st.title("Listar Clientes")
        clientes = Clientes.listar()
        for c in clientes:
            st.write(c)

    @classmethod
    def cliente_atualizar(cls):
        st.title("Atualizar Cliente")
        clientes = Clientes.listar()
        cliente_nomes = [c.get_nome() for c in clientes]

        selected_cliente_nome = st.selectbox("Selecionar Cliente", cliente_nomes)
        cliente = next((c for c in clientes if c.get_nome() == selected_cliente_nome), None)

        if cliente:
            novo_nome = st.text_input("Novo Nome", cliente.get_nome())
            novo_email = st.text_input("Novo Email", cliente.get_email())
            novo_fone = st.text_input("Novo Telefone", cliente.get_fone())
            enviar = st.button("Atualizar")

            if enviar:
                if novo_nome and novo_email and novo_fone:
                    try:
                        cliente_atualizado = Cliente(cliente.get_id(), novo_nome, novo_email, novo_fone)
                        Clientes.atualizar(cliente_atualizado)
                        st.success("Cliente atualizado!")
                    except ValueError:
                        st.error("Dado inválido!")

    @classmethod
    def cliente_excluir(cls):
        st.title("Deletar Cliente")
        clientes = Clientes.listar()
        cliente_nomes = [c.get_nome() for c in clientes]

        selected_cliente_nome = st.selectbox("Selecionar Cliente para Deletar", cliente_nomes)
        cliente = next((c for c in clientes if c.get_nome() == selected_cliente_nome), None)

        if cliente:
            if st.button("Deletar"):
                Clientes.excluir(cliente)
                st.success("Cliente excluído!")