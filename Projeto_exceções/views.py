from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from datetime import datetime, timedelta

class View:
    
    def cliente_admin():
        for c in View.cliente_listar():
            if c.email == "admin": 
                return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    def cliente_inserir(nome, email, fone, senha):
        # Verificar se o e-mail já existe
        for c in View.cliente_listar():
            if c.email == email:
                raise ValueError("Este e-mail já está cadastrado.")
        
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)

    def cliente_listar():
        return Clientes.listar()

    def cliente_listar_id(id):
        return Clientes.listar_id(id)

    def cliente_atualizar(id, nome, email, fone, senha):
        # Verificar se o e-mail já existe em outro cliente
        for c in View.cliente_listar():
            if c.email == email and c.id != id:
                raise ValueError("Este e-mail já está cadastrado.")

        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)

    def cliente_excluir(id):
        c = Clientes.listar_id(id)
        if not c:
            raise ValueError("Cliente não encontrado.")
        
        for h in Horarios.listar():
            if h.id_cliente == id:
                raise ValueError("Não é possível excluir um cliente com horário agendado.")

        Clientes.excluir(c)

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id": c.id, "nome": c.nome}
        return None

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        # Verificar se o id_cliente e id_servico são válidos
        cliente = Clientes.listar_id(id_cliente)
        servico = Servicos.listar_id(id_servico)
        
        if not cliente:
            raise ValueError("Cliente inválido.")
        if not servico:
            raise ValueError("Serviço inválido.")
        
        c = Horario(0, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.inserir(c)

    def horario_listar():
        return Horarios.listar()

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.data >= datetime.now() and h.id_cliente is None:
                disponiveis.append(h)
        return disponiveis

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        # Verificar se o id_cliente e id_servico são válidos
        cliente = Clientes.listar_id(id_cliente)
        servico = Servicos.listar_id(id_servico)
        
        if not cliente:
            raise ValueError("Cliente inválido.")
        if not servico:
            raise ValueError("Serviço inválido.")
        
        c = Horario(id, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.atualizar(c)

    def horario_excluir(id):
        c = Horarios.listar_id(id)
        if not c:
            raise ValueError("Horário não encontrado.")
        
        if c.id_cliente is not None:
            raise ValueError("Não é possível excluir um horário com cliente agendado.")

        Horarios.excluir(c)

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        # Validar data, hora de início, hora de fim e intervalo
        try:
            di = datetime.strptime(data + " " + hora_inicio, "%d/%m/%Y %H:%M")
            df = datetime.strptime(data + " " + hora_fim, "%d/%m/%Y %H:%M")
        except ValueError:
            raise ValueError("Formato de data ou hora inválido.")

        if di >= df:
            raise ValueError("A hora de início deve ser antes da hora de fim.")
        
        if intervalo <= 0:
            raise ValueError("O intervalo deve ser maior que zero.")
        
        d = timedelta(minutes=intervalo)
        x = di
        while x <= df:
            View.horario_inserir(x, False, None, None)
            x = x + d

    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()

    def servico_listar_id(id):
        return Servicos.listar_id(id)

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        c = Servicos.listar_id(id)
        if not c:
            raise ValueError("Serviço não encontrado.")
        
        for h in Horarios.listar():
            if h.id_servico == id:
                raise ValueError("Não é possível excluir um serviço que tenha horários agendados.")

        Servicos.excluir(c)
