from pratica import classificar_produto, verificar_estoque, calcular_frete, conceito, calcular_desconto, classificacao_filme
from pratica import nivel_combustivel, classe_ipv4


# QUESTAO 01
def test_classificacao():
    assert classificar_produto(49) == "Econômico"

def test_classificacao():
    assert classificar_produto(100) == "Intermediário"
    
def test_classificacao():
    assert classificar_produto(500) == "Premium"
    
def test_classificacao():
    assert classificar_produto(51) == "Intermediário"
    
def test_classificacao():
    assert classificar_produto(201) == "Premium"

def test_classificacao():
    assert classificar_produto(1) == "Econômico"



# QUESTAO 02
def test_estoque():
    assert verificar_estoque(0) == "Sem Estoque"

def test_estoque():
    assert verificar_estoque(1) == "Estoque Baixo"
    
def test_estoque():
    assert verificar_estoque(10) == "Estoque Baixo"
    
def test_estoque():
    assert verificar_estoque(12) == "Estoque Normal"
    
def test_estoque():
    assert verificar_estoque(100) == "Estoque Normal"

def test_estoque():
    assert verificar_estoque(5) == "Estoque Baixo"



# QUESTAO 03
def test_frete():
    assert calcular_frete(0.5) == "R$15,00"

def test_frete():
    assert calcular_frete(1.4) == "R$30,00"
    
def test_frete():
    assert calcular_frete(10) == "R$50,00"
    
def test_frete():
    assert calcular_frete(1) == "R$30,00"
    
def test_frete():
    assert calcular_frete(11) == "R$50,00"

def test_frete():
    assert calcular_frete(0.1) == "R$15,00"


# QUESTAO 04
def test_conceito():
    assert conceito(9.5) == "Conceito A"

def test_conceito():
    assert conceito(8) == "Conceito B"
    
def test_conceito():
    assert conceito(7) == "Conceito C"
    
def test_conceito():
    assert conceito(4) == "Conceito D"
    
def test_conceito():
    assert conceito(10) == "Conceito A"

def test_conceito():
    assert conceito(7) == "Conceito B"


# QUESTAO 05
def test_desconto():
    assert calcular_desconto(50) == "Sem desconto"

def test_desconto():
    assert calcular_desconto(101) == 90.9 
    
def test_desconto():
    assert calcular_desconto(499) == 449.1
    
def test_desconto():
    assert calcular_desconto(501) == 450.9
    
def test_desconto():
    assert calcular_desconto(350) == 315

def test_desconto():
    assert calcular_desconto(3000) == 2400


# QUESTAO 06
def test_idade():
    assert classificacao_filme(9) == "Livre"

def test_idade():
    assert classificacao_filme(11) == "10 Anos"
    
def test_idade():
    assert classificacao_filme(14) == "14 Anos"
    
def test_idade():
    assert classificacao_filme(18) =="18 Anos"
    
def test_idade():
    assert classificacao_filme(15) == "14 Anos"

def test_idade():
    assert classificacao_filme(17) == "14 Anos"


# QUESTAO 07
def test_combustivel():
    assert nivel_combustivel(9) == "Reserva"

def test_combustivel():
    assert nivel_combustivel(11) == "Médio"
    
def test_combustivel():
    assert nivel_combustivel(51) == "Cheio"
    
def test_combustivel():
    assert nivel_combustivel(40) == "Médio"
    
def test_combustivel():
    assert nivel_combustivel(100) == "Cheio"

def test_combustivel():
    assert nivel_combustivel(10) == "Reserva"


# QUESTAO 08
def test_ipv4():
    assert classe_ipv4("10.0.0.1") == "Classe A"

def test_ipv4():
    assert classe_ipv4("172.16.0.1") == "Classe B"
    
def test_ipv4():
    assert classe_ipv4("192.168.1.1") == "Classe C"
    
def test_ipv4():
    assert classe_ipv4("230.1.1.1") == "Classe D"
    
def test_ipv4():
    assert classe_ipv4("250.1.1.1") == "Classe E"