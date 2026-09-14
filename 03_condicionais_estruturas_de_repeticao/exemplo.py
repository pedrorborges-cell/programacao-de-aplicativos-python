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