class Client:
    def __init__(self,name,last_name,run,mail,password,money = 0,total_money=0):
        self.name = name
        self.last_name = last_name
        self.run = run
        self.mail = mail
        self.password = password
        self.money = money
        self.total_money = total_money

    
    def account_bank(self):
        print("---INGRESAR CUENTA---")
        print("nombre del cliente: ",self.name)
        print("apellido del cliente: ",self.last_name)
        print("run del cliente: ",self.run)
        print("mail del cliente: ",self.mail)
        password = (input("ingrese su contraseña: "))
        repeat_password = (input("vuelva a ingresar la contraseña: "))
        if (repeat_password==password):
            print("ingreso a la cuenta")   
            
            print("-MENU-")    
            print("1-ingresar dinero") 
            print("2-retirar dinero")
            print("3-saldo de la cuenta")
            print("4-salir de la cuenta")
            option= int(input("ingrese una de las opciones: "))

            if(option==1):
                money = float(input("ingrese el dinero a depositar: "))
                if(money>0):
                    self.money+= money
                    print("el dinero a depositar sera: ",self.money)
                elif(money<=0):
                    print("no se puede depositar esa cantidad de dinero")
            elif(option==2):
                money = float(input("ingrese el dinero a retirar: "))
                if(self.money>money):
                    self.money-= money
                    print("el dinero a retirar sera: ",self.money)
                elif(self.money<money):
                    print("no se puede retirar esa cantidad de dinero")    
            elif(option==3):
                print("saldo actual: ",self.money)
            elif(option==4):
                print("hasta pronto")
                exit()  
        else:
            print("el gmail y la contraseña no coinciden")
