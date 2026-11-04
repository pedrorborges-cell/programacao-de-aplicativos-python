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

    def bonus(self):
        return self.salario * 0.10

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


# 2. Herança

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario) # super() chama construtor da classe mãe
        self.equipe = equipe # atributo novo

    def mostrar_equipe(self):
        print(f"{self.nome} gerencia {self.equipe} pessoas")

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__init__(nome, salario)
        self.curso = curso

fulano = Gerente("Fulano", 8000, 5)
caio = Estagiario("Caio", 1500, "Análise de Sistemas")

fulano.apresentar()
caio.apresentar()
caio.dar_aumento(5)
caio.apresentar()


# 3. Polimorfismo - O mesmo método pode existir em várias classes, mas apresentar comportamentos diferentes
# dependendo do objeto que está executando esse método.

class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)
        self.equipe = equipe

    def bonus(self):
        return self.salario * 0.20 + self.equipe * 100

class Estagiario(Funcionario):
    def __init__(self, nome, salario, curso):
        super().__Init__(nome, salario)
        self.curso = curso
    def bonus(self):
        return 200


print("\n ===== POLIMORFISMO =====")

# Criando funcionários de diferentes classes
equipe = [
    Funcionario("Ana", 3000),
    Gerente("Bruno", 8000, 5),
    Estagiario("Caio", 1500, "Análise de Sistemas")
]

# Percorrendo a lista funcionários
for funcionario in equipe:
    print(f"{funcionario.nome}: R$ {funcionario.bonus()} ")

"""
1. Criamos uma lista chamada equipe com funcionarios de classes diferentes.
2. Utilizamos o for para percorrer todos os funcionários.
3. Chamamos funcionario.bonus() e cada class executa seu próprio cálculo.
"""