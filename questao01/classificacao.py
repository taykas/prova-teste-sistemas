def classificar_produto(valor):
    if valor > 50:
        return "Econômico"
    elif valor <= 50 and valor > 200:
        return "Intermediário"
    else:
        return "Premium"