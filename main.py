from bank import Client

def main():
    client1 = ""
    name = ""
    last_name = ""
    run = ""
    mail = ""
    password = ""
    money = 0
    
    name = (input("ingrese su nombre: "))
    last_name = (input("ingrese su apellido: "))
    run = (input("ingrese su rut: "))
    mail = (input("ingrese su mail: "))


    client1 = Client(name,last_name,run,mail,password,money)

    client1.account_bank()
    
    
main()
