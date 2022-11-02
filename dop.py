a = int(input("Birinchi son: "))
b = int(input("Ikkinchi son: "))
c = 0

if a % 2 == 0:
    print("juft son kiritdingiz")
if a % 2 != 0:
    print("toq son kiritdingiz")

for x in range(a, b):
    c += x
print("yig'indi", str(c), "ga teng")
if c % 2 == 0:
    print(str(c), "Juft son")
elif c % 2 != 0:
    print(str(c), "toq son")  
