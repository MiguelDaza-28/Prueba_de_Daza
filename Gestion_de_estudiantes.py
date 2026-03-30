#Prueba de desempeño - Modulo 1 Python
#Sistema de Gestion de Estudiantes

def agregar_e():
   
   print("\n---Add new coder---\n")

   name = input("Enter a name: ") 
   age = int(input("Enter an age: ")) 
   id = int(input("Enter an ID: "))
   course = input("Enter a course: ")
   status = input("Active/Inactive: ")
   print("\n Student Added Successfully! \n")
   
   return {
        "name": name,
        "age": age,
        "id": id,
        "course": course,
        "status": status
    }

estudiantes = {
    1: {
        "id": 1048229292,
        "name": "Jander",
        "age": 23,
        "course": "Malecon",
        "status": "active",
        
    },
    2: {
        "id": 1048229296,
        "name": "Luisa",
        "age": 21,
        "course": "Malecon",
        "status": "inactive",
    },

    3: {
        "id": 1048229297,
        "name": "Maria",
        "age": 32,
        "course": "Malecon",
        "status": "active",
    }
}

print(estudiantes)


def consultar_e():
    print("---List of students---\n")
    return estudiantes


def buscar_e():
    print("--- Searching Student---\n")
    criterio = ""
    while criterio not in ["1", "2", "3", "4", "5",]:
        print("\nSearch by which criteria?: \n")
        print("1. Name\n")
        print("2. Age\n")
        print("3. ID\n")
        print("4. Course\n")
        print("5. Status\n")
        criterio = input("Select the criteria: \n")
    llaves = {"1": "name", "2": "age", "3": "id", "4": "course", "5": "status",}
    llave_a_buscar = llaves[criterio]

    valor_buscado = input(f"Enter the {llave_a_buscar} to search for: ")

    encontrado = False
    for est in estudiantes.values():
        if str(est[llave_a_buscar]).lower() == valor_buscado.lower():
            print(f"\nStudent found: {est}")
            encontrado = True
            break

    if not encontrado:
        print("\nNo student was found with that criteria.")



def actualizar_e():
    print("\n--- Update of Student data---\n")
    editar = int(input("\n Enter the student number for which you wish to edit information: "))

    if editar in estudiantes [1]:
        print("\nWhich criteria needs to be changed? : \n")
        print("1. Name\n")
        print("2. Age\n")
        print("3. ID\n")
        print("4. Course\n")
        print("5. Status\n")
        editar_criterio = input("Select the criteria: \n")
        
        if editar_criterio == "1":
            input("Write the new name: \n")
            int(input("Write the new age: \n"))
            int(input("Write the new id: \n"))
            input("Write the new course: \n")
            input("Write the new status (Active/Inactive): \n")
            return estudiantes
        
        elif editar_criterio == "2":
            input("Write the new name: \n")
            int(input("Write the new age: \n"))
            int(input("Write the new id: \n"))
            input("Write the new course: \n")
            input("Write the new status (Active/Inactive): \n")
            return estudiantes
        
        elif editar_criterio == "3":
            input("Write the new name: \n")
            int(input("Write the new age: \n"))
            int(input("Write the new id: \n"))
            input("Write the new course: \n")
            input("Write the new status (Active/Inactive): \n")
            return estudiantes


def borrar_e():
    print("\n--- Which Student needs to be deleted? ---\n")
    borrar = int(input("\n Enter the student number you need to delete: "))

    if borrar in estudiantes [1]:
        del estudiantes [1]
        return estudiantes

    elif borrar in estudiantes [2]:
        del estudiantes [2]
        return estudiantes

    elif borrar in estudiantes [3]:
        del estudiantes [3]
        return estudiantes
        
        
opcion = ""

while opcion not in ["1", "2", "3", "4", "5"]:
    print("\nStudent Database: \n")
    print("What would you like to do?\n")
    print("1. Register New Student\n")
    print("2. View student list\n")
    print("3. Search for a student by criteria\n")
    print("4. Update student information\n")
    print("5. Delete a student\n")
    opcion = input("Which action would you like to perform?: \n")
    
if opcion == "1":
    print(agregar_e())
    print(estudiantes)

elif opcion == "2":
    print(consultar_e())

elif opcion == "3":
    print(buscar_e())

elif opcion == "4":
    print(actualizar_e())
    print(estudiantes)

elif opcion == "5":
    print(borrar_e())
    print(estudiantes)