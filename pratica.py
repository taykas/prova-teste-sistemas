import math

# QUESTAO 01
def classificar_produto(valor):
    if valor < 50:
        return "Econômico"
    elif valor >= 50 and valor > 200:
        return "Intermediário"
    else:
        return "Premium"


# QUESTAO 02
def verificar_estoque(qtd):
    if qtd == 0:
        return "Sem Estoque"
    elif qtd >= 1 and qtd <= 10:
        return "Estoque Baixo"
    else:
        return "Estoque Normal"

# QUESTAO 03
def calcular_frete(peso):
    if peso < 1:
        return "R$15,00"
    elif peso > 1 and peso <= 5:
        return "R$30,00"
    else:
        return "R$50,00"
    
# QUESTAO 04
def conceito(nota):
    if nota >= 9 and nota <= 10:
        return "Conceito A"
    elif nota >= 7 and nota <= 7.9:
        return "Conceito B"
    elif nota >= 5 and nota <= 6.9:
        return "Conceito C"
    else:
        return "Conceito D"
    
# QUESTAO 05
def calcular_desconto(valor_compra):
    if valor_compra <= 100:
        return "Sem desconto"
    elif valor_compra > 100 and valor_compra <= 500:
        return round(valor_compra - (valor_compra * 0.10), 1)
    else:
        return round(valor_compra - (valor_compra * 0.20), 1)
    
# QUESTAO 06
def classificacao_filme(idade):
    if idade < 10:
        return "Livre" 
    elif idade >= 10 and idade <= 13:
        return "10 Anos"
    elif idade >= 14 and idade <=17:
        return "14 Anos"
    else:
        return "18 Anos"
    
# QUESTAO 07
def nivel_combustivel(percentual):
    if percentual <= 10:
        return "Reserva"
    elif percentual >= 11 and percentual <- 50:
        return "Médio"
    else:
        return "Cheio"
    
# QUESTAO 08:
def classe_ipv4(ip):
    octeto = ""

    for i in range(3):
        if ip[i] == ".":
            i-=1

        octeto += ip[i]

    octeto = int(octeto)

    if octeto >= 1 and octeto <= 126:
        return "Classe A"
    elif octeto >= 128 and octeto <= 191:
        return "Classe B"
    elif octeto >= 192 and octeto <= 223:
        return "Classe C"
    elif octeto >= 224 and octeto <= 239:
        return "Classe D"
    else:
        return "Classe E"
