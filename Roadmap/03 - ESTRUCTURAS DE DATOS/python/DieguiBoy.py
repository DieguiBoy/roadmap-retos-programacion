from functools import partial

# --------- Estructuras de datos ---------- # 

# listas 
print("\n listas \n")
my_list = ["pera", "manzana", "banana", "melon"]
print(my_list)

my_list.append("cereza") # insersion
print(my_list)

my_list.remove("pera") # borrado
print(my_list)

print(my_list[2]) # acceso

my_list[1] = "platano" # update
print(my_list)

my_list.sort() # ordenacion
print(my_list)
#tipo 
print(type(my_list))


# tuplas
print("\n tuplas \n")
my_tuple = ("pera", "manzana", "banana", "melon") # las tuplas son elementos no modificables)
print(my_tuple[2]) # acceso
my_tuple = tuple(sorted(my_tuple)) # ordenacion (pasando a lista para ordernar, para posteriormente volver a tupla)
print(type(my_tuple))
print(my_tuple)

# sets 
print("\n Sets \n")
my_set = {"pera", "manzana", "banana", "melon"}
print(my_set)
my_set.add("guayaba") #insersion
print(my_set)
my_set.remove("pera") # borrado
print(my_set)
# los sets no permiten ordenacion

# diccionarios
print("\n diccionarios \n")
my_dict = {
    "name" : "Diego",
    "surname" : "Llanes",
    "age" : "21",
    "country" :"Mexico",
}
print(my_dict)
my_dict["city"] = "CDMX" # insersion
print(my_dict)
del my_dict["country"] # borrado
print(my_dict)
my_dict["age"] = "22"
print(my_dict)


# EXTRA 

def agenda_func():
    agenda = {"pepe":"4583804938"}
    options = {1:partial(select_contatc, agenda), 2:partial(add_contact, agenda),5: None ,3:partial(updated_contact, agenda),4:partial(delete_contact, agenda)}
    option = None
    while option != 5:
        option = int(input(f"****Agenda****\n " \
                    "Opciones\n" \
                    "Marque 1 para Seleccionar un contacto\n" \
                    "Marque 2 para agregar un nuevo contacto\n" \
                    "Marque 3 para actualizar un contacto existente\n" \
                    "Marque 4 para eliminar un contacto\n" \
                    "Marque 5 para salir de Agenda\n"  \
                    ">>>"))
        try:
            options[option]()
        except KeyError:
            print("error, try again")
        except TypeError:
            continue
        finally:
            print("Operacion exitosa")
    print("Agenda cerrada")

def add_contact(fuente):
    name = str(input("Nombre: "))
    number = input("Numero: ")
    while  len(number) > 11 or len(number) < 8:
        print("- Solo se permiten numeros\n" \
            "- Deber tener entre 8 o 11 digitos")
        number = input("Numero: ")
    fuente[name] = number
    print("contacto creado exitosamente")
    print("Contactos en Agenda")
    print(f"Contacto: {name} - {fuente[name]}")

def select_contatc(fuente:dict):
    print("Contactos en Agenda")
    print(", ".join(fuente.keys()))
    name  = input("Buscar: ")
    try:
        fuente[name]
    except KeyError:
        print("Contacto no encontrado")
    else:
        print(f"Contacto: {name} - {fuente[name]}")
    return name
def updated_contact(fuente:dict):
    print("Contactos en Agenda")
    print(", ".join(fuente.keys()))
    name  = input("Buscar: ")
    try:
        fuente[name]
    except KeyError:
        print("Contacto no encontrado")
    else:
        number = input("Introducir nuevo numero telefonico: ")
        while  len(number) > 11 or len(number) < 8:
            print("- Solo se permiten numeros\n" \
                "- Deber tener entre 8 o 11 digitos")
            number = input("Introducir nuevo numero telefonico: ")
        fuente[name] = number
        print("Actualizacion exitosa")
        print(f"Contacto: {name} - {fuente[name]}")



def delete_contact(fuente:dict):
    name = select_contatc(fuente)
    if name not in fuente:
        print("no se puede proseguir con la operacion")
        return False
    sure = input("Marque 1 para eliminar contacto: ")
    if sure == "1":
        del fuente[name]
        print("Eliminacion success")
        print("Contactos en Agenda")
        print(", ".join(fuente.keys()))
    else: 
        print("Error durante el proceso")

agenda_func()