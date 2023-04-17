"""
Comandos:
    - Para rodar os testes: pytest ou pytest -v (verbose)
    - Para visualizar a cobertura dos testes: pytest --cov=<arquivo/pasta com o código> <pasta com os testes> --cov-report term-missing
        pytest --cov=calculdora test/ --cov-report term-missing
"""

# Fazer as 4 operações: soma, subtração, multiplicação e divisão

class Calculadora:

    def soma(x, y):
        return float(x) + float(y)

    def subtracao(x, y):
        return float(x) - float(y)
    
    def multiplicacao(x,y):
        return float(x) * float(y)
    
    def divisao(x,y):
        return float(x) / float(y)
