task = '''
1.  Pracujesz dla firmy odzieżowej, której celem jest wypromowanie nowej kolekcji ubrań. 
    Firma ogłosiła konkurs, który ma na celu zdobywanie "lajków" i "udostępnień" na Facebooku.
    Jeśli strona firmy otrzyma danego dnia co najmniej 500 "lajków" i co najmniej 100 "udostępnień",
    to ceny spadną o 10%. Na razie masz napisać fragment programu,
    który rozstrzygnie czy warunki promocji są spełnione czy nie. Jeśli już wiesz jak to zrobić "GO ON!",
    a jeśli chcesz, aby Cię trochę pokierować - zajrzyj do kolejnych punktów:

    zadeklaruj zmienną MIN_LIKES  o wartości 500 i MIN_SHARES o wartości 100

    zadeklaruj zmienną num_likes i num_shares o wartościach wskazujących na to ile było kliknięć LIKE i SHARE na 
    Facebooku. Przypisz tym zmiennym wybrane przez CIebie wartości. Zmieniając te wartości będziesz testować poprawność 
    swojego programu,np 1300 lajków i 55 sharów

    napisz polecenie IF, które w przypadku spełnienia warunku opisanego na początku, wyświetli komunikat o obniżce ceny,
    a w przeciwnym razie wyświetli komunikat o braku wystarczającej ilości lajków i sharów

    przetestuj działanie polecenia IF zmieniając wartości zmiennych num_like i num_shares
'''

print(task)
min_likes = 500
min_shares = 100
num_likes = 1300
num_shares = 55

if min_likes <= num_likes and min_shares <= num_shares:
    print('''
        min_likes = {0:d}
        min_shares = {1:d}
        num_likes = {2:d}
        num_shares = {3:d}
        '''.format(min_likes, min_shares, num_likes, num_shares), '''
        The condition isn't fulfilled.
        ''')
else:
    print('''
            min_likes = {0:d}
            min_shares = {1:d}
            num_likes = {2:d}
            num_shares = {3:d}
            '''.format(min_likes, min_shares, num_likes, num_shares), '''
            The condition is fulfilled.
            ''')

task = '''
2.  Pracujesz dla restauracji, która chce nagrodzić klientów zamawiających w dni robocze (poza weekendem) pizze lub
    duży napój. Klienci spełniający warunki promocji dostaną kupon na darmowego burgera.
    Na razie piszesz polecenie decydujące o spełnieniu warunków promocji. Do dyspozycji masz zmienne:

    isPizzaOrdered - o wartości True/False, która informuje, czy klient kupił Pizzę

    isBigDrinkOrdered - o wartości True/False, która informuje, czy klient zamówił duży napój

    isWeekend - o wartości True/False, która informuje, czy jest weekend

    Napisz polecenie IF, które w przypadku, gdy klient kupił pizzę lub duży napój w dzień poza weekendem,
    wyświetli informację o kuponie na Burgera, a w przeciwnym razie wyświetli komunikat zachęcający do dalszych zakupów.

    Zmieniaj wejściowe warunki logiczne i testuj, czy polecenie zwraca oczekiwany napis.

'''

print(task)
isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('''
        isPizzaOrdered = {0:d}
        isBigDrinkOrdered = {1:d}
        isWeekend = {2:d}
        '''.format(isPizzaOrdered, isBigDrinkOrdered, isWeekend), '''
        You've recieved a coupon for free burger!
        ''')
else:
    print('''
        isPizzaOrdered = {0:d}
        isBigDrinkOrdered = {1:d}
        isWeekend = {2:d}
        '''.format(isPizzaOrdered, isBigDrinkOrdered, isWeekend), '''
        Thank you for your purchase!
        ''')

task = '''
3.  Twój zespół opracowuje przeglądarkę internetową w Pythonie! Twoim zadaniem jest sprawdzenie,
    czy operacja pobierania pliku na dysk ma się szansę udać, czy jest od razy skazana na porażkę ze względu na brak
    miejsca na dysku. Na wejściu masz następujące zmienne:

    diskSize - zmienna numeryczna (np. o wartości 140) oznaczająca wielkość dysku w GB

    diskSizeUsed - zmienna numeryczna (np. o wartości 133) oznaczająca ilosć zajętego miejsca na dysku w GB

    fileSize - zmienna numeryczna (np o wartości 10) oznaczająca wielkość pobieranego pliku w GB

    Zbuduj polecenie IF, które w przypadku, gdy jest wystarczająco wolnego miejsca na dysku wyświetli komunikat
    "File can be downloaded". W przypadku, gdy plik jest za duży, ma być wyświetlony komunikat o braku miejsca na dysku

    Zmieniając parametry wejściowe przetestuj działanie polecenia
'''

print(task)
diskSize = 140
diskSizeUsed = 133
fileSize = 10

if (diskSize - diskSizeUsed) > fileSize:
    print('''
        diskSize = {0:d}
        diskSizeUsed = {1:d}
        fileSize = {2:d}
        '''.format(diskSize, diskSizeUsed, fileSize), '''
        You can download the file.
        ''')
else:
    print('''
            diskSize = {0:d}
            diskSizeUsed = {1:d}
            fileSize = {2:d}
            '''.format(diskSize, diskSizeUsed, fileSize), '''
            You don't have enough empty storage to download this file.
            ''')