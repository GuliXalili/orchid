import email
from inspect import ismemberdescriptor
import logging


tanlov = input("Registratsita:, Login: ")
 
if tanlov == '1':
    print("Registratsiyaga xush kelibsiz")
    ism = input("ismingiz: ")
    familiy = input("familiyangiz:")
    email = input("emailingiz: ")
    parol = input("parolingiz: ")
    print(ism + "siz ruyhattan uttingiz")
    
elif tanlov == '2':
    print("Login va parolni kiriting")
    login = input("Loginni kiriting") 
    parol = input("Parolingiz") 
    if login == "admin" and parol == '123':
        print("Admin dasturga kirdingiz")
    elif login != "admin" and parol == '123':
        print(" Login xato")
    elif login == "admin" and parol != '123':
        print("Parol xato")
        
else:
    for x in range(60):
        print(x)
    print("Dasturda xato bor")

    
    
    
