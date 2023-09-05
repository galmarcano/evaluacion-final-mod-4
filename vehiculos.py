class Vehiculo():
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class AutoParticular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        Automovil.__init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Numero de ruedas: {self.nro_ruedas}, Velocidad: {self.velocidad} Km/h, Cilindrada: {self.cilindrada} cc, Numero de puestos: {self.nro_puestos}"

class AutoCarga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, peso_carga):
        Automovil.__init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.peso_carga = peso_carga

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Numero de ruedas: {self.nro_ruedas}, Velocidad: {self.velocidad} Km/h, Cilindrada: {self.cilindrada} cc, Peso de carga: {self.peso_carga}"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        Vehiculo.__init__(self, marca, modelo, nro_ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Numero de ruedas: {self.nro_ruedas}, Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, nro_radios, cuadro, motor):
        Bicicleta.__init__(self, marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, umero de ruedas: {self.nro_ruedas}, Tipo: {self.tipo}, Numero de radios: {self.nro_radios}, Cuadro: {self.cuadro}, Motor: {self.motor}"




def obtener_entero_valido(mensaje):
    while True:
        valor_str = input(mensaje)
        if valor_str.strip() and valor_str.isdigit() and int(valor_str) != 0:
            valor = int(valor_str)
            return valor
        else:
            print("Error: Ingrese un valor numérico entero válido.")

def obtener_flotante_valido(mensaje):
    while True:
        valor_str = input(mensaje)
        if valor_str.strip() and valor_str.replace(".", "", 1).replace("-", "", 1).isdigit() and float(valor_str) != 0.0:
            valor = float(valor_str)
            return valor
        else:
            print("Error: Ingrese un valor numérico válido.")

def obtener_valor_no_vacio(mensaje):
    while True:
        valor_str = input(mensaje)
        if valor_str.strip() and valor_str != "0":
            return valor_str
        else:
            print("Error: No se permiten valores vacíos.")




def correr_parte_1():
    while True:
        try:
            vehiculo_a_agg = int(input('¿Cuántos vehículos desea insertar?: '))
            break
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

    
    automoviles = []
    contador = 0    

    while contador < vehiculo_a_agg:
        marca = obtener_valor_no_vacio('Inserte la marca del automóvil: ')
        modelo = obtener_valor_no_vacio('Inserte el modelo del automóvil: ')
        nro_ruedas = obtener_entero_valido('Inserte el numero de ruedas del automóvil: ')
        velocidad = obtener_flotante_valido('Inserte la velocidad del automóvil en km/h: ')
        cilindrada = obtener_flotante_valido('Inserte la cilindrada del automóvil en cc: ')

        automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        automoviles.append(automovil)

        contador += 1

    for index, automovil in enumerate(automoviles, start=1):
        print(f'Datos del automóvil {automoviles.index(automovil) + 1}: Marca: {automovil.marca}, '
            f'Modelo: {automovil.modelo}, Número de ruedas: {automovil.nro_ruedas}, '
            f'Velocidad: {automovil.velocidad} km/h, Cilindrada: {automovil.cilindrada} cc')

def correr_parte_2():
    particular = AutoParticular("Ford", "Fiesta", 4, 180, 500, 5)
    carga = AutoCarga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    print(particular.__str__())
    print(carga.__str__())
    print(bicicleta.__str__())
    print(motocicleta.__str__())

    print(f'Motocicleta es instancia con relación a Vehículo:', isinstance (motocicleta, Vehiculo))
    print(f'Motocicleta es instancia con relación a Automovil:', isinstance (motocicleta, Automovil))
    print(f'Motocicleta es instancia con relación a Vehículo particular', isinstance (motocicleta, AutoParticular))
    print(f'Motocicleta es instancia con relación a Vehículo de Carga:', isinstance (motocicleta, AutoCarga))
    print(f'Motocicleta es instancia con relación a Bicicleta:', isinstance (motocicleta, Bicicleta))
    print(f'Motocicleta es instancia con relación a Motocicleta:', isinstance (motocicleta, Motocicleta))




if __name__ == "__main__":
    while True:
        print("Seleccione una opción:")
        print("1. Correr parte 1")
        print("2. Correr parte 2")
        print("0. Salir")
        
        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            correr_parte_1()
        elif opcion == "2":
            correr_parte_2()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")