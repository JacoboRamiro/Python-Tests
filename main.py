def es_palindromo(palabra: str) -> bool:
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def suma(a: int, b: int) -> int:
    return a + b
