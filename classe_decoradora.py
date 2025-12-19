
# Classes decoradoras:
# São classes que decoram objetos
# @Decorador <- os decoradores que começam com letra maiuscula são Classes decoradoras

class Multiplicar:
    # aqui a classe recebe a função que foi decorada
    def __init__(self, func):
        self.func = func
        self.multiplicador = 10
    
    # o que vem aqui nos parametros de __call__ 
    # são os argumentos passados na chamada da função decorada
    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self.multiplicador

# aqui a classe Multiplicar recebe 1 argumento que é a função decorada 
# e ela recebe essa função no __init__
@Multiplicar
def soma(x, y):
    return x + y

# aqui os argumentos (2, 2) são passados para o __call__ 
# da classe que decorou a função
dois_mais_dois = soma(2, 2)

# esse print vai mostrar o que for retornado de __call__
# já que a soma(2, 2) chama o __call__, aquilo que é retornado para a variável dois_mais_dois
# é o retorno de __call__
print(dois_mais_dois)

#####################################################################################################
#
# Passando com parâmetros para a classe 
 
class Dividir:
    def __init__(self, divisor):
        self.divisor = divisor
        
    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado / self.divisor
        return interna
        
# se eu colocar assim eu estou executando o init da minha classe
# e o python executa por padrão o decorador então eu executo duas vezes
# ex: @Dividir()()
@Dividir(10)
def subtracao(x, y):
    return x - y

# @Dividir(10) -> vai executar o init e criar a call 
# logo após o Python vai executar por padrão o decorator, dessa forma -> @Dividir(10)() -> chamando o __call__
# será passado pára __call__ a função decorada subtracao
# e dentro de call será criada e retornada a função interna 
# e agora quando for chamado subtracao na verdade será a funcão interna e é por isso que a função interna recebe os argumentos
# obs: a segunda execução do decorator @Dividir(10)() chama o call porque a primeira execução torna subtracao uma instância da Classe Dividir subtracao = Dividir(10)
# assim quando a segunda execução é passada é como se estivesse executando um objeto callable, ou seja, chama o __call__ porque se tornou um callable
# ai a palavra subtracao recebe a função interna que depois executada.

quatro_menos_dois = subtracao(4, 2)

print(quatro_menos_dois)