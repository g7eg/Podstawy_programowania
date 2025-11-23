import sys
import os
import pytest

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from l10.l10_z6 import (
        srednia_wydajnosc,
        maksymalna_wydajnosc,
        minimalna_wydajnosc,
        odchylenie_standardowe,
        srednia_wydajnosc_wbudowana,
        maksymalna_wydajnosc_wbudowana,
        minimalna_wydajnosc_wbudowana,
        odchylenie_standardowe_wbudowana,
        wydajnosci
    )
except ImportError:
    srednia_wydajnosc = maksymalna_wydajnosc = minimalna_wydajnosc = \
    odchylenie_standardowe = \
    srednia_wydajnosc_wbudowana = maksymalna_wydajnosc_wbudowana = minimalna_wydajnosc_wbudowana = \
    odchylenie_standardowe_wbudowana = \
    wydajnosci = None

    lista_zmiennych_do_sprawdzenia = (
        srednia_wydajnosc,
        maksymalna_wydajnosc,
        minimalna_wydajnosc,
        odchylenie_standardowe,
        srednia_wydajnosc_wbudowana,
        maksymalna_wydajnosc_wbudowana,
        minimalna_wydajnosc_wbudowana,
        odchylenie_standardowe_wbudowana,
        wydajnosci
    )

# Testy funkcji bez wbudowanych funkcji
@pytest.mark.skipif(
    # Używamy any() do sprawdzenia, czy jakikolwiek element z tupli jest None
    any(zmienna is None for zmienna in lista_zmiennych_do_sprawdzenia), 
    reason="Brak niezbędnych wyników (przynajmniej jedna zmienna ma wartość None).")
def test_srednia_wydajnosc():
    assert srednia_wydajnosc(wydajnosci) == 142

@pytest.mark.skipif(
    # Używamy any() do sprawdzenia, czy jakikolwiek element z tupli jest None
    any(zmienna is None for zmienna in lista_zmiennych_do_sprawdzenia), 
    reason="Brak niezbędnych wyników (przynajmniej jedna zmienna ma wartość None).")
def test_maksymalna_wydajnosc():
    assert maksymalna_wydajnosc(wydajnosci) == 170

@pytest.mark.skipif(
    # Używamy any() do sprawdzenia, czy jakikolwiek element z tupli jest None
    any(zmienna is None for zmienna in lista_zmiennych_do_sprawdzenia), 
    reason="Brak niezbędnych wyników (przynajmniej jedna zmienna ma wartość None).")
def test_minimalna_wydajnosc():
    assert minimalna_wydajnosc(wydajnosci) == 120

@pytest.mark.skipif(
    # Używamy any() do sprawdzenia, czy jakikolwiek element z tupli jest None
    any(zmienna is None for zmienna in lista_zmiennych_do_sprawdzenia), 
    reason="Brak niezbędnych wyników (przynajmniej jedna zmienna ma wartość None).")
def test_odchylenie_standardowe():
    assert round(odchylenie_standardowe(wydajnosci), 2) == 17.2

# Testy funkcji z wbudowanymi funkcjami
@pytest.mark.skipif(
    # Używamy any() do sprawdzenia, czy jakikolwiek element z tupli jest None
    any(zmienna is None for zmienna in lista_zmiennych_do_sprawdzenia), 
    reason="Brak niezbędnych wyników (przynajmniej jedna zmienna ma wartość None).")
def test_srednia_wydajnosc_wbudowana():
    assert srednia_wydajnosc_wbudowana(wydajnosci) == 142

@pytest.mark.skipif(
    # Używamy any() do sprawdzenia, czy jakikolwiek element z tupli jest None
    any(zmienna is None for zmienna in lista_zmiennych_do_sprawdzenia), 
    reason="Brak niezbędnych wyników (przynajmniej jedna zmienna ma wartość None).")
def test_maksymalna_wydajnosc_wbudowana():
    assert maksymalna_wydajnosc_wbudowana(wydajnosci) == 170

@pytest.mark.skipif(
    # Używamy any() do sprawdzenia, czy jakikolwiek element z tupli jest None
    any(zmienna is None for zmienna in lista_zmiennych_do_sprawdzenia), 
    reason="Brak niezbędnych wyników (przynajmniej jedna zmienna ma wartość None).")
def test_minimalna_wydajnosc_wbudowana():
    assert minimalna_wydajnosc_wbudowana(wydajnosci) == 120

@pytest.mark.skipif(
    # Używamy any() do sprawdzenia, czy jakikolwiek element z tupli jest None
    any(zmienna is None for zmienna in lista_zmiennych_do_sprawdzenia), 
    reason="Brak niezbędnych wyników (przynajmniej jedna zmienna ma wartość None).")
def test_odchylenie_standardowe_wbudowana():
    assert round(odchylenie_standardowe_wbudowana(wydajnosci), 2) == 17.2
