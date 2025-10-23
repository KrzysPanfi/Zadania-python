# =====================================================
#               ZADANIA PYTHON – PĘTLE I LOSOWANIE
# =====================================================
import random

# ------------------------------
# Zadanie 1 – Ciasteczko z wróżbą
# ------------------------------
# Napisz program, który losowo wybiera jedną przepowiednię spośród pięciu
# i wyświetla ją na ekranie.
# Stwórz listę przepowiedni i użyj funkcji losowej.
liczbazad = int(input("Podaj numer zadania"))
# Tu wpisz swój kod
if liczbazad == 1:
    list = ["Będziesz mial wypadek", "wygrasz milion", "wygrasz tysiąć", "wygrasz stówe", "nic nie wygrasz"]
    a = random.choice(list)
    print(a)

# ------------------------------
# Zadanie 2 – Rzut monetą
# ------------------------------
# Napisz program, który symuluje 100 rzutów monetą.
# Moneta ma dwie strony: "orzeł" i "reszka".
# Policz, ile razy wypadł orzeł, a ile reszka.
# Wyświetl wyniki.

# Tu wpisz swój kod
if liczbazad == 2:
    moneta = ""
    liczba_orzel = 0
    liczba_reszka = 0
    for i in range(100):
        a = random.randint(1, 2)
        if a == 1:
            moneta = "reszka"
            liczba_reszka = liczba_reszka + 1
        elif a == 2:
            moneta = "orzeł"
            liczba_orzel = liczba_orzel + 1

    print("liczba orzel:", liczba_orzel)
    print("liczba reszka:", liczba_reszka)
# ------------------------------
# Zadanie 3 – Gra „zgadnij liczbę”
# ------------------------------
# Napisz program, w którym użytkownik próbuje odgadnąć liczbę z zakresu 1–100.
# Komputer losuje liczbę.
# Użytkownik ma ograniczoną liczbę prób (np. 7).
# Po każdej próbie program informuje, czy liczba jest za mała, za duża, czy trafiona.
# Jeśli użytkownik nie zgadnie w wyznaczonej liczbie prób, wyświetl odpowiedni komunikat.

# Tu wpisz swój kod
if liczbazad == 3:
    cel = random.randint(1, 100)
    intput = 0
    proby = 0
    while not cel == intput:
        intput = int(input("Podaj liczbę"))
        if intput == cel:
            print("Trafiłeś")
        elif intput > cel:
            proby = proby + 1
            print("Za duża liczba")
        elif intput < cel:
            proby = proby + 1
            print("Za mała liczba")
        if proby > 6:
            print("Za duzo prób")
            break
# ------------------------------
# Zadanie 4 – Duży lotek
# ------------------------------
# Napisz program symulujący loterię 6/49.
# Użytkownik wybiera 6 liczb, komputer losuje 6 liczb.
# Porównaj liczby użytkownika z wylosowanymi przez komputer.
# Wyświetl wszystkie liczby i liczbę trafień.

# Tu wpisz swój kod
if liczbazad == 4:
    liczbatraf = 0
    listalos = list()
    listainput = list()
    for i in range(6):
        a = random.randint(1, 49)
        listalos.append(a)
    print("lista wylosowanych" + str(listalos))
    for i in range(6):
        a = int(input("Podaj cyfrę 1-49"))
        if a > 0 and a < 50:
            listainput.append(a)
        else:
            print("liczby mają być od 1-49")
    for i in listalos:
        for j in listainput:
            if i == j:
                liczbatraf = liczbatraf + 1
    print("Liczba trafionych " + str(liczbatraf))
    print("lista wylosowanych " + str(listalos))
    print("lista wybranych " + str(listainput))
# =====================================================
#             ZADANIA PYTHON – LISTY I KROTKI
# =====================================================

# ------------------------------
# Zadanie 5 – Zmiana elementu listy
# ------------------------------
# Dana jest lista 'imiona' z 4 imionami.
# Użytkownik podaje stare imię i nowe imię.
# Program powinien użyć metody index() do zamiany starego imienia na nowe.


# Tu wpisz swój kod
if liczbazad == 5:
    listaimienia = ["patryk", "michal", "jeremi", "zbigniew"]
    noweimie = str(input("Podaj nowe imie"))
    stareimie = str(input("Podaj  stare imie"))
    staryindex = listaimienia.index(stareimie)
    listaimienia[staryindex] = noweimie
    print(listaimienia)
# ------------------------------
# Zadanie 6 – Sortowanie listy
# ------------------------------
# Dana jest lista 'imiona' z 4 imionami.
# Posortuj listę alfabetycznie używając metody sort().
# Wyświetl wynik.

# Tu wpisz swój kod
if liczbazad == 6:
    listaimienia = ["patryk", "michal", "jeremi", "zbigniew"]
    listaimienia.sort()
    print(listaimienia)

# ------------------------------
# Zadanie 7 – Usuwanie elementu listy
# ------------------------------
# Dana jest lista 'imiona' z 4 imionami.
# Użytkownik podaje imię, które chce usunąć.
# Program powinien usunąć element używając metody remove().
# Wyświetl wynikową listę.

# Tu wpisz swój kod

if liczbazad == 7:
    listaimienia = ["patryk", "michal", "jeremi", "zbigniew"]
    stareimie = str(input("Podaj  stare imie"))
    listaimienia.remove(stareimie)
    print(listaimienia)
# ------------------------------
# Zadanie 8 – Sortowanie krotki
# ------------------------------
# Dana jest krotka 'imiona = ('Jakub', 'Bartosz', 'Max', 'Filip')'.
# Napisz program, który tworzy nową posortowaną listę na podstawie krotki.
# Wyświetl wynik.

# Tu wpisz swój kod


# ------------------------------
# Zadanie 9 – Suma elementów krotki
# ------------------------------
# Dana jest krotka 'krotka = (1, 2, 3, 4, 5)'.
# Oblicz sumę wszystkich elementów krotki i wyświetl wynik.

# Tu wpisz swój kod


# ------------------------------
# Zadanie 10 – Kieszeń (krotki)
# ------------------------------
# Dana jest krotka 'pocket = ('pen', 'pencil', 'keys')'.
# Sprawdź, czy w kieszonce są klucze i wyświetl odpowiedni komunikat.
# Wyświetl liczbę przedmiotów i dwa ostatnie elementy.
# Zdefiniuj nową krotkę 'add = ('coins',)' i spróbuj dodać ją do istniejącej.
# Umieść wszystkie elementy i dwa dodatkowe w większej kieszonce i wyświetl wynik.

# Tu wpisz swój kod


# ------------------------------
# Zadanie 11 – Porównanie dwóch list
# ------------------------------
# Stwórz dwie listy 'a' i 'b', każda po 3 liczby.
# Porównaj elementy list: sprawdź, czy elementy listy 'a' są większe od odpowiadających elementów listy 'b'.
# Wyniki zapisz w nowej liście 'greater' i wyświetl ją.
