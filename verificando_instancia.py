class Persona:
    def __init__(self, nombre: str, apellido: str, anno: int):
        self.nombre = nombre
        self.apellido = apellido
        self.anno =  anno
        
class Departamento:
    def __init__(self, nombre_dpto: str, nombre_corto_dpto: str):
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto
        
        #Se establacen comisiones por departamento
        if self.nombre_corto_dpto == "IS":
            self.comision = 0.5
        elif self.nombre_corto_dpto == "TI":
            self.comision = 0.8
        elif self.nombre_corto_dpto == "MK":
            self.comision = 0.2
        else:
            self.comision = 0
        
class Trabajador(Persona, Departamento):
    def __init__(self, nombre: str, apellido: str, anno: int, nombre_dpto: str, nombre_corto_dpto: str, salario: int):
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self,nombre_dpto, nombre_corto_dpto)
        self.salario = salario
        
            
    def calculo_salario(self):
        """Metodo que calcula el salario de un trabajador incluyendo las comisiones
        generadas por departamento, si corresponde.
        """
        if self.comision>0:
            salario = self.salario +(self.salario * self.comision)
            return f"El salario del trabajador mas comisiones es de {salario}"
        else:
            return f"El salario del trabajador es de {self.salario}"
       
        
    def verificar_inst_clase(self):
        print(f"Es trabajador instancia de Persona: {isinstance(self, Persona)}")
        print(f"Es trabajador instancia de Departamento: {isinstance(self, Departamento)}")
        print(f"Es trabajador instancia de Trabajador: {isinstance(self, Trabajador)}")
        
#Se crea instancia de clase trabajador.
pepito = Trabajador("Juan", "Pérez", 2005, "Ingeniería de software", "IS", 20000)

#Se imprimen argumentos en un diccionario con metodo __dict__
print(pepito.__dict__)

#Se verifica cada instancia por clase a traves del metodo verificar_inst_clase() de la clase Trabajador
pepito.verificar_inst_clase()

#Se imprime el salario del trabajador calculado con el metodo calculo_salario() de la clase Trabajador
print(pepito.calculo_salario())