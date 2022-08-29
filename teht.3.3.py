gender = input("Sukupuolesi (nainen/mies)? ")
hg_value = int(input("Hemoglobiinisi (g/l)? "))

if gender == "nainen":
    if not (5 < hg_value < 300):
        print("Virheellinen hemoglobiini arvo!")
    elif hg_value < 117:
        print("Hemoglobiini arvo on alhainen")
    elif hg_value <= 175:
        print("Hemoglobiini arvo on normaali")
    else:
        print("Hemobloniini arvo on korkea")
elif gender == "mies":
    if not (5 < hg_value < 300):
        print("Virheellinen hemoglobiini arvo!")
    elif hg_value < 134:
        print("Hemoblogiini arvo on alhainen")
    elif hg_value <= 195:
        print("Hemoglobiini arvo on normaali")
    else:
        print("Hemoglobiini arvo on korkea")

