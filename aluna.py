#path = (colocar o caminho)
class Servico:
    def __init__(self, codigo):
        self.codigo = codigo
    def cadastrarServico(self):
        self.nome = input('Digite o nome do servico: ')
        self.valor = float(input('Digite o valor: '))
        with open("servicos.txt", 'a') as arquivo:
            arquivo.write(f'{self.codigo} - {self.nome} - {self.valor}' '\n')
    def alterarServico(self):
        self.codigo = int(input('digite o codigo: '))
        with open("servicos.txt", 'r') as arquivo:
            dados = arquivo.readlines()
        for registro in dados:
            linha = registro.split('-')
        if linha[0] == self.codigo:
            valornovo = float(input('Digite o novo valor do servico: '))
            linha[2] = valornovo