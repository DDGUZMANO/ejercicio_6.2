# En este segundo ejercicio, tendreis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Debereis de definir los métodos para inicializar sus atributos,imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def calificacion(self):
        print(f"El Alumno {self.nombre}, tiene una nota de {self.nota}.")
        
        if (self.nota) >=5:
            print ("Ha sido aprobado")
        else:
            print ("Ha sido reprobado")
            
class Alumno_actual(Alumno):
    pass

pedro = Alumno_actual("Pedro",3)
pedro.calificacion()

juan = Alumno_actual("Juan",6)
juan.calificacion()

maria = Alumno_actual("Maria",5)
maria.calificacion()

        
        
        

        