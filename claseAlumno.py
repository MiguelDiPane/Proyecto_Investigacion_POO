class Alumno:
    #Atributos
    __nombre = ''
    __apellido = ''
    __dni = ''
    __reg = 0

    #Metodos
    def __init__(self,nom='',ap='',dni='',reg=0):
        self.__nombre = nom
        self.__apellido = ap
        self.__dni = dni
        self.__reg = reg

    def getNombre(self):
        return self.__nombre 
    def getApellido(self):
        return self.__apellido
    def getDni(self):
        return self.__dni
    def getRegistro(self):
        return self.__reg 

    def __gt__(self, otro):
        if type(otro) == Alumno:
            return (self.__reg > otro.getRegistro())
        elif type(otro) == int:
            return (self.__reg > otro)
        else:
            return None

    def __lt__(self, otro):
        if type(otro) == Alumno:
            return (self.__reg < otro.getRegistro())
        elif type(otro) == int:
            return (self.__reg < otro)
        else:
            return None    
    
    def __eq__(self, otro):
        if type(otro) == Alumno:
            return (self.__reg == otro.getRegistro())
        elif type(otro) == int:
            return (self.__reg == otro)
        else:
            return None

    def __ge__(self, otro):
        if type(otro) == Alumno:
            return (self.__reg >= otro.getRegistro())
        elif type(otro) == int:
            return (self.__reg >= otro)
        else:
            return None
    
    def __le__(self, otro):
        if type(otro) == Alumno:
            return (self.__reg <= otro.getRegistro())
        elif type(otro) == int:
            return (self.__reg <= otro)
        else:
            return None

    def __ne__(self, otro):
        if type(otro) == Alumno:
            return (self.__reg != otro.getRegistro())
        elif type(otro) == int:
            return (self.__reg != otro)
        else:
            return None