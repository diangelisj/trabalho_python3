#path = (colocar o caminho)
class Servico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.servicos = []

    def cadastrar(self):
        nome = input("Nome do serviço: ")
        valor = input("Valor do serviço: ")
        self.servicos.append({"codigo": self.codigo, "nome": nome, "valor": valor})
        #altere o arquivo pelo caminho do arquivo no seu S.O
        with open("servicos.txt", "a") as arquivo:
            arquivo.write(f"{self.codigo};{nome};{valor}\n")
    
    def alterar(self, codigo, novo_valor):
        for servico in self.servicos:
            if servico["codigo"] == codigo:
                servico["valor"] = novo_valor
        with open("servicos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        with open("servicos.txt", "w") as arquivo:
            for linha in linhas:
                dados = linha.strip().split(";")
                if dados[0] == codigo:
                    arquivo.write(f"{codigo};{dados[1]};{novo_valor}\n")
                else:
                    arquivo.write(linha)

#para utilizar. lembre-se de manter ter o nome do arquivo com o mesmo nome da classe servico.py

                    servico = Servico("S001")
                    servico.cadastrar()
                    servico.alterar("S001", "R$ 50,00")



