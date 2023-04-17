import xml.etree.ElementTree as ET

def main():
    print("Ejercicio 1: Creación y escritura de archivo XML")
    
    # crear el elemento raíz del archivo XML
    estudiantes = ET.Element("Estudiantes")
    
    # pedir los datos de cada estudiante y agregarlos al archivo XML
    while True:
        print("Ingresar registro s o S para salir, para ingresar presione cualquier tecla: ")
        dato = input()
        if dato == 's' or dato == "S":
            break
        else:
            # crear el elemento estudiante y agregar los datos como atributos
            estudiante = ET.SubElement(estudiantes, "Estudiante")
            print("Ingrese el nombre del estudiante: ")
            estudiante.set("Nombre", input())
            print("Ingrese el apellido paterno: ")
            estudiante.set("ApellidoPaterno", input())
            print("Ingrese el apellido materno: ")
            estudiante.set("ApellidoMaterno", input())
            print("Ingrese el número de control: ")
            estudiante.set("NoControl", input())
            print("Ingrese el CURP: ")
            estudiante.set("CURP", input())
            print("Ingrese el correo electrónico: ")
            estudiante.set("CorreoElectronico", input())
            print("Registro agregado con éxito!")
    
    # crear el objeto ElementTree y escribir el archivo XML
    arbol = ET.ElementTree(estudiantes)
    arbol.write("estudiantes.xml")

if __name__ == "__main__":
    main()
