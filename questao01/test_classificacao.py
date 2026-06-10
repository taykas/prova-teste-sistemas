from classificacao import classificar_produto

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
    assert classificar_produto(0) == "Econômico"

