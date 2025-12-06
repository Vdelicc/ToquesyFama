## Codigo de proyecto final.
## Juego de Toques y Famas.
import random
num_adivina = random.sample(range(10),4)
print(num_adivina)
#num_1 = num_adivina //100
#print(num_adivina[0]
intentos = 0
famas = 0
while  intentos < 6:
     if famas == 4:
          print("ganaste")
     print("ingresa un numero de 4 digitos distintos")
     Num_user = int(input())
     numeros_escritos=[]
     intentos +=1
     Num1 = Num_user //1000
     Num2 = (Num_user - Num1*1000) //100
     Num3 = (Num_user - Num1*1000-Num2*100) //10
     Num4 = (Num_user - Num1*1000-Num2*100-Num3*10) 
     numeros_escritos.extend([Num1, Num2, Num3, Num4])
     i = 0
     for num_escrito in numeros_escritos:
            if num_escrito == num_adivina[i]:
               print("tienes una fama en", num_escrito)   
               i += 1  
               famas += 1  
                
print("perdiste")


