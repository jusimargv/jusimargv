class Veiculo:
    
    def __init__(self, cor, nome, fabricante, modelo, placa, numero_rodas):
        
        self.cor =cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        self.nome = nome
        self.fabricante =fabricante
        self.modelo = modelo
    
 
 
    def __str__(self):
         return f"{self.__class__.__name__}: {', '.join ([f'{chave} = {valor}' for chave,valor in self.__dict__.items()])}"    

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    
    pass

class Caminhao(Veiculo):
 
    pass
    
moto = Motocicleta("azul","CG-Titan","Yamaha","CG-150","JAS0I35",2)
 
carro = Carro("Cinza","Camry","Toyota","HXL","MGW-9985",4)


caminhao = Caminhao("vermelha","D-600","Wolkswagen","D-1620","DFG-5263",8)


print(carro)
print(caminhao)
print(moto)

    