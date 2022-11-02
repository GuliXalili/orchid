a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))

def son(a, b):
    while b > a:
            a += 1
            print(str(a) + " soniya")
            
son(a, b)
        