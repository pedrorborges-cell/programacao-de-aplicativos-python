# 1. Estruturas Condicionais

nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


# 2. Condionais e Operadores Lógicos
#and -> Todas as condições devem ser verdadeiras
#or -> Pelo menos uma condição deve ser verdadeira
#not -> inverte o resultado

idade  = 20
ingresso = True

if idade >= 18 and ingresso:
    print("Entrada permitida")
else:
    print("Entrada não permitida")


# 3. Estruturas de Repetição while

contador = 1

while contador <= 5:
    print(contador)
    contador += 1


# 4. Estrutura de Repetição for

for numero in range(1, 6):
    print(numero)

# 4,5. Percorrendo uma Lista
nomes = ["Ana", "Carlos", "João", "Maria"]

for nome in nomes:
    print(nome)


# 6. Break, Continue, Pass

for numero in range(1, 11):

    if numero == 6:
        break
        #continue
        #pass
    print(numero)


# 7. Percorrendo uma lista

for nome in nomes:
    print(nome)


# 8. Verificando se um elemento existe

if "João" in nomes:
    print("João está na lista")
else:
    print("João não está na lista")


# 9. Lista com diferentes tipos de dados

dados = ["João", 18, 1.75, True]
print(dados)


# 10. Lista de números
notas = [7.5, 8.0, 6.5, 9.0]
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media:.1f}")


# 11. Tuplas
#São semelhantes às listas, a principal diferença é que tuplas não podem ser alteradas depois de criadas.

coordenadas = (10, 20)
print(coordenadas)

# acessando elementos
print(coordenadas[0])
print(coordenadas[1])


# 12. Dicionários
# Armazenam informações no formato: (chave: valor)

aluno = {
    "nome": "Carlos",
    "idade": 20,
    "nota": 8.5
}
print(aluno)


# 13. Acessando valores do dicionário

print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])


# 14. Alterando valores

aluno["nota"] = 9.0
print(aluno)