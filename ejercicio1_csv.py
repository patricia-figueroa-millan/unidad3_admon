import csv

def main():
    print("Ejercicio 1: Creación y escritura de archivo CSV")
    # abrir el archivo CSV en modo de escritura
    with open('estudiantes.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        
        # escribir los nombres de las columnas
        writer.writerow(['Nombre', 'Apellido Paterno', 'Apellido Materno', 'No. de Control', 'CURP', 'Correo electrónico'])
        
        # pedir los datos de cada estudiante y escribirlos en una fila separada
        while True:
            print("Ingresar registro s o S para salir, para ingresar presione cualquier tecla: ")
            dato = input()
            if dato == 's' or dato == "S":
                break
            else:
                print("Ingrese el nombre del estudiante: ")
                campo_nombre = input()
                print("Ingrese el apellido paterno: ")
                campo_apellidoP = input()
                print("Ingrese el apellido materno: ")
                campor_apellidoM = input()
                print("Ingrese el número de control: ")
                campo_noControl = input()
                print("Ingrese el CURP: ")
                campo_CURP = input()
                print("Ingrese el correo electrónico: ")
                campo_correo = input()
                writer.writerow([campo_nombre, campo_apellidoP, campor_apellidoM, campo_noControl, campo_CURP, campo_correo])
                print("Registro escrito con exito!")

if __name__ == "__main__":
    main()



