import time
import random  # Importeer random
from array_data import array  # Importeer de array vanuit array_data.py

# Lineair zoeken
def linear_search(array, target):
    for element in array:
        if element == target:
            return True
    return False

# Random target selecteren om te zoeken
target = random.choice(array)

# Gebruik time.perf_counter() om de tijd te meten
start_time = time.perf_counter()
found = linear_search(array, target)
end_time = time.perf_counter()

# Resultaten
print(f"Lineair zoeken: {'Gevonden' if found else 'Niet gevonden'} in {end_time - start_time:.6f} seconden")
