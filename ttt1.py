import time
from ttt import *

if login == "0000":
    print("Molodets!")
elif parol == "1234":
    print("Gap yoq!")
elif login == 0000 and parol != 1234 :
    b = 0
    while  b < 10:
        b += 1
        time.sleep(1)
        print(b) 


elif login != 0000 and parol != 1234:
        a = 0
        while  a < 60:
            a += 1
            time.sleep(1)
            print(a)
            

