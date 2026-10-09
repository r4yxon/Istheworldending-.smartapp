import requests


def haal_temperatuur():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.0908&longitude=5.1222&current=temperature_2m&timezone=auto"

    response = requests.get(url)
    data = response.json()
    weer_momenteel = data ["current"]
    temperatuur = weer_momenteel["temperature_2m"]

    print(f"De huidige temperatuur in Utrecht is: {temperatuur} C")
    return temperatuur

def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid/100 * windsnelheid

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return("Het is heel koud en het stormt! Verwarming helemaal aan!")

    elif gevoel < 0 and windsnelheid <= 10:
        return ("Het is behoorlijk koud! Verwarming aan op de benedenverdieping!")

    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return ("Het is best koud en het waait; verwarming aan en roosters dicht!")

    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return ("Het is een beetje koud, elektrische kachel op de benedenverdieping aan!")

    elif 10 <= gevoel < 22:
        return ("Heerlijk weer, niet te koud of te warm.")

    else:
        return ("Warm! Airco aan!")

def weerstation():
    temperaturen = []

    for dag in range(7):
        while True:
            temperatuur = input("wat is op dag " + str(dag + 1) + " de temperatuur in Celsius? : ")
            if temperatuur == "":
                return
            try:
                temperatuur = float(temperatuur)
                break
            except ValueError:
                print("voer een geldig getal.")
        temperaturen.append(temperatuur)

        while True:
            windsnelheid = input("Wat is op dag " + str(dag + 1) + " de windsnelheid in m/s? : ")
            if windsnelheid == "":
                return
            try:
                windsnelheid = float(windsnelheid)
                break
            except ValueError:
                print("voer een gelding getal.")

        while True:
            luchtvochtigheid = input("Wat is op dag " + str(dag + 1) + " de vochtigheid in % : ")
            if luchtvochtigheid == "":
                return
            try:
                luchtvochtigheid = int(luchtvochtigheid)

                if 0 <= luchtvochtigheid <=100:
                    break
                else:
                    print("type een % tussen 0 en 100 in.")

            except ValueError:
                print("voer een gelding getal.")

        print("Het is " + str(temperatuur) + "C (" + str(Fahrenheit(temperatuur)) + "F)")
        print(weerrapport(temperatuur,windsnelheid,luchtvochtigheid))
        print("the gemiddelde temperatuur tot nu is :" + str(sum(temperaturen) / len(temperaturen)))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

if __name__ == "__main__":
    weerstation()
