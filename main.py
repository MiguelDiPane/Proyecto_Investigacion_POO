import csv
from claseManejadorAlumno import ManejadorAlumno
from claseMenu import Menu

if __name__ == '__main__':
    #Lectura de archivo de alumnos
    nombreArch = 'misAlumnos.csv'
    print('Lectura de archivo: {}'.format(nombreArch))
    archivo = open(nombreArch)
    reader = csv.reader(archivo,delimiter=',')
    manejador = ManejadorAlumno()
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:     
            nombre = fila[0]
            apellido = fila[1]
            dni = fila[2]
            registro = fila[3]
            manejador.cargarAlumno(nombre,apellido,dni,registro)        
    archivo.close()

    #Ordeno el archivo antes de trabajar con el
    manejador.ordenarAlumnos()

    miMenu = Menu()
    miMenu.define_menu(['[1]- Agregar alumno','[2]- Eliminar alumno','[3]- Ver alumnos','[4]- Ver total inscriptos','[5]- Salir'])
    miMenu.showMenu()
    op = miMenu.selectOption()

    while op != 5:
        #Agregar alumno
        if op == 1:
            print('Nuevo alumno')
            nom = input('Nombre: ')
            ap = input('Apellido: ')
            dni = input('DNI: ')
            reg = input('Registro: ')
            manejador.insertAlumno(nom,ap,dni,reg)
            input('Presione ENTER para continuar...')
        #Eliminar alumno
        elif op == 2:
            reg = input('Ingrese numero de registro: ')
            pos = manejador.buscarAlumno(reg)
            manejador.eliminaAlumno(pos)
            input('Presione ENTER para continuar...')
        #Ver alumnos
        elif op == 3:
            manejador.showAlumnos()
            input('Presione ENTER para continuar...')
        #Ver total de inscriptos a LCC
        elif op == 4:
            manejador.totalInscriptos()
            input('Presione ENTER para continuar...')

        miMenu.showMenu()
        op = miMenu.selectOption()

