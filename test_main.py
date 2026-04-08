from main import es_palindromo, es_primo, suma

def test_es_palindromo():
    assert es_palindromo("ana") is True
    assert es_palindromo("radar") is True
    assert es_palindromo("python") is False

def test_es_primo():
    assert es_primo(2) is True
    assert es_primo(13) is True
    assert es_primo(4) is False
    assert es_primo(1) is False

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
