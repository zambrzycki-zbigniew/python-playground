task = '''
1.  Dokuczałeś prowadzącemu ten kurs i dostajesz "za karę zadanie" - musisz wyznaczyć sumy dwóch kolejnych liczb
    od 0 do 50, np
        0+1 = 1
        1+2 = 3
        2+3 = 5
        3+4 = 7 itd.
    Wyjmij kartkę i licz lub:
        zadeklaruj zmienną number i przypisz jej wartość 1
        zadeklaruj zmienną previousNumber i przypisz jej wartość 0
        Napisz  pętlę while, która wykonywać się będzie tak długo, jak długo number jest mniejsze niż 50
        w pętli:
            wyświetl sumę number i previous_number
            do previous_number przypisz wartość number
            zwiększ number o 1
'''

print(task)
i = 1
while i <= 50:
    print(i+(i-1))
    i += 1

task = '''
2.  Teraz napiszesz... poniekąd prostą grę. Zasady są proste. Komputer wymyśli sobie liczbę od 0 do 20,
    a Ty musisz ją zgadnąć!

    Polecenia
        import random
        my_number = random.randint(0,20)

    wygenerują liczbę losową i umieszczą jej wartość w zmiennej my_number
    (więcej o module random w dalszej częśći kursu).
    Zadeklaruj zmienną guess i przypisz jej wartość -1 (to wartość spoza zakresu losowanych liczb -
    czyli na pewno nie jest równa wylosowanej liczbie)
    Wyświetl instrukcję do gry - przynajmniej słowa "Guess my number!"
    Wykonuj pętlę while tak długo jak wartość w zmiennej guess jest różna od wartości my_number    
    poleceniem:
        guess = int(input())
    wczytaj odpowiedź użytkownika (uwaga program nie jest odporny na wprowadzenie w tym miejscu
    np. napisu zamiast liczby - o obsłudze błędów opowiadam w ostatnim module kursu)
    Sprawdź wartość liczby guess i
        jeżeli jest równa my_number, to wyświetl gratulacje
        w przeciwnym razie jeśli guess jest większe od my_number wyświetl
            "Sorry- my number is smaller than your guess, Try again!"
        w przeciwnym razie wyświetl
            "Sorry- my number is greater than your guess, Try again!"

    A teraz pobaw się kilka razy ;)
'''

print(task)

task = '''
3.  Do poprzedniego zadania dodaj zmienną trials, która będzie liczyć ilość prób. Początkowo powinna mieć wartość 0,
    a potem po każdej instrukcji wczytywania liczby guess ma być powiększana o 1.

    Wyświetlając gratulacja wyświetl też informacje za którym razem udało się odgadnąć liczbę
'''

print(task)
import random
my_number = random.randint(0, 20)
guess = -1
trials = 1
print('Guess my number!')
guess = int(input())
while guess != my_number:
    if guess > my_number:
        print("Try lower number!")
    else:
        print("Try higher number!")
    guess = int(input())
    trials += 1
print("Correct! My number was {0:d}! You've found it out after trying {1:d}".format(my_number, trials),
      "time!" if trials == 1 else "times!")