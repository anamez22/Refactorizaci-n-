class Empleado:
    def __init__(self, nombre, apellido, salario_base):
        self.nombre = nombre
        self.apellido = apellido
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario_base, bonus):
        super().__init__(nombre, apellido, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return super().calcular_salario() + self.bonus

class Vendedor(Empleado):
    def __init__(self, nombre, apellido, salario_base, comisiones):
        super().__init__(nombre, apellido, salario_base)
        self.comisiones = comisiones

    def calcular_salario(self):
        return super().calcular_salario() + self.comisiones