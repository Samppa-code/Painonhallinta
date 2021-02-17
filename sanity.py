# Moduli syötteen oikeellisuuden tarkistamiseen
"""Tarkistaa käyttäjän syötteen oikeellisuuden tarkistusfunktioiden avulla
"""


# Funktioiden määrittelyt

def on_jarkeva(syote, alaraja, ylaraja):
    """ Puhdistaa merkkijonosta ylimääräiset whitespacen ja selvittää onko syötetty avo annujen rajojen sisällä.
     Funkio muuttaa desipaalipilkun desimaali pisteeksi

    Args:
        syote (string): Näppäimmistöltä syötetty arvo
        alaraja (float): Pienin sallittu arvo
        ylaraja (float): Suurin sallittu arvo

    Returns (float) : Käyttäjän syöttämä arvo numeerisena
    """

    # Poistetaan whitespace merkit merkkijonon ympäriltä
    puhditettu_syote = syote.lstrip()
    puhditettu_syote = puhditettu_syote.rstrip()

    # Selvitetään onko merkkijonossa pilkku (,)
    pilkunpaikka = puhditettu_syote.find(",")

    # Jos pilkku löytyy, korvataan pisteellä
    if pilkunpaikka != -1:
        korjattu_syote = puhditettu_syote.replace(",", ".")
    else:
        korjattu_syote = puhditettu_syote

    # Muutetaan korjattu syöte merkkijonosta liukuluvuiksi
    try:
        luku = float(korjattu_syote)
    except:
        print("Syötetyssä tiedossa on ylimääräisiä merkkejä, vain numerot sallittu")
        luku = 0

    # Tarkistetaan, ettei syöte ole alarajan alapuolella
    try:
        if luku < alaraja:
            raise Exception ("Syöttämäsi arvo on alle sallitun")
    except Exception as virheilmoitus:
        print (virheilmoitus)
    
    # Tarkitetaan, ettei syöte ole ylärajan yläpuolella

    try:
        if luku > ylaraja:
            raise Exception ("Syöttämäsi arvo on yli sallitun")
    except Exception as virheilmoitus:
        print (virheilmoitus)

    # Palautetaan luku
    return luku

    # Testataan toimintaa
tulos = on_jarkeva("Sata", 1, 500)
print(tulos)