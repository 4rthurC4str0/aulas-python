from bonus import Calcular_bonus_mixin

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        self._nome = nome
        self._salario_base = salario_base
    
    @abstractmethod
    def calcular_bonus_salario(self): ...
    
    
    @property
    def cargo(self): ...
    
    @cargo.setter
    @abstractmethod
    def cargo(self, cargo): ...
    
        
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario_base, cargo):
        super().__init__(nome, salario_base)
        self.obj_bonus = Calcular_bonus_mixin()
        self._salario_bonificado = "Sem bonus"
        self.cargo = cargo
    
    @Funcionario.cargo.getter
    def cargo(self):
        if not self._cargo:
            raise AttributeError("Você não cadastrou um cargo!")
        
        return self._cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo
        
    def calcular_bonus_salario(self):
        self.bonus = self.obj_bonus.calcular_bonus(self.cargo, self._salario_base)
        if  not self.bonus:
            pass
        else:
            self._salario_bonificado = self._salario_base + self.bonus
        
    
    def __str__(self):
        return f'Nome: {self._nome} | Salario base: {self._salario_base} | Cargo: {self._cargo} | Salario bonificado: {self._salario_bonificado} '
        
class Gerente(Funcionario):
    def __init__(self, nome, salario_base, cargo, numero_de_funcionarios):
        super().__init__(nome, salario_base)
        self._numero_de_funcionarios = numero_de_funcionarios
        self.obj_bonus = Calcular_bonus_mixin()
        self.cargo = cargo

        
    @Funcionario.cargo.getter
    def cargo(self):
        return self._cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo
        
    def calcular_bonus_salario(self):
        self.bonus = self.obj_bonus.calcular_bonus(self.cargo, self._salario_base)
        if  not self.bonus:
            pass
        else:
            self._salario_bonificado = self._salario_base + self.bonus
        
    def __str__(self):
        return f'Nome: {self._nome}  | Salario base: {self._salario_base} | Cargo: {self.cargo} | Salario bonificado: {self._salario_bonificado} | Numero de Funcionários: {self._numero_de_funcionarios} '
            

if __name__ == '__main__':
 
    obj1 = Desenvolvedor('arthur', 1000, 'jr')
    obj1.cargo = 'senior'
    obj1.calcular_bonus_salario()
    print(obj1._cargo)
    print(obj1)