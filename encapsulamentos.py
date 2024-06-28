class conta:
    def __init__(self, saldo, nro_agencia):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
        
    def depositar(self, valor):
        #...
        
       self._saldo +=valor
    
    
    def sacar(self, valor):
        #...
        self._saldo -= valor
    
    
conta = conta("00001", 100)  
conta.depositar(input(" : "))
  
print(conta.nro_agencia)
print(conta.mostrar_saldo)