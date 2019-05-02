task = '''
Tym razem pomożemy lekarzom przeprowadzając wstępną analizę: czy pacjent ma grypę, czy tylko przeziębienie (zakładamy,
że pacjentowi coś dolega, w tym zadaniu mamy tylko pomóc zdiagnozować czy to jest grypa czy przeziębienie):

1.  Utwórz 3 zmienne

    -musclePain - wartość false
    -fever - wartość true
    -weakness - wartość true
'''

print(task)
musclePain = False
fever = True
weakness = True

task = '''2.  Napisz wyrażenie if, które

    -jeśli występuja wszystkie 3 objawy wyświetli komunikat "suspiction of influenza"
    -w przeciwnym razie wyświetli "The flu is unlikely"
'''

print(task)
print("suspiction of influenza" if musclePain and fever and weakness else "The flu is unlikely")

task = '''
3.  Napisz wyrażenie if, które:

    -jeśli występuja wszystkie 3 objawy wyświetli komunikat "suspiction of influenza"
    -jeśli wystęouje osłabienie (weakness) ale nie ma gorączki lub nie ma bólu mięśni to wyświetli "Just take a rest!"
    -w przeciwnym razie wyświetli "you may be cold"
'''

print(task)
if musclePain and fever and weakness:
    print("suspiction of influenza")
elif weakness and (not musclePain or not fever):
    print("Just take a rest!")
else:
    print("you may be cold")

task = '''
4.  Mężczyźni przeziębienie przechodzą jak grypę... dodaj zmienną isMan o wartości true
'''

print(task)
isMan = True

task = '''
5.  Napisz wyrażenie if, które:

    -komunikat o grypie wyświetli jeżeli występują wszystkie 3 objawy lub co najmniej jeden z nich o ile pacjent jest mężczyzną
    -w pozostałych przypadkach zachowanie ma być jak w  poprzednim przykładzie
'''

print(task)
if musclePain and fever and weakness or (isMan and (musclePain or fever or weakness)):
    print("suspiction of influenza")
elif weakness and (not musclePain or not fever):
    print("Just take a rest!")
else:
    print("you may be cold")

task = '''
6.  Zmieniamy temat. Pilot przed wystartowaniem powinien sprawdzić listę kontrolną. Właśnie piszesz kod, 
    który odpowiada za wyświetlenie napisu "CHECK IS COMPLETED" jeżeli lista kontrolna została już pomyślnie wykonana i
    zamknięta, w przeciwnym razie powinien być wyświetlany komunikat "CHECK NOT DONE YET!". Zmienna True/False,
    która zawiera informację o tym czy lista kontrolna została już wykonana nazywa sie isCheckCompleted.
    Korzystając z ternary operator przygotuj polecenie if wyświetlające odpowiedni komunikat.
'''

print(task)
isCheckCompleted = True
print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")