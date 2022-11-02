lugat = {
    "Tesla": {
        "a": ["Model 3", "5 497 500 P"],
        "b": ["Model S", "7 900 000 P"],
        "c": ["Model X", "7 600 000 P"]
        },
    "Lada": {
        "d": ["Granta", "678 300 000 c"],
        "e": ["Largus", "1 300 900 c"],
        "f": ["Vesta", "1 121 900 c"] 
        },
    "Daewoo": {
        "g": ["Lacetty", "200 000 000 c"],
        "h": ["Matiz", "60 000 000 c"],
        "i": ["Tiko", "30 000 000 c"]
    }
}

komp = input("Kompaniya nomini kiriting: ")

tanla = input('''Tesla
        a: Model 3, 5 497 500 P
        b: Model S, 7 900 000 P
        c: Model X, 7 600 000 P
        Lada
        d: Granta, 678 300 000 c
        e: Largus, 1 300 900 c
        f: Vesta, 1 121 900 c
        Daewoo
        g: Lacetty, 200 000 000 c
        h: Matiz, 60 000 000 c
        i: Tiko, 30 000 000 c 
        Shulardan birini tanlang; ''')
 
if komp.lower() == "tesla":
    if tanla.lower() == "a":
        print(lugat["Tesla"]["a"])
    elif tanla.lower() == "b":
        print(lugat["Tesla"]["b"])
    elif tanla.lower() == "c":
        print(lugat["Tesla"]["c"])


elif komp.lower() == "lada":
    if tanla.lower() == "d":
        print(lugat["Lada"]["d"])
    elif tanla.lower() == "e":
        print(lugat["Lada"]["e"])
    elif tanla.lower() == "f":
        print(lugat["Lada"]["f"])
        
        
elif komp.lower() == "daewoo":
    if tanla.lower() == "g":
        print(lugat["Daewoo"]["g"])
    elif tanla.lower() == "h":
        print(lugat["Daewoo"]["h"])
    elif tanla.lower() == "i":
        print(lugat["Daewoo"]["i"])
     