import sys
import os
import pytest
from io import StringIO
from contextlib import redirect_stdout

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from l11.l11_z6 import Ksiazka, dodaj_ksiazke, wypisz_ksiazki
except ImportError:
    Ksiazka = None
    dodaj_ksiazke = None
    wypisz_ksiazki = None

@pytest.mark.skipif(Ksiazka is None or dodaj_ksiazke is None or wypisz_ksiazki is None, reason="Brak klasy 'Ksiazka' lub/i 'dodaj_ksiazke' i/lub 'wypisz_ksiazki' do zaimportowania.")
def test_ksiazka_str():
    ksiazka = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 1834)
    assert str(ksiazka) == "'Pan Tadeusz' - Adam Mickiewicz (1834)"

@pytest.mark.skipif(Ksiazka is None or dodaj_ksiazke is None or wypisz_ksiazki is None, reason="Brak klasy 'Ksiazka' lub/i 'dodaj_ksiazke' i/lub 'wypisz_ksiazki' do zaimportowania.")
def test_dodaj_ksiazke():
    lista_ksiazek = []
    dodaj_ksiazke(lista_ksiazek, "Dziady", "Adam Mickiewicz", 1823)
    assert len(lista_ksiazek) == 1
    assert lista_ksiazek[0].tytul == "Dziady"
    assert lista_ksiazek[0].autor == "Adam Mickiewicz"
    assert lista_ksiazek[0].rok_wydania == 1823

@pytest.mark.skipif(Ksiazka is None or dodaj_ksiazke is None or wypisz_ksiazki is None, reason="Brak klasy 'Ksiazka' lub/i 'dodaj_ksiazke' i/lub 'wypisz_ksiazki' do zaimportowania.")
def test_wypisz_ksiazki():
    lista_ksiazek = [
        Ksiazka("Quo Vadis", "Henryk Sienkiewicz", 1896),
        Ksiazka("Lalka", "Bolesław Prus", 1890)
    ]
    
    expected_output = ("Lista książek:\n"
                       "'Quo Vadis' - Henryk Sienkiewicz (1896)\n"
                       "'Lalka' - Bolesław Prus (1890)\n")
    
    f = StringIO()
    with redirect_stdout(f):
        wypisz_ksiazki(lista_ksiazek)
    output = f.getvalue()
    
    assert output == expected_output

@pytest.mark.skipif(Ksiazka is None or dodaj_ksiazke is None or wypisz_ksiazki is None, reason="Brak klasy 'Ksiazka' lub/i 'dodaj_ksiazke' i/lub 'wypisz_ksiazki' do zaimportowania.")
def test_wypisz_ksiazki_pusta_lista():
    lista_ksiazek = []
    
    expected_output = "Lista książek jest pusta.\n"
    
    f = StringIO()
    with redirect_stdout(f):
        wypisz_ksiazki(lista_ksiazek)
    output = f.getvalue()
    
    assert output == expected_output
