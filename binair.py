import time
import random  # Importeer random
from array_data import array  # Importeer de array vanuit array_data.py
# Binair zoeken
def binary_search(array, target, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, low, mid - 1)
    else:
        return binary_search(array, target, mid + 1, high)

# Random target selecteren om te zoeken
target = random.choice(array)

# Gebruik time.perf_counter() om de tijd te meten
start_time = time.perf_counter()
found = binary_search(array, target, 0, len(array) - 1)
end_time = time.perf_counter()

# Resultaten
print(f"Binair zoeken: {'Gevonden' if found else 'Niet gevonden'} in {end_time - start_time:.6f} seconden")
