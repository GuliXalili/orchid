a = [["Gulhayo"], ["Gulbahor"]]
b = int(input("Sonni kiriting: "))

def son(b):
    if b % 2 == 0:
        print(a[1])
        
    elif b % 2 != 0:
        print(a[0])
        
son(b)   