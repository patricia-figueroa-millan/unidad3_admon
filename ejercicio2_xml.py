import xml.etree.ElementTree as ET

def main():
    # Crear el elemento raíz
    estudiantes = ET.Element('estudiantes')
    
    # Pedir datos de estudiantes y agregarlos como subelementos de la raíz
    while True:
        print("Ingresar registro s o S para salir, para ingresar presione cualquier tecla: ")
        dato = input()
        if dato == 's' or dato == "S":
            break
        else:
            estudiante = ET.SubElement(estudiantes, 'estudiante')
            print("Ingrese el nombre del estudiante: ")
            nombre = input()
            ET.SubElement(estudiante, 'Nombre').text = nombre
            print("Ingrese el apellido paterno: ")
            apellidoP = input()
            ET.SubElement(estudiante, 'ApellidoPaterno').text = apellidoP
            print("Ingrese el apellido materno: ")
            apellidoM = input()
            ET.SubElement(estudiante, 'ApellidoMaterno').text = apellidoM
            print("Ingrese el número de control: ")
            noControl = input()
            ET.SubElement(estudiante, 'NoControl').text = noControl
            print("Ingrese el CURP: ")
            curp = input()
            ET.SubElement(estudiante, 'CURP').text = curp
            print("Ingrese el correo electrónico: ")
            correo = input()
            ET.SubElement(estudiante, 'Correo').text = correo
            print("Registro escrito con exito!")
    
    # Crear el árbol y escribirlo en un archivo XML
    tree = ET.ElementTree(estudiantes)
    tree.write('estudiantes.xml', encoding='utf-8', xml_declaration=True)
    print("Archivo creado con éxito")

if __name__ == "__main__":
    main()

