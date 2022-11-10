import Valores_3 as bs3
  
while True:

    bs3.h = int(input("Insira o valor das horas: "))
    m = int(input("Insira os minutos: "))

    if bs3.h < 0:
        break
    
    elif m < 0:
        break

    elif bs3.h == 24:
        print(f"São {bs3.AM('a')}:{m} AM.")
        continue
                               
    elif bs3.h >= 12:
        print(f"São {bs3.PM('p')}:{m} PM.")
        continue
                       
    elif bs3.h < 12:
        print(f"São {bs3.AM('a')}:{m} AM.")
        continue

    
    

