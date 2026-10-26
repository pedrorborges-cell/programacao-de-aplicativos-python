# 1. Encapsulamento - proteger o salário para que ele só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #Privado: dois sublinhados

    def apresentar(self):
        print(f"Sou {self.nome} e ganho {self.salario:.2f}")

    @property
    def salario(self):
        return self.__salario

    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
            return
        self.__salario = self.__salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")


ana = Funcionario("Ana", 3000)
ana.apresentar()

ana.dar_aumento(10)
ana.apresentar()

try: #try/except é um bloco usado em programação para tratar erro
    ana.salario = 10000
except AttributeError:
    print("Não é permitido alterar o salário diretamente.")

try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salario não pode ser acessado de fora.")
