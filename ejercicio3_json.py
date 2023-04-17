import json

def main():
    print("Ejercicio 3: Creación y escritura de archivo JSON")
    # crear una lista para almacenar los datos de los estudiantes
    estudiantes = []
    # pedir los datos de cada estudiante y agregarlos al diccionario
    while True:
        print("Ingresar registro s o S para salir, para ingresar presione cualquier tecla: ")
        dato = input()
        if dato == 's' or dato == "S":
            break
        else:
            print("Ingrese el nombre del estudiante:")
            campo_nombre = input()
            print("Ingrese el apellido paterno: ")
            campo_apellidoP = input()
            print("Ingrese el apellido materno: ")
            campo_apellidoM = input()
            print("Ingrese el número de control: ")
            campo_noControl = input()
            print("Ingrese el CURP: ")
            campo_CURP = input()
            print("Ingrese el correo electrónico: ")
            campo_correo = input()
                
            estudiante = {
                'Nombre': campo_nombre, 
                'Apellido Paterno': campo_apellidoP, 
                'Apellido Materno': campo_apellidoM, 
                'No. de Control': campo_noControl, 
                'CURP': campo_CURP, 
                'Correo electrónico': campo_correo
                }
            estudiantes.append(estudiante)
            print("Registro agregado con éxito!")

            # guardar los datos en un archivo JSON
            with open('estudiantes.json', 'w') as f:
                json.dump(estudiantes, f)
                print("Datos guardados en el archivo estudiantes.json")

if __name__ == "__main__":
    main()

    