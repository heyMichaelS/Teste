from codigo.calculadora import Calculadora
class TestCalculadora:
    
    def test_de_soma_de_dois_valores_positivos(self):
        # GIVEN
        numero_1 = 1
        numero_2 = 1
        valor_esperado = 2

        # WHEN
        valor_resultante = Calculadora.soma(numero_1, numero_2)
        
        # THEN
        assert valor_resultante == valor_esperado


    def test_de_subtracao_de_dois_valores_positivos(self):
        # GIVEN
        numero_1 = 1
        numero_2 = 1
        valor_esperado = 0

        # WHEN
        valor_resultante = Calculadora.subtracao(numero_1, numero_2)

        # THEN
        assert valor_resultante == valor_esperado

    def test_multiplicacao_de_dois_valores_positivo(self):
        # GIVEN
        numero_1 = 1.5
        numero_2 = 7.4
        valor_esperado = 11.1

        # WHEN
        valor_restante = Calculadora.multiplicacao(numero_1, numero_2)

        # THEN
        assert round(valor_restante, 2) == valor_esperado


    def test_divisao_de_dois_numeros_positivo(self):
        #GIVEN
        numero_1 = 2
        numero_2 = 0
        valor_esperado = 0

        #WHEN 
        valor_resultante = Calculadora.divisao(numero_1, numero_2)

        #THEN
        if numero_1 or numero_2 == 0:
            print("Zero não é dividivel")
        else:
            valor_resultante = Calculadora.divisao(numero_1, numero_2)


        assert valor_resultante == valor_esperado


