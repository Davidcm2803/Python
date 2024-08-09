import os
from turtle import clear
import time
clear= lambda:os.system("cls")

class hotel:
    #valor por noche por persona
    valordia=55000
    print("Bienvenido a nuestro sistema")
    time.sleep(0.3)
    usuario = input("\n Por favor ingrese su usuario: ")

    while usuario != "123":
        print("\n El usuario es incorrecto, ingrese el usuario nuevamente ")
        usuario = input("\n Por favor ingrese su usuario correctamente: ")
    time.sleep(0.5)
    print("\nUsuario confirmado. Ingrese la contraseña")
    time.sleep(0.3)
    contrasena = input("\nPor favor ingrese su contraseña: ")
    while contrasena != "12":
        print("\n La contraseña es incorrecta, Por favor ingrese su contraseña: ")
        contrasena = input("\n Por favor ingrese su contraseña correctamente: ")
    time.sleep(1)    
    print("\nContraseña confirmada!")
    time.sleep(0.3)
    print("bienvenido estimado", usuario, "puede empezar a reservar")
    time.sleep(1)

    def menu(self):
        clear()
        time.sleep(1)
        print("                 MENÚ \n1. Informacíon \n2. Reservar \n3. Salir")
        opcion=int(input("\n Seleccione el numero de la gestion que desea realizar: "))
        if opcion==1:
            self.informacion(self)
            self.menu(self)
        
        elif opcion==2:
            self.reserva(self)
        elif opcion==3:
            print("gracias por usar el codigo")
        else:
            print("Intenta un número valido")
            time.sleep(2)
            self.menu(self)
        clear()          
    def informacion(self):
        time.sleep(1.5)
        clear()
        print("                 Informacion \n \n El costo por noche tiene un valor de",self.valordia,"\n A continuacion un listado con el descuento por personas\n 2 personas: 10%\n 3 personas: 15%\n 4 personas: 20%\n 5 o más peronas: 30%")
        opcion=int(input("Si desea regresar al menu principal Presione 1 o si desea salir presione 2: "))
        if opcion==1:
            self.menu(self)
        else:
            print("Gracias por usar el codigo")

    def reserva(self):
        time.sleep(1)
        clear()
        print("                 Reserva \n")
        while True:
            try:
                self.personas=int(input("Para cuantas personas le gustaría reservar?:"))
                break
            except ValueError:
                print("\n Se permiten solamente numeros enteros")
        while True:
            try:
                self.dias=int(input("Cuantas noches quiere reservar?: "))
                break
            except ValueError:
                print("\n Se permiten solamente numeros enteros")
        while True:
            try:
                self.cuartos=int(input("Cuantas cuartos desea tener?: "))
                break
            except ValueError:
                print("\n Se permiten solamente numeros enteros")
        self.lista1=["Total personas",self.personas,"Total días",self.dias,"Total cuartos",self.cuartos]
        print(self.lista1)
        self.Preciosindescuento=self.dias*self.valordia
        if (self.personas==2):
            self.Totalapagar = (self.Preciosindescuento*0.5)
        elif (self.personas==3):
            self.Totalapagar = (self.Preciosindescuento*0.10)
        elif (self.personas==4):
            self.Totalapagar = (self.Preciosindescuento*0.13)
        else:
            self.Totalapagar = (self.Preciosindescuento*0.15)
        opcion=int(input("Si desea más información acerca de los EXTRAS presione 1 o si desea pagar presione 2: "))
        if opcion==1:
            self.extras(self)
        elif opcion==2:
            self.pagosinextra(self)
        time.sleep(3)
    def extras(self):
        time.sleep(1)
        clear()
        print("                Extras \n \n Cama Queen Size tiene un costo de 10000 cada \n King Size tiene un costo de 7000 cada una \n Camas indivuales no tienen precio adicional")
    
    def pagosinextra(self):
        print("holaa")

Riu=hotel
print(Riu.menu(Riu))




