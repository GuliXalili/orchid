son = [0, 0, 0,[0, 0, [0, "1, 2 yoki, 3ni tanlang: "]]]

b = int(input(son[3][2][1]))

if b == 1 :
        a = int(input("Birinchi son: "))
        amal = input("Amal: ")
        b = int(input("Ikkinchi son: "))


        if amal == "+":
            print(a + b)
        
        elif amal == "-":
            print(a - b)
        
        elif amal == "*":
            print(a * b)
        
        elif amal == "/":
            print(a / b)
            
elif b == 2 :
    login = int(input("Loginni kiriting: "))
    parol = int(input("Parolni kiriting: "))
    
    if login == 1234 and parol == 8976:
        print("tugri")
    elif login != 1234 and parol == 8976:
            print("Login xato")
    elif login == 1234 and parol != 8976:
            print("Parol xato")
            
elif b == 3:
    class Gul:
        def __init__(self, nomi, rangi, narxi):
            self.nomi = nomi
            self.rangi = rangi
            self.narxi = narxi
        def __str__(self):
            return f"{self.nomi},{self.rangi},{self.narxi}"
        
    g1 = Gul("Lola", "Pushti", 20000)
    g2 = Gul("Atirgul", "Qizil", 10000)
    g3 = Gul("Qizgaldoq", "qirmizi", 5000)

    print(g1)
    print(g2)
    print(g3)
        