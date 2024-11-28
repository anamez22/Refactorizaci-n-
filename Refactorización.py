#Refactorización 
class Empleado:
    def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario_base, bonus):
#   se agrego super(). _init_ para inicializar los atributos 
#   se agrego salario_base para que no haya repetición 
        super().__init__(nombre, apellido, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
# se agrego super().calcular_salario para que calcule correctamente antes de agregar los componentes 
        return super().calcular_salario() + self.bonus 


class Vendedor(Empleado):
    def __init__(self, nombre, apellido, salario_base, comisiones):
        super().__init__(nombre, apellido, salario_base)
        self.comisiones = comisiones

    def calcular_salario(self):
        return super().calcular_salario() + self.comisiones
