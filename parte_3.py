from vehiculos import Vehiculo, Automovil
import csv
import ast

class AutoParticular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        Automovil.__init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos
    
    def __str__(self):
        return "{" + ", ".join([f"'{key}': '{value}'" for key, value in self.__dict__.items()]) + "}"    
    
    def guardar_datos_csv(self, nombre_archivo):
        archivo = open(nombre_archivo, "a+", newline="")
        archivo_csv = csv.writer(archivo)
        datos = [self.__class__, self.__dict__]
        archivo_csv.writerow(datos)
        archivo.close()

    def leer_datos_csv(self, nombre_archivo):
        vehiculos = []
        archivo = open(nombre_archivo, "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            try:
                clase_str, atributos_str = vehiculo
                if clase_str == f"<class '{self.__class__.__module__}.{self.__class__.__name__}'>":
                    atributos = ast.literal_eval(atributos_str)
                    vehiculo = AutoParticular(**atributos)
                    vehiculos.append(vehiculo)
            except ValueError as e:
                print("Error al procesar datos:", e)
        archivo.close()
        return vehiculos
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        Vehiculo.__init__(self, marca, modelo, nro_ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return "{" + ", ".join([f"'{key}': '{value}'" for key, value in self.__dict__.items()]) + "}"    

    def guardar_datos_csv(self, nombre_archivo):
        archivo = open(nombre_archivo, "a+", newline="")
        archivo_csv = csv.writer(archivo)
        datos = [self.__class__, self.__dict__]
        archivo_csv.writerow(datos)
        archivo.close()

    def leer_datos_csv(self, nombre_archivo):
        vehiculos = []
        archivo = open(nombre_archivo, "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            try:
                clase_str, atributos_str = vehiculo
                if clase_str == f"<class '{self.__class__.__module__}.{self.__class__.__name__}'>":
                    atributos = ast.literal_eval(atributos_str)
                    vehiculo = Bicicleta(**atributos)
                    vehiculos.append(vehiculo)
            except ValueError as e:
                print("Error al procesar datos:", e)
        archivo.close()
        return vehiculos
    
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor):
        Bicicleta.__init__(self, marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return "{" + ", ".join([f"'{key}': '{value}'" for key, value in self.__dict__.items()]) + "}"    

    def guardar_datos_csv(self, nombre_archivo):
        archivo = open(nombre_archivo, "a+", newline="")
        archivo_csv = csv.writer(archivo)
        datos = [self.__class__, self.__dict__]
        archivo_csv.writerow(datos)
        archivo.close()

    def leer_datos_csv(self, nombre_archivo):
        vehiculos = []
        archivo = open(nombre_archivo, "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            try:
                clase_str, atributos_str = vehiculo
                if clase_str == f"<class '{self.__class__.__module__}.{self.__class__.__name__}'>":
                    atributos = ast.literal_eval(atributos_str)
                    vehiculo = Motocicleta(**atributos)
                    vehiculos.append(vehiculo)
            except ValueError as e:
                print("Error al procesar datos:", e)
        archivo.close()
        return vehiculos
    
class AutoCarga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        Automovil.__init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return "{" + ", ".join([f"'{key}': '{value}'" for key, value in self.__dict__.items()]) + "}"    

    def guardar_datos_csv(self, nombre_archivo):
        archivo = open(nombre_archivo, "a+", newline="")
        archivo_csv = csv.writer(archivo)
        datos = [self.__class__, self.__dict__]
        archivo_csv.writerow(datos)
        archivo.close()

    def leer_datos_csv(self, nombre_archivo):
        vehiculos = []
        archivo = open(nombre_archivo, "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            try:
                clase_str, atributos_str = vehiculo
                if clase_str == f"<class '{self.__class__.__module__}.{self.__class__.__name__}'>":
                    atributos = ast.literal_eval(atributos_str)
                    vehiculo = AutoCarga(**atributos)
                    vehiculos.append(vehiculo)
            except ValueError as e:
                print("Error al procesar datos:", e)
        archivo.close()
        return vehiculos

print('Lista de Vehiculos Particular')
particular = AutoParticular("Ford", "Fiesta", 4, 180, 500, 5)
particular.guardar_datos_csv("vehiculos.csv")
particulares = particular.leer_datos_csv("vehiculos.csv")
for particular in particulares:
    print(particular)

print('Lista de Vehiculos Carga')
carga = AutoCarga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
carga.guardar_datos_csv("vehiculos.csv")
cargas = carga.leer_datos_csv("vehiculos.csv")
for carga in cargas:
    print(carga)

print('Lista de Vehiculos Bicicleta')
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
bicicleta.guardar_datos_csv("vehiculos.csv")
bicicletas = bicicleta.leer_datos_csv("vehiculos.csv")
for bicicleta in bicicletas:
    print(bicicleta)


print('Lista de Vehiculos Motocicleta')
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
motocicleta.guardar_datos_csv("vehiculos.csv")
motocicletas = motocicleta.leer_datos_csv("vehiculos.csv")
for motocicleta in motocicletas:
    print(motocicleta)