liczby = [1, 3, 4, 2, 3, 5, 4]
litery = ['komarnica', 'pszczoła', 'mucha domowa', 'żuk gnojowy', 'e', 'f', 'g']

# tworzenie listy krotek (liczba, litera)
krotki = list(zip(liczby, litery))

# sortowanie listy krotek wg pierwszego elementu
krotki_posortowane = sorted(krotki, key=lambda x: x[0])

# wyświetlanie wyniku
for krotka in krotki_posortowane:
    print(krotka[1], krotka[0])
