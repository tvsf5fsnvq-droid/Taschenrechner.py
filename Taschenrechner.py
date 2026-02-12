# Die Import-Anweisung 'from _pyrepl.readline import raw_input' ist nicht notwendig und
# würde in den meisten Umgebungen einen Fehler verursachen, wurde entfernt.

def menu():
    """Zeigt das Menü an und verarbeitet die Benutzereingaben."""
    print('Willkommen bei Ihrem Taschenrechner 🧮')
    print('-' * 30)
    print('Drücken Sie die ...')
    print('1 um 2 Zahlen zu summieren (Addition)')
    print('2 um die Differenz von 2 Zahlen zu bestimmen (Subtraktion)')
    print('3 um das Produkt von 2 Zahlen zu bestimmen (Multiplikation)')
    print('4 um 2 Zahlen zu dividieren (Division)')
    print('5 um das Programm zu beenden')
    print('-' * 30)


def taschenrechner():
    """Die Hauptfunktion, die das Menü in einer Schleife anzeigt und Operationen ausführt."""

    while True:
        # Menü anzeigen
        menu()

        # Benutzereingabe für die Option
        # input() wird in Python 3 für die Eingabe von Strings verwendet.
        option = input('Geben Sie nun eine der Zahlen ein (1-5): ')

        # Programm beenden, wenn '5' gewählt wird.
        if option == '5':
            print('Auf Wiedersehen! 👋')
            break

        # Überprüfen, ob die Option eine gültige Operation ist.
        if option in ('1', '2', '3', '4'):
            try:
                # Benutzereingabe für die Zahlen.
                # Die Eingabe wird sofort in einen Gleitkommazahl (float) konvertiert,
                # um sowohl Ganzzahlen als auch Dezimalzahlen zu ermöglichen.
                zahl_eins = float(input('Die erste Zahl, bitte: '))
                zahl_zwei = float(input('Die zweite Zahl, bitte: '))

                # Operationen ausführen
                if option == '1':
                    ergebnis = zahl_eins + zahl_zwei
                    print(f'Das Ergebnis der Addition ist: {ergebnis}')

                elif option == '2':
                    ergebnis = zahl_eins - zahl_zwei
                    print(f'Das Ergebnis der Subtraktion ist: {ergebnis}')

                elif option == '3':
                    ergebnis = zahl_eins * zahl_zwei
                    print(f'Das Ergebnis des Produkts ist: {ergebnis}')

                elif option == '4':
                    # Division durch Null abfangen
                    if zahl_zwei != 0:
                        ergebnis = zahl_eins / zahl_zwei
                        print(f'Das Ergebnis der Division ist: {ergebnis}')
                    else:
                        print('FEHLER: Division durch Null ist nicht erlaubt. 🚫')

            except ValueError:
                # Fehler abfangen, falls der Benutzer keine gültige Zahl eingibt.
                print('FEHLER: Ungültige Eingabe. Bitte geben Sie nur Zahlen ein.')

            # Eine leere Zeile zur besseren Lesbarkeit nach dem Ergebnis
            print('\n' + '=' * 30 + '\n')

        else:
            # Ungültige Menü-Option
            print('Ungültige Option. Bitte wählen Sie eine Zahl zwischen 1 und 5.')
            print('\n' + '=' * 30 + '\n')


# Programm starten
if __name__ == '__main__':
    taschenrechner()