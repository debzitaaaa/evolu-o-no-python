'''Olá :) Depois de tanto tempo voltei aqui com mais um código incrível da minha evolução! Aprendi conceitos muito legais da POO com o professor Michel, e quis compartilhar 
esse código que fiquei muito orgulhosa de mim mesma por fazer e entender!'''

'''Explore o conceito de encapsulamento criando uma conta bancária e tentando acessar/modificar o saldo diretamente e através de métodos.'''

class ContaBancária:
    def __init__(self, titular, saldo_inicial): #comecei inicializando os atributos da classe
        self.titular = titular #atribui titular na memória
        self.__saldo = saldo_inicial #deixei o py renomear o atributo internamente, dificultando o acesso direto fora da classe
    
    def get__saldo(self): #estou puxando o saldo
        return self.__saldo
    
    def set_depositar(self, valor): #método setter para realizar o depósito 
        if valor > 0: #se o valor for maior que zero
            self.__saldo += valor #eu realizo o depósito
            return f"Saldo atual com o deposito: {self.__saldo}" 
        else: #mas se não
            return f"Não é possível realizar o depósito." #eu não realizo os depósitos 
        
    def set_sacar(self,valor): #aqui estou fazendo outro método setter, mas agora pra realizar o saque 
        if valor > 0 and self.__saldo >= valor: #aqui estou dizendo que, se o valor for maior que 0 e o saldo ser maior ou igual o valor
            self.__saldo -= valor #eu realizo o saque 
            return f"Valor atual com o saque: {self.__saldo}"
        elif valor <=0: #mas se o valor do saque for negativo 
            return f"Saque inválido." #eu digo que o saque é inválido
        else: #mas se o seu saldo não for nenhum desses anterirores
            return f"Saldo insuficiente." #eu digo que ele é insuficiente 
        
criando_minha_conta = ContaBancária("Débora", 5000) #aqui estou criando o meu objeto
depositando = 3000 
sacando = 8000
print(criando_minha_conta.set_depositar(depositando)) #teste depósito
print(criando_minha_conta.set_sacar(sacando)) #teste saque 
