class viagem():
    def __init__(self,distancia,tempo):
        self.distancia = distancia
        self.tempo = tempo
    def velocidade_media(self):
        return self.distancia / self.tempo
    
print(viagem(200,2.25).velocidade_media())
        