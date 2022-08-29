
alamittainen_kuha = 37
kuhan_pituus = int(input("Kuhan pituus senttimetreinä? "))

if kuhan_pituus <37:
    print("Laske kuha takaisin järveen.")
    print(f"Alimmasta hyväksytystä pituudesta puuttuu {alamittainen_kuha - kuhan_pituus} cm")

elif kuhan_pituus >37:
    print("Voit pitää kuhan.")