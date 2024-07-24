import random
from ship import Ship

def place_ships():
    ships = []
    max_attempts = 10000  # Максимальное количество попыток

    def is_valid_position(new_ship, ships):
        for ship in ships:
            for x, y in ship.coordinates:
                for nx, ny in new_ship:
                    if abs(x - nx) <= 1 and abs(y - ny) <= 1:
                        return False
        return True

    ship_lengths = [3, 2, 2, 1, 1, 1, 1, 1]  # Длины кораблей

    for length in ship_lengths:
        placed = False
        for attempt in range(max_attempts):
            direction = random.choice(["H", "V"])
            if direction == "H":
                x, y = random.randint(0, 7), random.randint(0, 7 - length + 1)
                new_ship = [(x, y + i) for i in range(length)]
            else:
                x, y = random.randint(0, 7 - length + 1), random.randint(0, 7)
                new_ship = [(x + i, y) for i in range(length)]
            
            if all(0 <= cx < 8 and 0 <= cy < 8 for cx, cy in new_ship) and is_valid_position(new_ship, ships):
                ships.append(Ship(new_ship))
                print(f"Корабль добавлен: {new_ship}")
                placed = True
                break
        if not placed:
            raise RuntimeError(f"Не удалось разместить корабль длиной {length}. Попробуйте еще раз.")
    
    return ships

def random_shot(board):
    while True:
        shot = (random.randint(0, 7), random.randint(0, 7))
        if shot not in board.hits and shot not in board.misses:
            return shot
