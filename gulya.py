a = int(input("birinchi son: "))
b = int(input("ikkinchi son: "))
amal = input("amalni kiriting: ")
c = 0

def son(a, b, c):
    if amal == "+":
        print("Javob: ", a+b)
        while c <= a+b:
            c += 1
            print(c)
  
    elif amal == "-":
        print("Javob: ", a-b)
        while c <= a-b:
            c += 1
            print(c)
     
    
    elif amal == "*":
        print("Javob: ", a*b)
        while c <= a*b:
            c += 1
            print(c)

    elif amal == "/":
        print("Javob: ", a/b)
        while c <= a/b:
            c += 1
            print(c)
    
son(a, b, c)


