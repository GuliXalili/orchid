ism = input("ismingizni kiriting")
familiya = input("familiyangizni  kiriting")
parol = input("parolni kiriting")

if ism == "Gul" and familiya == "aliyeva" and parol == "9090":
    print('platformaga kirdingiz')
elif ism != "Gul" and familiya == "aliyeva" and parol != "9090":
    print('ismni va parolni xato kiritdingiz')
elif ism == "Gul" and familiya != "aliyeva" and parol == "9090":
    print('familiyani xato kiritdingiz')
elif ism == "Gul" and familiya =="aliyeva" and parol != "9090":
    print('parol xato')
else:
    print('platformaga kirolmadingiz')
 
    
    
