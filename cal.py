try:
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
        
except ValueError:
    print("Tur xatoligi bor")
except ZeroDivisionError:
    print("0ga bo'la olmaysiz")
except:
    print("Xatolik mavjud")






