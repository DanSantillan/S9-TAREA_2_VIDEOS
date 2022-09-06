class Persona():

    def __init__(self, apePat, apeMat, nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom

    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def datos(self):
        print(self.mostrarNombreCompleto())


class Estudiante(Persona):

    def __init__(self, apePat, apeMat, nom, pro):
        super().__init__(apePat, apeMat, nom)
        self.profesion = pro

    def datos(self):
        super().datos()
        print("Profesión: {0}".format(self.profesion))
"""
### Video 35
estu1 = Estudiante("Santillan", "Alfonso", "Daniel", "Ingeniería en Software")
print(estu1.mostrarNombreCompleto())
print(estu1.profesion)
"""

"""
### Video 36
estu1 = Estudiante("Santillan", "Alfonso", "Daniel", "Ingeniería en Software")
estu1.datos()

print(isinstance(per1, Estudiante))
"""

"""
### Video 37
per1 = Persona("Santillan", "Alfonso", "Daniel")
print(isinstance(per1, Estudiante))
"""
