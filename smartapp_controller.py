def aantal_dagen(inputFile):
    text = open("input.txt")
    dayspecs = text.readlines()
    text.close()
    dayspecs = dayspecs[1:]
    return len(dayspecs)

def auto_berekenen(Inputfile, Outputfile):
    text = open(Inputfile)
    dayspecs = text.readlines()
    dayspecs = dayspecs[1:]
    output = open(Outputfile, "w")

    for line in dayspecs:
        info = line.split(" ")
        date = info[0]
        num_people = int(info[1])
        temp_setpoint = int(info[2])
        temp_outside = int(info[3])
        precip = int(info[4])

        verschil = temp_setpoint - temp_outside
        if verschil >= 20 :
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        vents = num_people + 1

        if vents >4:
            vents = 4

        if precip < 3 :
            watering = True
        else:
            watering = False

        output.write(date + ";" + str(cv) + ";" + str(vents) + ";" + str(watering) + "\n")
    output.close()
    text.close()

def overwrite_settings(outputfile):
    date_change = input ("welke datum wil jij veranderen? : ")
    systeem = input("welke systeem? 1 = CV, 2 = vents, 3 = watering : ")
    newvalue = input("wat zou de nieuwe value zijn? : ")
    file = open(outputfile)
    lines = file.readlines()
    file.close()

    gevonded_datum = False
    for line in lines:
        info = line.strip().split(";")
        if info[0] == date_change:
            gevonded_datum = True
    if gevonded_datum == False:
        return -1
    if systeem not in ["1", "2", "3"]:
        return -3
    if systeem == "1":
        if not newvalue.isdigit() or int(newvalue) < 0 or int(newvalue) > 100:
            return -3
    elif systeem == "2":
        if not newvalue.isdigit() or int(newvalue) < 0 or int(newvalue) > 4:
            return -3
    elif systeem == "3":
        if newvalue not in ["0","1"]:
            return -3
    if systeem == "3":
        if newvalue == "0":
            newvalue = "False"
        else:
            newvalue = "True"

    updated_lines = []

    for line in lines :
        info = line.strip().split(";")

        if info[0] == date_change:
            info[int(systeem)] = newvalue

        updated_lines.append(";".join(info) + "\n")
    file = open(outputfile, "w")
    file.writelines(updated_lines)
    file.close()

    return 0

def smart_app_controller():
    while True:
        print("1: aantal dagen bekijken")
        print("2: automatisch berekenen")
        print("3: instellingen overschrijven")
        print("4: stoppen")

        keuze = input("Maak een keuze: ")
        if keuze == "1":
            print("aantal dagen:", aantal_dagen("input.txt"))
        elif keuze == "2":
            auto_berekenen("input.txt", "output.txt")
            print("instellingen automatisch berekend.")
        elif keuze == "3":
            resultaat = overwrite_settings("output.txt")
            print("resultaatcode:", resultaat)
        elif keuze == "4":
            print("programma gestopt.")
            break
        else:
            print("ongeldige keuze.")

if __name__ == "__main__":
    smart_app_controller()
