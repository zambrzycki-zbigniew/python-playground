task = '''
Nadal analizujesz wydajność kanałów, jakimi można dotrzeć do klientów.
Każdorazowo po zmienie słownika wyświetl jego zawartość

1.  Utwórz obiekt dictionary o nazwie channels z następującymi kluczami i wartościami:

    -Google - 1480
    -Email - 300
    -Natural Traffic - 440
    -TV Spot - 700
'''

print(task)
channels = {"Google": 1480, "Email": 300, "Natural Traffic": 440, "TV Spot": 700}
print(channels)

task = '''
2.  Wyświetl wartość skojarzoną z kluczem "Email"
'''

print(task)
print(channels["Email"])

task = '''
3.  Utwórz nowy słownik channelsUpdate z kluczami i wartościami:

    -Natural Traffic -  520
    -News - 600
'''

print(task)
channelsUpdate = {"Natural Traffic": 520, "News": 600}
print(channelsUpdate)

task = '''
4.  Zaktualizuj słownik chanels wartościami z channelsUpdate
'''

print(task)
channels.update(channelsUpdate)
print(channels)
print(channelsUpdate)

task = '''
5.  Wyświetl wszystkie klucze z channels
'''


print(task)
print(channels.keys())

task = '''
6.  Usuń wartość 'Email' ze słownika
'''


print(task)
print(channels.pop("Email"))
print(channels)