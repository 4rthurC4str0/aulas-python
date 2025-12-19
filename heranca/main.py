from funcionarios import Desenvolvedor

from abc import ABC

class Sistema(ABC):
    
    def cadastrar_funcionario(self, nome, salario_base, cargo):
        return Desenvolvedor(nome, salario_base, cargo)
    
    def remover_funcionario(self, nome): ...
    
    def bonus_salario(self): ...
    
    def mostrarFuncionarios(self): ...



if __name__ == '__main__':
    
    while(True):
        nome = input("Digite o nome do funcionário")
    
    sistema = Sistema()
    nome = 'arthur'
    cargo = 'pleno'
    salario_base = 1000
    cliente1 = sistema.cadastrar_funcionario(nome, salario_base, cargo)
    

    print(cliente1)