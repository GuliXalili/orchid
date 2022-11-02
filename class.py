
qwer = input("Son: ")



class Chel:
    def __init__(self, ism, fam, yosh):
        self.ism = ism
        self.fam = fam
        self.yosh = yosh
        
    def __str__(self):
        return f"Ism: {self.ism}, Fam: {self.fam}, Yosh: {self.yosh}"

a = Chel("Gulhayo", "Xalilova", 21)
b = Chel("Iboxon", "Xalilova", 28)



class Animal:
    def __init__(self, tur, laqab, rangi):
        self.tur = tur
        self.laqab = laqab
        self.rangi = rangi
        
    def __str__(self):
        return f"Tur: {self.tur}, Laqab: {self.laqab}, Rangi: {self.rangi}"

c = Animal("Quy", "Sevara", "oppoq")
d = Animal("Eshshak", "Umida", "sariq")



if qwer == "1":
    print(a)
    print(b)
   
    
elif qwer == "2":
    print(c)
    print(d)
    



    
    