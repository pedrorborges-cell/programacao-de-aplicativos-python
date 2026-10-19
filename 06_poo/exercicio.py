# 1. Cachorro

class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: Au au!")

    def mostrar_info(self):
        print(f"Nome: {self.nome} | Raça: {self.raca} | Idade: {self.idade} anos")


cachorro1 = Cachorro("Rex", "Labrador", 3)
cachorro2 = Cachorro("Bob", "Rottweiler", 5)

cachorro1.latir()
cachorro1.mostrar_info()

cachorro2.latir()
cachorro2.mostrar_info()

cachorro1.idade = 4
cachorro1.mostrar_info()


# 2. Livro

print("\n------------------------------------------------------------------------------------------------------------")

class Livro:
    def __init__(self, titulo, autor, total_paginas, paginas_lidas = 0):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.paginas_lidas = paginas_lidas

    def ler(self, paginas):
        self.paginas_lidas = min(
            self.paginas_lidas + paginas, self.total_paginas
        )

    def porcentagem_lida(self):
        return (self.paginas_lidas / self.total_paginas) * 100

    def paginas_restantes(self):
        return self.total_paginas - self.paginas_lidas

    def terminou(self):
        return self.paginas_lidas == self.total_paginas


livro1 = Livro("Don Quixote", "Miguel de Cervantes", 1100,)
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96,)


for livro, sessoes in [(livro1, [64, 100, 92]), (livro2, [30, 40, 50])]:
   for paginas in sessoes:
       livro.ler(paginas)
       print(f"\nLivro: {livro.titulo}")
       print(f"Porcentagem lida: {livro.porcentagem_lida():.1f}%")
       print(f"Páginas restantes: {livro.paginas_restantes()}")
       print(f"Terminou: {livro.terminou()}")

print("\n------------------------------------------------------------------------------------------------------------\n")

# 3. Conta Bancária

class ContaBancaria:
   def __init__(self, titular, saldo=0):
       self.titular = titular
       self.saldo = saldo


   def depositar(self, valor):
       self.saldo += valor
       print(f"Novo saldo: R$ {self.saldo:.2f}")


   def sacar(self, valor):
       if valor <= self.saldo:
           self.saldo -= valor
           print(f"Saque realizado. Saldo: R$ {self.saldo:.2f}")
       else:
           print("Saldo insuficiente")

   def extrato(self):
       print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

conta1 = ContaBancaria("João")
conta2 = ContaBancaria("Maria", 500)

conta1.depositar(200)
conta1.sacar(50)
conta1.extrato()

conta2.depositar(100)
conta2.sacar(300)
conta2.sacar(400)
conta2.extrato()

# 4. Personagem de Videogam

class Personagem:
    def __init__(self, nome, classe, vida = 100, nivel = 1):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.nivel = nivel

    def receber_dano(self, valor):
        self.vida = max(0, self.vida - valor)
        if self.vida == 0:
            print(f"{self.nome} foi derrotado!")

    def curar(self, valor):
        self.vida = min(100, self.vida + valor)

    def subir_nivel(self):
        self.nivel += 1
        self.vida = 100

    def status(self):
        print(
            f"Nome: {self.nome} | Classe: {self.classe} | "
            f"Nível: {self.nivel} | Vida: {self.vida}"
        )

    personagem1 = Personagem("Arthur", "Guerreiro")
    personagem2 = Personagem("Merlin", "Mago")

    personagem1.receber_dano(40)
    personagem1.curar(20)
    personagem1.subir_nivel()

    personagem2.receber_dano(60)
    personagem2.receber_dano(50)

    print("\nStatus final:")
    personagem1.status()
    personagem2.status()

