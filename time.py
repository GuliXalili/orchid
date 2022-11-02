import time

a = int(input("Parolni kiriting: "))

if a == "0000":
    print("Siz dasturga kirdingiz")
else:
        a = 0
        while  a < 6:
            a += 1
            time.sleep(1)
            print(a)



    
