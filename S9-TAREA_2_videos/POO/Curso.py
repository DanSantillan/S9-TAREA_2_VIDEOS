class Curso():
    """
    nombre = "Matemática"
    creditos = 5
    profesion = "Ingeniería Civil"
    """

    ### Estado inicial del objeto:
    def __init__(self, nom, cre, pro):
        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"  ### Propiedad encapsulada.

    def mostrarDatos(self):
        dat = "Nombre: {0} / Créditos: {1} / Modo de impartición: {2}"
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docenteAsignado = self.__verificarDocente()

        ### Pertenece al video32
        if docenteAsignado:
            print("Existe docente asignado.")
        else:
            print("No es necesario asignar un docente...")

    def __verificarDocente(self):
        # print("Verificando si existe docente asignado...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False

    # toString()
    ### Video 34
    def __str__(self):
        texto = "Nombre: {0} - Créditos: {1}"
        return texto.format(self.nombre, self.creditos)

"""
###Video30
#curso1= Curso()
#print(curso1.nombre)

curso1 = Curso("Matemática", 5, "Ingeniería Civil")
print(curso1.nombre)

curso2 = Curso("Lenguaje", 4, "Ingeniería Industrial")
print(curso2.nombre)
"""

""""
###Video 31
curso1 = Curso("Matemática", 5, "Ingeniería Civil")
print(curso1.nombre)
curso1.mostrarDatos()
"""

"""
###Video 32
curso1 = Curso("Matemática", 5, "Ingeniería Civil")
print(curso1.nombre)
curso1.mostrarDatos()
"""

"""
###Video 34
curso1 = Curso("Matemática", 5, "Ingeniería Civil")
print(curso1.nombre)
curso1.mostrarDatos()
"""


