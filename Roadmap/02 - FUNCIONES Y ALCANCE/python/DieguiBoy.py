# ---------Funciones----------- # 

# simple

def wave():
    print("hello, world")
wave()

# Con parámetro

def wave_name(name):
    print(f"Hello, {name}")
wave_name("Robin")

# Con varios parámetros 
def wave_sev_par(name, adj):
    print(f"Hello, {name}, {adj}")
wave_sev_par("Robin", "chico maravilla")

# Con retorno

def wave_return():
    return "Your welcome \n"

print(wave_return())

# Función con parámetros predetermindados

def thanks_default(name = "Batman"):
    print(f"You're welcome, {name}\n")
thanks_default()
# Función dentro de función

def thanks():
    print ("Thanks Robin, you are the best")
    thanks_default()
thanks()

# ******Variables****** # 
# global, puede ser usada dentro o fuera de funciones
var_global = 21 
def my_age():
    print(f"I am {var_global} years old")
my_age()

# local, solo es válida dentro de la función donde fue creada 

def your_ages():
    var_local = 34
    print(f"You are {var_local} year old")
your_ages()

def both_var():
    try:
        print(f"I am {var_global}")
        print(f"he is {var_local}")
    except:
        print("Local variables can't be used outside of his function")
    finally:
        print("successful test") 

both_var()

# función del sistema len() cuenta los espacios en una cadena 

string = "Tonight is gonna be a good night"

print(f"the string has {len(string)} characters")


# ************ DIFICULTAD EXTRA **************#

def zip_zap(zip= "zip", zap= "zap"):
    num = 0
    for i in range(1, 101):
        
        if i % 3 ==0 and i % 5 == 0:
            i = zip +" "+ zap
        elif i % 3 == 0:
            i = zip
        elif i % 5 == 0:
            i = zap
        else:
            num += 1  
        print(i)
    print(f"Se han impreso un total de {num} números.")    

zip_zap()
