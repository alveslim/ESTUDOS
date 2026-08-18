from run import divisao, informacoes

def test_divisao():
    val = 8
    resp = divisao(val)
    print(resp)
    
    assert resp == val / 2 # assert e uma validacao em python
    assert isinstance(resp, float) # sentencas
    
def test_informacoes():
    resp = informacoes()
    assert isinstance(resp, dict)
    assert "name" in resp
    assert "Height" not in resp # sempre colocando instrucoes
    assert "Rafa" in resp["name"]

