import sys
import os
import pytest

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from l10.l10_z5 import dodaj_wielomiany, odejmij_wielomiany, pomnoz_wielomiany
except ImportError:
    dodaj_wielomiany = None
    odejmij_wielomiany = None
    pomnoz_wielomiany = None

@pytest.mark.skipif(dodaj_wielomiany is None or odejmij_wielomiany is None or pomnoz_wielomiany is None, reason="Brak funkcji 'dodaj_wielomiany' lub/i 'odejmij_wielomiany' i/lub 'pomnoz_wielomiany' do zaimportowania.")
def test_dodaj_wielomiany():
    assert dodaj_wielomiany([2, -3, 0, 4], [1, 5, 2]) == [2, -2, 5, 6]
    assert dodaj_wielomiany([1], [1, 2, 3]) == [1, 2, 4]
    
@pytest.mark.skipif(dodaj_wielomiany is None or odejmij_wielomiany is None or pomnoz_wielomiany is None, reason="Brak funkcji 'dodaj_wielomiany' lub/i 'odejmij_wielomiany' i/lub 'pomnoz_wielomiany' do zaimportowania.")
def test_odejmij_wielomiany():
    assert odejmij_wielomiany([2, -3, 0, 4], [1, 5, 2]) == [2, -4, -5, 2]
    assert odejmij_wielomiany([1], [1, 2, 3]) == [-1, -2, -2]

@pytest.mark.skipif(dodaj_wielomiany is None or odejmij_wielomiany is None or pomnoz_wielomiany is None, reason="Brak funkcji 'dodaj_wielomiany' lub/i 'odejmij_wielomiany' i/lub 'pomnoz_wielomiany' do zaimportowania.")
def test_pomnoz_wielomiany():
    assert pomnoz_wielomiany([2, -3, 0, 4], [1, 5, 2]) == [2, 7, -11, -2, 20, 8]
    assert pomnoz_wielomiany([1, 2], [3, 4]) == [3, 10, 8]