---

# Lineair en Binair Zoeken in Python

Dit project bevat implementaties van **lineair** en **binair** zoeken in een gesorteerde array in Python. Beide zoekmethoden worden getest op een grote array van getallen met een range van 100.000.

## Bestanden

- **`array_data.py`**: Dit bestand genereert een array van getallen met een range van 100.000 en de andere code gebruikt dit.
- **`lineair.py`**: Bevat de implementatie van lineair zoeken. Het zoekt door de array van `array_data.py` en meet de tijd die het kost om een target te vinden.
- **`binair.py`**: Bevat de implementatie van binair zoeken. Het zoekt ook door dezelfde array en meet de tijd die het kost om een target te vinden.

## Hoe te gebruiken

1. **Clone of download** de repository.
2. Zorg ervoor dat je Python geïnstalleerd hebt.
3. Run **`array_data.py`** om een array te genereren (hoeft niet apart uitgevoerd te worden, de array wordt automatisch in de andere code gebruikt).
4. Run **`lineair.py`** om de lineaire code uit te voeren:
   ```bash
   python lineair.py
   ```
5. Run **`binair.py`** om de binaire code uit te voeren:
   ```bash
   python binair.py
   ```

## Voorbeeld Uitvoer

- **Lineair zoeken**:
  ```
  Lineair zoeken: Gevonden in 0.003456 seconden
  ```

- **Binair zoeken**:
  ```
  Binair zoeken: Gevonden in 0.000123 seconden
  ```

## Vereisten

- Python 3.x

---
