import sys
import os
import datetime
from random import randint

a = input("[+]Ingrese el bin que desea generar: ")
b = input("[+]Ingrese el mes y el año de caducidad: ")

# Bin generador

bin_format = ""
date = print(f"{b}")
limit = 30
ccv = True
check = True

#CHECKER BASADO EN ALGORITMO LUHN
def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

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

#GENERA UNA BASE DE BIN XXXXXXXXXXXXXXXX
def ccgen(bin_format):
    out_cc = ""
    if len(bin_format) == 16:
        #Iteration over the bin
        for i in range(15):
            if bin_format[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                out_cc = out_cc + bin_format[i]
                continue
            elif bin_format[i] in ("x"):
                out_cc = out_cc + str(randint(0,9))
            else:
                print("\nCaracter no valido en el formato: {}\n".format(bin_format))
                print("El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
                sys.exit()

         #Generate checksum (last digit) -- IMPLICIT CHECK
        for i in range(10):
            checksum_check = out_cc
            checksum_check = checksum_check + str(i)

            if cardLuhnChecksumIsValid(checksum_check):
                out_cc = checksum_check
                break
            else:
                checksum_check = out_cc

    else:
        print("\033[1;32m")
        print("\nERROR: Inserta un bin valido\n")
        print("SOLUCION: El formato del bin es: xxxxxxxxxxxxxxxx de 16 digitos\n")
        sys.exit()

    return(out_cc)


#Random ccv gen
def ccvgen():
    ccv = ""
    num = randint(10,999)

    if num < 100:
        ccv = "0" + str(num)
    else:
        ccv = str(num)

    return(ccv)


#The main function
    def main():
        for i in range(int(limit)):
        if bin_format = "": 
            if ccv and date:                                                                                                                                 
               (ccgen(bin_format) + "|" + ccvgen() + "|" + print(f"{b}")())
            elif ccv and not date:
               (ccgen(bin_format) + "|" + ccvgen())
            elif date and not ccv:
                (ccgen(bin_format) + "|"  + print(f"{b}")())
            elif not date and not ccv:
                (ccgen(bin_format))
                

