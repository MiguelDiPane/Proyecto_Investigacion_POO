from claseAlumno import Alumno

class ManejadorAlumno:

    #Atributos
    __lista = []

    #Metodos
    def __init__(self):
        self.__lista = []

    #Carga un nuevo alumno en la lista
    def cargarAlumno(self,nom,ap,dni,reg):
        if type(nom) == str and type(ap) == str and type(dni) == str and type(reg) == str and reg.isdigit():
            miAlumno = Alumno(nom,ap,dni,int(reg))
            self.__lista.append(miAlumno)
  
    #Muestra todos los alumnos inscriptos en LCC
    def showAlumnos(self):
        print('{:20}{:15}{:15}{:10}'.format('Nombre','Apellido','DNI','Registro'))
        for alumno in self.__lista:
            nom = alumno.getNombre()
            ap = alumno.getApellido()
            dni = alumno.getDni()
            reg = alumno.getRegistro()
            print('{:20}{:15}{:10}{:10}'.format(nom,ap,dni,reg))           

    #Busco alumno segun numero de registro  
    def buscarAlumno(self,reg):
        if reg.isdigit():
            reg = int(reg)
            for indice, unAlumno in enumerate(self.__lista):
                registro = unAlumno.getRegistro()
                if reg >= registro:
                    break
            if reg != registro:     
                indice = None
        else:
            indice = None
        return indice
    
    #Busca alumno para agregar nuevo
    def buscarAlumnoIgualoAnterior(self, reg):
        for indice, unAlumno in enumerate(self.__lista):
            print(indice)
            if reg >= unAlumno.getRegistro():
                break
        return(indice)

    #Elimina un alumno segun indice encontrado       
    def eliminaAlumno(self,indice):
        if indice != None:
            nom = self.__lista[indice].getNombre()
            ap = self.__lista[indice].getApellido()
            print('Eliminar alumno: {} {}'.format(nom,ap))
            op = input('Confirme operacion [S]i - [N]o: ')
            if op.lower() == 's':
                self.__lista.pop(indice)
                print('Alumno eliminado')
            else:
                print('No se elimina el alumno')

    #Ordena a los alumnos en orden descendente por numero de registro. 
    def ordenarAlumnos(self):
        self.__lista.sort(reverse=True) #En orden descendente

    #Inserta un nuevo alumno en su posicion segun su numero de registro
    def insertAlumno(self, nom,ap,dni,reg):
        if type(nom) == str and type(ap) == str and type(dni) == str and type(reg) == str and reg.isdigit():
            if self.buscarAlumno(reg) == None:
                unAlumno = Alumno(nom,ap,dni,int(reg))        
                posicion = self.buscarAlumnoIgualoAnterior(int(reg))
                if posicion < (len(self.__lista)-1):
                    self.__lista.insert(posicion, unAlumno)
                else: #El alumno debe agregarse al final
                    self.__lista.append(unAlumno)
                print("El alumno se inserto en la posicion {0}".format(posicion))
            else:
                print('El numero de registro ya se encuentra registrado en el archivo.')
        else:
            print('Error: Tipo de datos incorrecto.')

    #Muestra el total de inscriptos a la carrera LCC
    def totalInscriptos(self):
        total = len(self.__lista)
        print('Actualmente hay {} alumnos en LCC'.format(total))