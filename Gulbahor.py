
a = input(''' 1 = String
2 = Integer
3 = float
4 = boolean
5 = List
Sonlardan birini tanlang:''')


if a == "1":
    print("Bu string malumot")
    b = input('''
    1)ozimiz haqimizda malumot
    2)registratsiya
    qaysi birini tanlaysiz:
    ''')
    if b == '1':
        print("Xalilova Gulhayo G'ofur qizi NDPida 2-kurs talabasi")
    elif b == '2':
        i = input("ism: ")
        f = input("familiya: ")
        p = input("Parol: ")
        r = input("registratsiya: ")
    
elif a == "2":
    print("Bu integer malumot")
    c = input('''1)kalkulyator
    2)toq son
    3)juft son
    4)00 bilan tugaydigan sonlar
    shulardan birini tanlang: ''')
    if c == '1':
        bir = int(input("Birinchi son: "))
        ikki = int(input("Ikkinchi son: "))
        amal = input("Amalni kiriting")
        def cal(bir, ikki):
            if amal == "+":
                print(bir + ikki)
            elif amal == "-":
                print(bir - ikki)
            elif amal == "*":
                print(bir * ikki)
            elif amal == "/":
                print(bir / ikki)
                
        cal(bir, ikki)
        
    elif c == '2':
        aa = -1
        while aa < 100:
            aa += 2
            print(aa)
    elif c == '3':
        bb = 0
        while bb < 100:
            bb += 2
            print(bb)
    elif c == '4':
        ab == 0
        while ab < 900:
            ab += 100
            print(ab)
        
elif a == "3":
    print("Bu float malumot")
elif a == "4":
    print("Bu boolean malumot")
elif a == "5":
    print("Bu list malumot")
else:
    print("Error")