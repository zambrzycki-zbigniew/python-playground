task = '''
Dana jest lista:
    data = ['Error:File cannot be open',
            'Error:No free space on disk',
            'Error:File missing',
            'Warning:Internet connection lost',
            'Error:Access denied']

Napisz pętlę for, która wyświetli elementy tej listy jeden po drugim.
Podczas wyświetlania elementów konwertuj napisy do wielkich liter.
'''

print(task)
data = ['Error:File cannot be open',
            'Error:No free space on disk',
            'Error:File missing',
            'Warning:Internet connection lost',
            'Error:Access denied']
for dat in data:
    print(dat.upper())

task = '''ZADANIE 2
Jak widzisz, każdy z elementów listy zawiera znak ":".

    W pętli for każdy z przetwarzanych napisów rozbij ze względu na ":" korzystając z funkcji split.
    Wynik zapamiętaj w nowej dwuelementowej liście elements.
    Następnie wyświetl elements[0] konwertując napis do wielkich liter, a elements[1] wyświetl bez żadnej konwersji
'''

print(task)
elements = []
for dat in data:
    elements.append(dat.split(":"))
for element in elements:
    print(element[0].upper(), element[1])

task = '''ZADANIE 3
Rozpocznij od poprzednio utworzonej pętli. Zmieniamy zasady wyświetlania:
Jeżeli w elements[0] znajduje się napis "Error", wyświetl elements[1] konwertując tekst do wielkich liter
w przeciwnym razie wyświetl elements[1] bez żadnej konwersji
'''

print(task)
for element in elements:
    print(element[0].upper(), element[1].upper() if element[0] == "Error" else element[1])