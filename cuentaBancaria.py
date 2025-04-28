#Cuenta bancaria usando conceptos de POO

#Se deben corregir errores del codigo ya que necesitan cambios. VER LUEGO

class Cuenta:
    def __init__(self,titular,numero_cuenta,saldo, monto):
        self.titular = titular
        self.numero_cuenta = numero_cuenta 
        self.saldo = saldo
        self.monto = monto

    #metodos 
    def ingresar_datos(self,titular,numero_cuenta,saldo):
        titular = input("Ingrese su nombre y apellido: ")
        print(titular)
        numero_cuenta = int(input("Ingrese su numero de cuenta: "))
        print(numero_cuenta)
        saldo = float(input("Ingrese el saldo correspondiente: "))
        print(saldo) 

    #Depositar dinero a la cuenta, osea es necesario conocer el monto que se desea ingresar, ademas de la cuenta a la que se quiere ingresar

    def depositar_dinero(self,monto,saldo):
        if monto >0:
            print("Se ha depositado {self.monto} a la cuenta de {self.titular}")
            self.saldo += monto 
        else:
            print("Saldo insuficiente para ingresar dinero. Vuelva a interntarlo: ")       

    def trasnferir_dinero(self,cuenta, otra_cuenta,monto):
        if monto > self.saldo:
            print("Cantidad elevada de la cuenta")
        else:
            if monto <= self.saldo:
                self.saldo -= monto 
                self.otra_cuenta += monto 

            print("La cuenta {self.cuenta} deposito una cantidad de dinero {self.otra_cuenta}")

    def mostrar_datos(self):
        print("El titular de la cuenta es: {self.titular}")
        print("El numero de la cuenta es {self.numero_cuenta}")
        print("La cantidad de dinero disponible en la cuenta bancaria es de : {self.saldo}")        


def main():
    cuenta_1 = Cuenta("Jose Martinez",1234,5000.0)
    cuenta_2 = Cuenta("Martin Suarez",4567,10000.0)

    print ("DATOS DE LA CUENTA BANCARIA")

    opcion = input("INGRESE UNA OPCION CORRESPONDIENTE: ")

    if opcion == '1':
        print("1- INGRESAR DATOS DE LA CUENTA BANCARIA")
        cuenta_1.ingresar_datos()
        return 
    elif opcion == '2':
        print("2-DEPOSITO DE DINERO A LA CUENTA BANCARIA")
        cuenta_2.depositar_dinero()
        return 
    elif opcion == '3':
        print("3-TRASNFERIR DINERO DESDE CUENTA ORIGEN A CUENTA DESTINO")
        cuenta _1.transferir_dinero()
        return 
    elif opcion == '4':
        print("4-MOSTRAR DATOS CORRESPONDIENTES")   
        cuenta_1.mostrar_datos()

    else:
        print("INGRESO UNA OPCION INCORRECTA")     





if __name__ == "__main__":
    main()



