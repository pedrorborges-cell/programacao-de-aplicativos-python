# O que é uma função:
# Uma função é um bloco de código criado para realizar uma determinada tarefa.
# Ela permite organizar e reutilizar o código.

# 1. Criando uma Função
# Utilizar a palavra def para uma função

def saudacao():
    print("Olá, seja bem vindo!")

# Para executar a função, chamamos o seu nome

saudacao()


# 2. Função com Parâmetro

def saudacao(nome):
    print(f"\nOlá {nome}, seja bem vindo(a)!")

saudacao("Ana")
saudacao("Carlos")


# 3. Mais de um Parâmetro

def apresentar(nome, idade):
    print(f"\nNome: {nome}")
    print(f"Idade: {idade}")

apresentar("Maria", 17)


# 4. Função com Cálculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")

somar(10, 5)


# 5. Retornando um Valor
# O return devolve um valor parao local onde a função foi chamada.

def somar(numero1, numero2):
    return numero1 + numero2

resultado = somar(10, 5)
print(resultado)


# 6. Função com Condição

def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

resultado = verificarIdade(20)
print(resultado)


# 7. Parâmetro com Valor Padrão
# Podemos definir um valor padrão para um parâmetro.

def saudacao(nome = "Aluno"):
    print(f"\nOlá {nome}")

saudacao()
saudacao("João")


# 8. Vários Parâmetros

def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

print(calcularMedia(8, 7, 9))


# 9. Funções para Organizar o Programa

def cadastrarProduto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preco do produto: "))
    return nome, preco

def exibirProduto(nome, preco):
    print("\n === Produtos Cadastrados ===")
    print(f"Nome: {nome}")
    print(f"Preço: R$ {preco}")

nome , preco = cadastrarProduto()
exibirProduto(nome, preco)