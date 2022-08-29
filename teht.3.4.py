import math

vuosiluku = int(input("Kirjoita vuosiluku "))

if int(vuosiluku/4):
    print("Vuosiluku on karkausvuosi")

if not int(vuosiluku/4):
    print("Vuosiluku ei ole karkausvuosi")

elif (vuosiluku /100 and vuosiluku /400):
    print("Vuosiluku on karkausvuosi")
#else:
    #print("Vuosiluku ei ole karkausvuosi")
