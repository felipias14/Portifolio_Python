import random
import string

# O usúario escolhe o tamnho da senha e quantidade de números e caracteres especiais
tamanho = int(input("Quantos caracteres terá a senha:  "))
quantidade_num = int(input("Quantos números: "))
quantidade_caracteres = int(input("Quantos caracteres especiais: "))

SENHA = ''

# faz as escolhas de numeros
for i in range(quantidade_num):
    SENHA += random.choice(string.digits)

# faz as escolhas de caracteres
for i in range(quantidade_caracteres):
    SENHA += random.choice(string.punctuation)

# faz escolha das letras
for i in range(tamanho-quantidade_num-quantidade_caracteres):
    SENHA += random.choice(string.ascii_letters)

# transformo minha senha que é uma string em uma lista para usar a funçao shuffle
SENHA_FORTE = list(SENHA)
random.shuffle(SENHA_FORTE)

# juntos todos os caracteres da lista na minha string SENHA
SENHA = ''.join(SENHA_FORTE)
print(SENHA)
