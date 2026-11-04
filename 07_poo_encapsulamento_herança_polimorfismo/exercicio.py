# 1. Personagens de um Jogo de RPG

# 1. Encapsulamento - proteger a vida para que ela só mude seguindo regras

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__vida = 100  # Privado: dois sublinhados

    def status(self):
        print(f"Sou {self.nome} e tenho {self.vida} de vida")

    @property
    def vida(self):
        return self.__vida

    def receber_dano(self, valor):
        if valor <= 0:
            print(f"Dano inválido para {self.nome}")
            return
        self.__vida = self.__vida - valor
        if self.__vida < 0:
            self.__vida = 0
        print(f"{self.nome} recebeu {valor} de dano")

    def curar(self, valor):
        if valor <= 0:
            print(f"Cura inválida para {self.nome}")
            return
        self.__vida = self.__vida + valor
        if self.__vida > 100:
            self.__vida = 100
        print(f"{self.nome} foi curado em {valor}")

    def atacar(self):
        return 10


p1 = Personagem("Aprendiz")
p1.status()

p1.receber_dano(30)
p1.status()

p1.receber_dano(-10)  # Dano negativo inválido

p1.curar(150)  # Tenta curar além do limite de 100
p1.status()

try:  # try/except é um bloco usado em programação para tratar erro
    p1.vida = 50
except AttributeError:
    print("Não é permitido alterar a vida diretamente.")

try:
    print(p1.__vida)
except AttributeError:
    print("O atributo __vida não pode ser acessado de fora.")


# 2. Herança

class Guerreiro(Personagem):
    def __init__(self, nome, forca):
        super().__init__(nome)  # super() chama construtor da classe mãe
        self.forca = forca  # atributo novo


class Mago(Personagem):
    def __init__(self, nome, mana):
        super().__init__(nome)
        self.mana = mana  # atributo novo

    def mostrar_mana(self):
        print(f"{self.nome} tem {self.mana} de mana")


guerreiro = Guerreiro("Thorin", 15)
mago = Mago("Gandalf", 50)

guerreiro.status()
mago.status()
mago.mostrar_mana()

# Teste com isinstance
print(f"Mago é um Personagem? {isinstance(mago, Personagem)}")


# 3. Polimorfismo - O mesmo método pode existir em várias classes, mas apresentar comportamentos diferentes
# dependendo do objeto que está executando esse método.

class Guerreiro(Personagem):
    def __init__(self, nome, forca):
        super().__init__(nome)
        self.forca = forca

    def atacar(self):
        return 10 + self.forca


class Mago(Personagem):
    def __init__(self, nome, mana):
        super().__init__(nome)
        self.mana = mana

    def mostrar_mana(self):
        print(f"{self.nome} tem {self.mana} de mana")

    def atacar(self):
        if self.mana >= 10:
            self.mana -= 10
            return 25
        else:
            print(f"{self.nome} está sem mana suficiente!")
            return 5


print("\n ===== POLIMORFISMO =====")

# Criando personagens de diferentes classes
grupo = [
    Personagem("Camponês"),
    Guerreiro("Guerreiro", 15),
    Mago("Mago", 20)
]

# Percorrendo a lista de personagens
for personagem in grupo:
    print(f"{personagem.nome} atacou e causou {personagem.atacar()} de dano!")

"""
1. Criamos uma lista chamada grupo com personagens de classes diferentes.
2. Utilizamos o for para percorrer todos os personagens.
3. Chamamos personagem.atacar() e cada classe executa seu próprio cálculo de dano.
"""


# Desafio Extra: Simulação de Batalha

print("\n ===== DESAFIO EXTRA: SIMULAÇÃO DE BATALHA =====")

monstro = Personagem("Monstro")
herois = [
    Guerreiro("Thorin", 15),
    Mago("Gandalf", 20)
]

rodada = 1
monstro.status()

while monstro.vida > 0:
    print(f"\n--- Rodada {rodada} ---")
    for heroi in herois:
        if monstro.vida > 0:
            dano = heroi.atacar()
            print(f"{heroi.nome} atacou o {monstro.nome}!")
            monstro.receber_dano(dano)
            monstro.status()
    rodada += 1

print(f"\nO {monstro.nome} foi derrotado!")