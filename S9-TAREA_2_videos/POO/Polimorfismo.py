### Polimorfismo (poli => muchas / morfos: formas)

class Estudiante_P():

    def describir_P(self):
        print("Soy un buen estudiante.")


class Docente_P():

    def describir_P(self):
        print("Me dedico a enseñar cursos.")


class Trabajador_P():

    def describir_P(self):
        print("Trabajo dentro de una gran empresa.")


def describirPersona_P(persona):
    persona.describir_P()


#doc_1 = Trabajador_P()
#describirPersona_P(doc_1)