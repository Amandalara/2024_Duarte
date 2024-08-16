from datetime import datetime
import enum


class boleto:
    def __init__(self,codBarras,dateEmissao,dataVencimento,datapagto,valorBoleto,valorPago,situacaoPagamento):
        self.__codBarras = codBarras
        self.__dateEmissao = dateEmissao
        self.__dataVencimento = dataVencimento
        self.__datapagto = datapagto
        self.__valorboleto = valorBoleto
        self.__valorpago = valorPago
        self.__situacaoPagamento = situacaoPagamento

        if self.__codBarras == '':
            raise ValueError("Código de barras inválido")
        
        if self.__dateEmissao > datetime.now():
            raise ValueError('Data de emissão inválida')

        if self.__dataVencimento < self.__dateEmissao :
            raise ValueError('Data de vencimento inválida')
        
        if self.__datapagto < self.__dateEmissao:
            raise ValueError("Data de pagamento inválida")
        
        if self.__valorboleto <= 0:
            raise ValueError('Valor inválido')
        
        if self.__valorpago <= 0:
            raise ValueError('Valor inválido')
        
        self.__situacaoPagamento = self.__situacaoPagamento
        


    def pagamento(self):
        return self.__valorboleto - self.__valorpago
    
    def situacao(self):
        if self.__valorpago == 0:
            self.__situacaoPagamento = pagamento.Emaberto
            print('Boleto em aberto')
        
        elif self.__valorpago < self.__valorboleto and self.__valorpago > 0:
            self.__situacaoPagamento= pagamento.PagoParcial
            print('Boleto parcialmento pago')
        
        elif self.__valorpago == self.__valorboleto:
            self.__situacaoPagamento = pagamento.Pago
            print('Boleto pago')
    
    # def __str__(self):
    #     return f'Código de barras ={self.__codBarras}, data de emissão ={datetime.strptime(self.__dateEmissao, '%d/%m/%Y')}, data de vencimento ={datetime.strftime(self.__dataVencimento,'%d/%m/%y')},data de pagamento ={datetime.strptime(self.__datapagto,'%d/%m/%Y')}, valor do boleto ={self.__valorboleto},valor pago ={self.__valorpago}'

        
class pagamento(enum.Enum):
    Emaberto = 1
    PagoParcial = 2
    Pago = 3


class UI:
    @staticmethod 

    def menu():
        print('1 - Gerar novo boleto,  2 - pagar boleto, 3 - sair  ')
        return int(input('Digite um número:'))

    def main():
        respo = 0
        while respo != 3:
            respo = UI.menu()
            if respo == 1:
                UI.gerar_boleto()
            if respo == 2:
                UI.pagar_boleto()
    
    def gerar_boleto():
        codBarras = input('Digite o código de barras:')
        dateEmissao = input('Digite a data de emissão do boleto(dd/mm/aa)')
        dateVencimento = input('Digite a data de vencimento do boleto(dd/mm/aa)')
        datepagto = input('Digite a data de pagamento do boleto(dd/mm/aa)')
        valorBoleto = float(input('Digite o valor do boleto:'))
        valorPago = float(input('Digite o valor a ser pago:'))
        situacaoPagamento = pagamento
        x = boleto(codBarras,datetime.strptime(dateEmissao, '%d/%m/%Y'),datetime.strptime(dateVencimento, '%d/%m/%Y'),datetime.strptime(datepagto, '%d/%m/%Y'),valorBoleto,valorPago,situacaoPagamento)
        print(x)


    def pagar_boleto(valorBoleto,valorPago):
        print('O valor do boleto é ',valorBoleto)
        print('O que foi pago = ',valorPago)
        x = boleto(valorBoleto,valorPago)
        s = boleto()
        print(s.pagamento())
        print(s.situacao())
        print(x)
        
UI.main()
