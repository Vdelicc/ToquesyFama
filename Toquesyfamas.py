## Codigo de proyecto final.
## Juego de Toques y Famas.
import random
num_adivina = random.sample(range(10),4)
print(num_adivina)
#num_1 = num_adivina //100
#print(num_adivina[0]
intentos = 0
while  intentos < 5:  
     print("ingresa un numero de 4 digitos distintos")
     Num_user = int(input())
     intentos +=1
     print(Num_user)
     Num1 = Num_user //1000
     Num2 = (Num_user - Num1*1000) //100
     Num3 = (Num_user - Num1*1000-Num2*100) //10
     Num4 = (Num_user - Num1*1000-Num2*100-Num3*10) 
     if Num1 == Num2 or Num1 == Num3 or Num1 == Num4 or Num2 == Num3 or Num2 == Num4 or Num3 == Num4:
        print("Debe ingresar un numero sin digitos repetidos")
     else:
           
else:
   print("perdiste")


