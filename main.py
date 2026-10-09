import weeropdracht
import smartapp_controller

def main():
    while True:
        print("\n --SmartApp-- ")
        print("1: Weerstation")
        print("2: Smart App Controller")
        print("3: Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            weeropdracht.haal_temperatuur()
            weeropdracht.weerstation()
        elif keuze == "2":
            wachtwoord = input("Voer het WACHTWOORD in : ")

            if wachtwoord == "WACHTWOORD":
                smartapp_controller.smart_app_controller()
            else:
                print("onjuist wachtwoord.")

        elif keuze == "3":
            print("SmartApp afgesloten.")
            break
        else:
            print("Ongeldige keuze.")

if __name__ == "__main__":
    main()