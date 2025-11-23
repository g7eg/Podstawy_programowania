import sys
import os
import pytest

# Dodaj ścieżkę do katalogu głównego projektu
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try: 
    from l10.l10_z1 import kelvin_na_celsiusz
except ImportError:
    kelvin_na_celsiusz = None
    
@pytest.mark.skipif(kelvin_na_celsiusz is None, reason="Brak funkcji 'kelvin_na_celsiusz' do zaimportowania.")
def test_kelvin_na_celsiusz():
    assert kelvin_na_celsiusz(0) == -273.15
    assert kelvin_na_celsiusz(273.15) == 0
    assert kelvin_na_celsiusz(373.15) == 100
    assert kelvin_na_celsiusz(1000) == 726.85
    assert kelvin_na_celsiusz(-1) == None

if __name__ == "__main__":
    pytest.main()
