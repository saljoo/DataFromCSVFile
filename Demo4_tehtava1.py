#Puretaan tiedosto listaksi
def tiedoston_purku(vaesto_data: str) -> list:
    vaesto = []
    with open (vaesto_data) as tiedosto:
        for rivi in tiedosto:
            henkilo = rivi.strip().split(",")
            if henkilo[0].isnumeric() == True:
                vaesto.append(henkilo)
            
        return vaesto

#Funktio, jolla tarkistetaan suomea puhuvien naisten määrä
def nainen_suomi(vaesto_data: str) -> int:
    nainen_ja_suomi = 0
    henkilot = []
    x = 0
    for rivi in tiedoston_purku(vaesto_data):
        if rivi[0] != x:
            henkilot.append(rivi)
            x = rivi[0]
    
    for henk in henkilot:
        if henk[2] == "\"2\"" and henk[4] == "\"1\"":
            nainen_ja_suomi += 1
    
    return nainen_ja_suomi

#Funktio, jolla tarkistetaan henkilöiden määrä, joiden perheen koko on ollut edes jossakin vaiheessa vähintään neljä
def perhe_vahintaan_4(vaesto_data: str) -> int:
    maara = 0
    nykyinen = 0
    for rivi in tiedoston_purku(vaesto_data):
        if int(rivi[6]) >= 4 and int(rivi[0]) != nykyinen:
            nykyinen = int(rivi[0])
            maara += 1

    return maara 

#Funktio, jolla tarkistetaan henkilöiden jakautuminen alueittain
def alueet(vaesto_data: str):
    etela_suomi = 0
    lansi_suomi = 0
    ita_suomi = 0
    pohjois_suomi = 0

    for rivi in tiedoston_purku(vaesto_data):
        match rivi[7]:
            case "\"1\"":
                etela_suomi += 1
            case "\"2\"":
                lansi_suomi += 1
            case "\"3\"":
                ita_suomi += 1
            case "\"4\"":
                pohjois_suomi += 1

print(nainen_suomi("vaestolaskenta_data.csv"))
print(perhe_vahintaan_4("vaestolaskenta_data.csv"))