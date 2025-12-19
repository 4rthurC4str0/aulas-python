
class Cargos():
    def __init__(self):
        self._cargos = {
            'jr': 0,
            'pleno': 20,
            'senior': 30,
        }
    
    def calcular_bonus(self, cargo, salario_base): ...
    
class Calcular_bonus_mixin(Cargos):
    
    def calcular_bonus(self, cargo, salario_base):
        self.__bonus_do_funcionario = None
        self.__porcentagem_bonus_do_funcionario = 0
        
        if cargo not in self._cargos.keys(): 
            raise KeyError("Digite um cargo válido -->> Esse cargo não existe na empresa <<--")
        
        self.__porcentagem_bonus_do_funcionario = self._cargos[cargo]

        self.__bonus_do_funcionario = salario_base * (self.__porcentagem_bonus_do_funcionario / 100)
            
        return self.__bonus_do_funcionario

