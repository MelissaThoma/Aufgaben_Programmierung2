print("Hallo")
print("why???")

""" Notenverwaltung
---------------
1 ... Fächer mit zugehörigen Noten eingeben
2 ... Notendurchschnitt berechnen
3 ... Drei besten Fächer mit Noten ausgeben und
den zugehörigen Notendurchschnitt berechnen.
4 ... Drei schlechtesten Fächer mit Noten ausgeben
und den zugehörigen Notendurchschnitt berechnen.
5 ... Bonus: Nach Fächern suchen und den zugehörigen
Notendurschnitt berechnen.
0 ... Exit"""


noten = {}

while True:
    print("\n1 Eingeben")
    print("2 Durchschnitt")
    print("3 Drei beste")
    print("4 Drei schlechteste")
    print("5 Fach suchen")
    print("0 Exit")

    wahl = input("Wahl: ")

    if wahl == "0":
        break

    # 1 Noten eingeben
    elif wahl == "1":
        fach = input("Fach: ")
        try:
            note = float(input("Note: "))
            noten[fach] = note
        except:
            print("Ungültige Eingabe")

    # 2 Durchschnitt
    elif wahl == "2":
        if len(noten) == 0:
            print("Keine Noten vorhanden")
        else:
            avg = sum(noten.values()) / len(noten)
            print("Durchschnitt:", round(avg, 2))

    # 3 Drei beste
    elif wahl == "3":
        beste = sorted(noten.items(), key=lambda x: x[1], reverse=True)[:3]
        for fach, note in beste:
            print(fach, note)

    # 4 Drei schlechteste
    elif wahl == "4":
        schlechteste = sorted(noten.items(), key=lambda x: x[1])[:3]
        for fach, note in schlechteste:
            print(fach, note)

    # 5 Fach suchen
    elif wahl == "5":
        fach = input("Fach: ")
        if fach in noten:
            print(fach, noten[fach])
        else:
            print("Nicht gefunden")



    