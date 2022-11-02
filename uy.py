from re import I


class Odam:
    def __init__(self, ism, familiya, xobbi):
        self.ism = ism
        self.familiya = familiya
        self.xobbi = xobbi
        
    def __str__(self):
        return f'{self.ism}, Familiyasi:{self.familiya}, Xobbi:{self.xobbi}'

class Kasb(Odam):
    def __init__(self, ism, familiya, xobbi, turi, maosh, vaqti):
        super().__init__( ism, familiya, xobbi)
        self.turi = turi
        self.maosh = maosh
        self.vaqti = vaqti
        
    def chiqarish(self):
        print(self.ism,self.familiya,self.xobbi,self.turi,self.maosh,self.vaqti)
    
a = Kasb("Shaxnoza", "Xaydarova", "uxlash",  "Uqituvchi", "1000$", "20 soat")
b = Kasb("Gulhayo", "Xalilova", "uxlash", "Stuardessa", "2000$", "Belgilanmagan")
c = Kasb("Gulbaxor", "Ergasheva", "uxlash", "IT mataxassisi", "3000$", "Belgilanmagan")

print(a.chiqarish())
print(b.chiqarish())
print(c.chiqarish())

class Sifati(Odam):
    def __init__(self, ism, familiya, xobbi, kurinishi, buyi, vazni):
        super().__init__( ism, familiya, xobbi,)
        self.kurinishi = kurinishi
        self.buyi = buyi
        self.vazni = vazni
        
    def chiqarish1(self):
        print(self.ism,self.familiya,self.xobbi,self.kurinishi,self.buyi,self.vazni)
    
d = Sifati("Shaxnoza", "Xaydarova", "uxlash",  "Kelishgan", 1.68, 50)
e = Sifati("Gulhayo", "Xalilova", "uxlash", "Chiroyli", 1.68, 48)
f = Sifati("Gulbaxor", "Ergasheva", "uxlash", "Guzal", 1.68, 49)

print(d.chiqarish1())
print(e.chiqarish1())
print(f.chiqarish1())

class Malumot(Odam):
    def __init__(self, ism, familiya, xobbi, address, nomer, yoshi):
        super().__init__( ism, familiya, xobbi)
        self.address = address
        self.nomer = nomer
        self.yoshi = yoshi
        
    def chiqarish2(self):
        print(self.ism,self.familiya,self.xobbi,self.address,self.nomer,self.yoshi)
        
i = Malumot("Shaxnoza", "Xaydarova", "uxlash", "Nurota", 1234567, 19)
j = Malumot("Gulhayo", "Xalilova", "uxlash", "Navoi", 3564785, 21)
k = Malumot("Gulbaxor", "Ergasheva", "uxlash", "Qiziltepa", 5875389, 19)

print(i.chiqarish2())
print(j.chiqarish2())
print(k.chiqarish2())
        
        
    