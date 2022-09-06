import os
#from modulos import funcionesMatematicas
from modulos.funcionesMatematicas import multiplicar, sumar
from Paquete1.funcionesCadenas import contarLetras
from Paquete1.funcionesNumericas import *
from POO.Persona import *
from POO.Curso import *
from POO.Cuenta import *
from POO.Herencia import *
from POO.HerenciaMultiple import *
from POO.Polimorfismo import *
from POO.RelacionesClases import *

print("Ingrese cero(0) para finalizar el programa...")

while True:
    menu_principal=input("Ingrese el número del video [1 - 40]: ")
    os.system("cls")
    
    if menu_principal=="1":
        print("""VIDEO 1:
Explicación del lenguaje PYTHON. Es multiparadigma, posee tipado dinámico.
Fue creado a finales de los años 80 por el científico holándes de la computanción Guido Van rossun.
""")
    
    elif menu_principal=="2":
        print("""VIDEO 2:
Instalación del Intérprete de Python y PyCharm IDE.
""")
    
    elif menu_principal=="3":
        print("""VIDEO 3:
Creación de Proyecto de Python.

Hola Mundo            
""")
    
    elif menu_principal=="4":
        print("""VIDEO 4:
Variables en Python
""")
        nombre="UskoKruM2010"
        print(nombre)
        
        edad=25
        print(edad)
        
        edad=True
        print(edad)
        
        sueldo=205.10
        print(sueldo)
    
    elif menu_principal=="5":
        print("""VIDEO 5:
Conversiones (Casting)              
""")
        numero1="35"
        numero2="18"
        print(numero1 + numero2)
        
        sueldo=1200.43
        sueldoEntero=int(sueldo)
        print(sueldoEntero)
        
        valor=1200.43
        valorDecimal=float(valor)
        print(valorDecimal * 3)
             
        edad=100
        print(len(str(edad)))
        
    elif menu_principal=="6":
        print("""VIDEO 6:
Números, Operaciones Matemáticas y Comentarios en Python              
""")
        entero=23
        decimal=31.78
        complejo=12+53
        booleano=True
        print(entero)
        print(decimal)
        print(complejo)
        print(booleano)
        
        num1=20
        num2=4
        print("\nSuma: ",(num1 + num2))
        print("Resta: ",(num1 - num2))
        print("Mulriplicación: ",(num1 * num2))
        print("División: ",(num1 / num2))
        print("División Exacta: ",(num1 // num2))
        print("Potencia: ",(num1 ** num2))        
        
    elif menu_principal=="7":
        print("""VIDEO 7:
Concatenación en Python              
""")
        texto1="Hola"
        texto2="Mundo"
        textoFinal= texto1 +" "+ texto2
        print(textoFinal)        
        print("El saludo es: %s %s" % (texto1,texto2))
        
        saludoFinal="Saludo: {0} {1}".format(texto1,texto2)
        print(saludoFinal)
        
        saludoFinal="Saludo: {x} {y}".format(x=texto1,y=texto2)
        print(saludoFinal)
    
    elif menu_principal=="8":
        print("""VIDEO 8:
Funciones de Cadenas (Strings) en Python              
""")
        texto="BienveNIdos al canal de UskoKruM2010"
        print(texto)
        print(texto.lower())
        print(texto.upper())
        print(texto.title()) ###convertir una cadena a un formato titulo
        print(texto.find("al")) ###Posición donde se encuentra la cadena o porción
        print(texto.count("e")) ### Cantidad de ocurrencias de una letra o porción
        
        textoFinal=texto.replace("e", "3")
        print(textoFinal)
        
        valor= texto.isnumeric() ### Arroja True o False dependiendo si es un número
        print(valor)
        
        cadenaSeparada= texto.split(" ") ###Separado mediante espacio
        print(cadenaSeparada)
        
    elif menu_principal=="9":
        print("""VIDEO 9:
Tuplas (Tuples) en Python
""")
        tupla=(1,2,3)
        print(tupla)
        tupla2=(7, "Daniel", True, 450.1, 16+7j, 15, "Felicidad", False)
        print(tupla2)
        tupla3=(9,3,(4,5,6))
        print(tupla3)
        print(tupla2[1])
        ###tupla2[1]="UskoKruM" ###Esto genera un error porque es inmutable
        print(tupla2[-1]) ### Permite acceder al último elemento
        print(tupla2[0:4])
        print(tupla2[-2])
        
        a,b,c=tupla
        print(a)
        print(b)
        print(c)
        
        tuplaFinal=tupla+tupla2
        print(tuplaFinal)
        
        print(tuplaFinal.count("21"))
        print(tuplaFinal.index(3))
        
    elif menu_principal=="10":
        print("""VIDEO 10:
Listas (List) en Python              
""")
        lista1=["Daniel", 25, 98.3, True, "Santillan", 56.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-1])
        
        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])
        
        lista1.append("UskoKruM2010")
        print(lista1)
        
        lista1.insert(4,"Ecuador")
        print(lista1)
        
        lista1.extend(["Alejando",110,False])
        print(lista1)
        
        print(lista1.index("Santillan")) ###donde esta "santillan"
        
        lista1.remove(56.3)
        print(lista1)
        
        lista1.pop() ### elimina el último elmento de la lista
        print(lista1)
        
        lista2=["Danny","Milagro"]
        lista3=lista1 + lista2
        print(lista3)
        
        print(lista2 * 4)
        
        print("UskoKruM2010" in lista1) ### Ver si un elemento esta dentro de la lista
        print("UskoKruM2010000" in lista1)
    
    elif menu_principal=="11":
        print("""VIDEO 11: 
Diccionarios en Python              
""")
        diccionario={"España":"Madrid","Perú":"Lima","Alemania":"Berlin"}
        print(diccionario["Perú"])
        print(diccionario)
        
        diccionario["Venezuela"]="Caracas"
        print(diccionario)
        
        diccionario["España"]="Barcelona"
        print(diccionario)
        
        del diccionario["España"]  ###del= eliminar
        print(diccionario)
        
        dic2={"Santillan":"Daniel",20:True, "Sueldo":150.80}
        print(dic2[20])
        
        llaves= ("España", "Francia", "Inglaterra")
        dicPais={llaves[0]:"Madrid", llaves[1]:"París", llaves[2]:"Londres"}
        print(dicPais)
        
        datosPersonales={"Apellido": "Santillan", "Anios":{1:2010,2:2011,3:2012,4:2013,5:2014}}
        print(datosPersonales)
        print(datosPersonales["Anios"])
        
        print(datosPersonales.get('apel',"Daniel"))
        
        print(datosPersonales.keys())
        valores=list(datosPersonales.values())
        print(valores)
                        
    elif menu_principal=="12":        
        print("""VIDEO 12:
Lectura de Datos por Teclado en Python              
""")
        nombre=input("Ingrese su nombre: ")
        edad=int(input("Ingrese su edad: "))
        sueldo=float(input("Ingrese su sueldo: "))
        
        print("Hola, " + nombre)
        print("Tu edad es: ", edad)
        
        edadFutura=edad + 20
        print("Tu edad (dentro de 20 años será): ", edadFutura)
        print("Tu sueldo es: ", sueldo)
        
    elif menu_principal=="13":        
        print("""VIDEO 13:
Estructura Condicional IF, ELSE, ELIF en Python              
""")
        edad=int(input("Ingrese su edad: "))
        if edad >18:
            print("Eres mayor de edad.")
        elif edad == 18:
            print("Tienes 18 años!")            
        else:
            print("No eres mayor de edad.")
            
    elif menu_principal=="14":        
        print("""VIDEO 14:
Funciones en Python
""")    
        def saludar():
            print("Santillan")
            print("Daniel")
            print("UskoKruM2010")
            return "Hola"
        print(saludar())      
        
        def evaluarSueldoMinimo(sueldo):
            if sueldo >=850:
                print("Cumples con el sueldo")
            else:
                print("Ganas menos que el sueldo mínimo")
        evaluarSueldoMinimo(850)
        evaluarSueldoMinimo(100)
                        
    elif menu_principal=="15":
        ###!     And          |         OR        |      Not        
        ###*  A   B  Salida   |   A   B  Salida   |    A   Salida       
        ###   v   v     v     |   v   v     v     |    v      f
        ###   v   f     f     |   v   f     v     |    f      v
        ###   f   v     f     |   f   v     v     |  
        ###   f   f     f     |   f   f     f     |  
        print("""VIDEO 15:
Operadores Lógicos (AND - OR - NOT) en Python
""")    
        distancia= 400
        numeroHermano= 3
        salarioPadres= 3000
        
        tieneBeneficio=False
        
        if (distancia > 1000 and numeroHermano >2) or salarioPadres < 2000:
            tieneBeneficio=True
        
        print(not(tieneBeneficio))
        
        if (5>3) and (8<6):
            print("Verdadero")
        else:
            print("Es mentira...")                    
        
    elif menu_principal=="16":        
        print("""VIDEO 16:
Operador Ternario en Python
""")
        sexos=("Hombre","Mujer")
        
        posicion=True
        sexo= sexos[posicion] ### [1] Mujer
        print(sexo)
        sexo= sexos[not posicion] ### [0] Hombre
        print(sexo)
            
    elif menu_principal=="17":        
        print("""VIDEO 17:
Función Range en Python
""")    
        numeros=range(5)  ### [0,1, 2, 3, 4,]        
        print(numeros[1])
        
        numeros1=range(4, 10) ### [4, 5, 6, 7, 8, 9] tupla    
        print(numeros1[5])
        
        numeros2=range(10, 100, 8) ### [10,18,26,34,42,50,56,66,74,82,90,98] tupla    
        print(numeros2[9])
                
    elif menu_principal=="18":        
        print("""VIDEO 18:
Bucle For en Python
""")    
        for num in range(0,20,2): ###( valor inicial, hasta el valor, de 2 en 2)
            print("Valor actual: {0}".format(num))
        
        for i in range(1,13):
            print("{0} x {1} es: {2}".format(i,i,(i*i)))
        
        for nom in ["Karen","Oscar","Daniel","Leonardo"]:
            print("Cantidad de letras de {0} es: {1}".format(nom,len(nom)))
            
    elif menu_principal=="19":        
        print("""VIDEO 19:
IF con Tuplas & Listas (IF - IN)
""")    
        print("--Cursos--")
        print("Matemática - Biología - Lenguaje - Ciencias")
        
        curso=input("Ingrese el curso deseado: ")
        print(curso)
        
        if curso in ("Matemática","Biología","Lenguaje","Ciencias"):
            print("Curso {0} seleccionado.".format(curso))
        else:    
            print("No Existe el curso...")
        
    elif menu_principal=="20":        
        print("""VIDEO 20:
Factorial de un número con Python
""")    
        numero=int(input("Ingrese un número: "))
        factorial=1
        for n in range(1,(numero+1)):
            factorial=factorial*n
        print("El factorial de {0} es: {1}".format(numero,factorial))
                
    elif menu_principal=="21":        
        print("""VIDEO 21:
Bucle While en Python
""")    
        indice=1        
        while indice<10: ### mientras
            print("Valor actual: {0}".format(indice))
            indice=indice+1
        print("Hemos terminado el bucle While\n")
        
        inicio=2
        while inicio <=100:
            print("Número par: {}".format(inicio))
            inicio+=2
        print("Hemos terminado el bucle While.")
        
    elif menu_principal=="22":        
        print("""VIDEO 22:
Sentencias Break, Continue, Pass en Python
""")    
        ###* Break: permite salir de un bucle cuando se cumple una condición
        for numero in range(1,6):
            if numero == 3:
                break
            print("El número es: {0}".format(numero))
        print("Bucle terminado.\n")
        
        ###* Continue: omite una parte del bucla cuando se cumple una condición y continúa con el resto
        for numero in range(1,6):
            if numero == 3:
                continue
            print("El número es: {0}".format(numero))
        print("Bucle terminado.\n")
        
        ###* pass: permite continuar con una sentencia o función que no tiene o aún no tiene un bloque de código útil.
        for numero in range(1,6):
            if numero <= 3:
                pass ### aqui no pasa nada y el blucle sigue trabajando
            else:
                print("El siguiente valor es mayor a 3: ")
            print("El número es: {0}".format(numero))
        print("Bucle terminado.")
    
    elif menu_principal=="23":        
        print("""VIDEO 23:
Generadores en Python ( Cláusula yield ) 
""")    
        ### Generadores: Permite Extraer valores de una función y almacenarlo
        ### (de uno en uno) en objetos iterables (que se pueden recorrer).
        ### sin la necesidad de almacenar TODAS A LA VEZ en la memoria RAM.
        def generaMultiplos7(limite):            
            numero=1
            listaNumeros=[]
            while numero<=limite:
                listaNumeros.append(numero*7) ###Para agregar un elemento
                numero=numero+1
            return listaNumeros ### Retornar toda la lista creada
        print(generaMultiplos7(10))
        
        def generaMultiplos7(limite):            
            numero=1           
            while numero<=limite:
                yield numero *7 ### ceder. la instrucción "yield" genera un objeto iterable.
                numero=numero+1        
        obtieneMultiplos7=generaMultiplos7(10)
        ### nect(): retorna el siguiente elemento de un objeto iterable
        print(next(obtieneMultiplos7))
        print("Acá hay 300 líneas de códigos...")
        print(next(obtieneMultiplos7))
        print("Acá hay 1000 líneas de códigos...")
        print(next(obtieneMultiplos7))
        ### son más eficientes ue las funciones traicionales
        ### muy útiles con listas de valores infinitos
        ### entre llamada y llamada, el objeto iterable entra en un estado de pausa(suspención)
                                
    elif menu_principal=="24":        
        print("""VIDEO 24:
Generadores en Python ( Cláusula yield from )
""")    
        ### Cuando indicamos un * adelante del parámetro de una función,
        ### estamos indicando que se va a recibir un número indeterminado
        ### de parámetros. Además, esos parámetros se recibirán en forma de tupla.
        
        # def devuelveLenguajes(*lenguajes):
        #     for leng in lenguajes:
        #         yield leng
                
        # def devuelveLenguajes(*lenguajes):
        #     for leng in lenguajes:
        #         for letra in leng:   ###for anidados
        #             yield letra
        ### hacen lo mismo ||
        
        def devuelveLenguajes(*lenguajes):
            for leng in lenguajes:
                yield from leng
                
        lenguajesObtenidos=devuelveLenguajes("Python","Java","PHP","Ruby","JavaScript")        
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        
    elif menu_principal=="25":        
        print("""VIDEO 25:
Excepciones en Python. Bloque TRY EXCEPT FINALLY
""")    
        ### Excepción: Error en tiempo de ejecución (durante la ejecución de un programa)        
        numero1= 20
        numero2= 0
        
        #print("La división de {0} entre {1} es: {2}".format(numero1,numero2,(numero1/numero2)))
        
        try:
            resultado=numero1/numero2
        #except:
        except ZeroDivisionError:
            print("No se puede dividir entre 0...")
        finally:  ### siempre aparece independientemente de si ocurre o no una excepción
            print("Yo siempre aparezco.")            
        print("Aquí termina el programa.")
        
    elif menu_principal=="26":        
        print("""VIDEO 26:
Sentencia RAISE (Lanzamiento de Excepciones)
""")    
        ### RAISE: Sirve para lanzar (DE forma intencional) excepciones en Python
        def evaluarNota(nota):
            if nota<0:
                raise ValueError("Valor incorrecto...")
                #raise ZeroDivisionError("No se permite valores negativos...")
            elif nota>=16:
                print("Excelente")
            elif nota>=11:
                print("Aprobado")
            else:
                print("Desaprobado")        
        #evaluarNota(-1)    
        evaluarNota(11)    
        print("Este es el fin de mi programa...")
        
    elif menu_principal=="27":        
        print("""VIDEO 27:
Módulos en Python. Importación de archivos externos
""")    
        
        ### Módulo:
        ### Es un archivo con extensión .py o .pyc (Python compilado), que posee su propio espacio de 
        ### nombres y que puede contener variables, funciones, clases o incluso otros módulos.
        ### ¿Para qué sirven?
        ### Para organizar mejor el código y poder reutilizarlo mejor.
        ### Modularizarción y reutilización.
            
        #print(funcionesMatematicas.sumar(5,6))
        #print(funcionesMatematicas.multiplicar(5,6))
        
        print(sumar(5,6))
        print(multiplicar(5,6))
        
    elif menu_principal=="28":        
        print("""VIDEO 28:
Paquetes de Python. Archivo __init__.py
""")    
        print(multiplicar(5,6))
        print(contarLetras("Daniel Santillan"))

    elif menu_principal=="29":        
        print("""VIDEO 29:
Programación Orientada a Objetos (POO) en Python: Clases y Objetos
""")
        persona1 = Persona_Des()
        persona1.apellidos = "Santillan Alfonso"
        print(persona1.apellidos)
        persona1.despertar_Per()
        print(persona1.despierta_Per)

        persona2 = Persona_Des()
        persona2.apellidos = "Paz Torres"
        print(persona2.apellidos)
        # persona2.despertar_Per()
        print(persona2.despierta_Per)
        
    elif menu_principal=="30":        
        print("""VIDEO 30:
Constructores de Clase en Python. Método __init__() para inicializar objetos
""")
        curso1 = Curso("Matemática", 5, "Ingeniería Civil")
        print(curso1.nombre)

        curso2 = Curso("Lenguaje", 4, "Ingeniería Industrial")
        print(curso2.nombre)

    elif menu_principal=="31":        
        print("""VIDEO 31:
Encapsulamiento de Variables de Clase en Python
""")
        curso1 = Curso("Matemática", 5, "Ingeniería Civil")
        print(curso1.nombre)
        curso1.mostrarDatos()

    elif menu_principal=="32":        
        print("""VIDEO 32:
Encapsulamiento de Métodos de Clase en Python
""")
        curso1 = Curso("Matemática", 5, "Ingeniería Civil")
        print(curso1.nombre)
        curso1.mostrarDatos()

    elif menu_principal=="33":        
        print("""VIDEO 33:
Métodos Accesores (GET - SET) En Python
""")
        cuenta1 = Cuenta("Oscar García", 15000, "Soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Dólares")
        print(cuenta1.get_Moneda())

    elif menu_principal=="34":        
        print("""VIDEO 34:
Método de Clase __str__ (Conversión a String)
""")
        curso1 = Curso("Matemática", 5, "Ingeniería Civil")
        print(curso1)
        curso1.mostrarDatos()

    elif menu_principal=="35":        
        print("""VIDEO 35:
Herencia en Python. Método super()
""")
        estu1 = Estudiante("Santillan", "Alfonso", "Daniel", "Ingeniería en Software")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)

    elif menu_principal=="36":        
        print("""VIDEO 36:
Sobreescritura de Métodos en Python: Uso de Método super()
""")
        estu1 = Estudiante("Santillan", "Alfonso", "Daniel", "Ingeniería en Software")
        estu1.datos()

    elif menu_principal=="37":        
        print("""VIDEO 37:
Principio de Sustitución entre Clases
""")
        per1 = Persona("Santillan", "Alfonso", "Daniel")
        print(isinstance(per1, Estudiante))
        
    elif menu_principal=="38":        
        print("""VIDEO 38:
Herencia MÚLTIPLE en Python | Programación Orientada a Objetos
""")
        cX1 = ClaseX(15, 21)

    elif menu_principal=="39":        
        print("""VIDEO 39:
Polimorfismo en Python | Programación Orientada a Objetos
""")
        doc_1 = Trabajador_P()
        describirPersona_P(doc_1)

    elif menu_principal=="40":        
        print("""VIDEO 40:
Relaciones entre Clases en Python (Dependencia entre Clases)
""")
        pais1 = Pais("Ecuador", "Guillermo Lasso")
        print(pais1)

        ciudad1 = Ciudad("Milagro", "17.64 millones", pais1)
        print(ciudad1)

        urba1 = Urbanizacion("María de los Angeles", ciudad1)
        print(urba1)

    elif menu_principal=="0":
        break    
    else:
        os.system("cls")        
        print("No existe ese video...")   

print("Gracias por usar el programa")
    
