import math

vuosiluku = int(input("Kirjoita vuosiluku "))

if vuosiluku % 4 == 0:
    print("Vuosiluku on karkausvuosi")
elif vuosiluku % 100 and vuosiluku % 400 == 0:
    print("Vuosiluku on kaurkausvuosi")
else:
    print("Vuosiluku ei ole karkausvuosi")
