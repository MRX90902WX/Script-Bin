import sys
from random import randint
from os import system

system("clear")
system("setterm -foreground red")
print("/////////////////////////////////////////////")
print(" _   _                            ____")
print("| \ | | __ _ _ __ ___  ___  ___  / ___|")
print("|  \| |/ _` | '_ ` _ \/ __|/ _ \| |  _")
print("| |\  | (_| | | | | | \__ \ (_) | |_| |")
print("|_| \_|\__,_|_| |_| |_|___/\___/ \____| v2.0")
print("")
print("/////////////////////////////////////////////")
print("")
print("")
system("setterm -foreground green")
bin_format = input("[+]Ingrese el bin: ")
fecha_cad = input("[+]Ingrese el mes y el año: ")
cantidad = input("[+]Ingrese la cantidad a generar: ")
print("")
print(" TARGET         CVV  MM/AA")

def esValido(card_number):
  
   sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

def generar_cc(bin_format):
  cc = ""
  if len(bin_format) == 16:
    for i in range(15):
      if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        cc += bin_format[i]
        continue
      elif bin_format[i] == "x":
        cc += str(randint(0, 9))
      else:
        print("\nCaracter no valido en el formato: {}\n".format(bin_format))
        print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    for i in range(10):
      verificador = cc + str(i)
      if esValido(verificador):
        cc = verificador
        break
      else:
        verificador = cc

  else:
    print("\nERROR: Inserte un bin válido\n")
    print("SOLUCIÓN: El formato del bin es: xxxxxxxxxxxxxxxx de 16 dígitos\n")
    sys.exit()

  return cc

def ccv_gen():
  ccv = ""
  num = randint(10, 999)
  ccv = "0" + str(num) if num < 100 else str(num)
  return ccv

def main():
  for i in range(int(cantidad)):
    cc = generar_cc(bin_format)
    print(f"{cc}|{ccv_gen()}|{fecha_cad}")

main()

print("\n\033[1;32mTodas las tarjetas fueron validadas con exito ")
