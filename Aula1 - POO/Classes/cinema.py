class SessaoCinema:
    def __init__(self, dia, horario):
        self.dia = dia
        self.horario = horario

    def calcular_valor_inteira(self):
        valor_base = self._calcular_valor_base()
        if self._horario_em_acremente():
            return valor_base * 1.5
        else:
            return valor_base

    def calcular_valor_meia(self):
        return self.calcular_valor_inteira() / 2

    def _calcular_valor_base(self):
        if self.dia in ["segunda", "terca", "quinta"]:
            return 16
        elif self.dia == "quarta":
            return 8
        else:
            return 20

    def _horario_em_acremente(self):
        horario_numerico = int(self.horario.split(":")[0])
        return 17 <= horario_numerico <= 23
    
print(SessaoCinema('segunda',17).calcular_valor_inteira)
