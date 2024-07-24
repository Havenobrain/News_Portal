import random
from ship import Ship

class Board:
    def __init__(self, ships):
        self.ships = ships
        self.hits = set()
        self.misses = set()
    
    def display(self):
        grid = [["O" for _ in range(8)] for _ in range(8)]
        for ship in self.ships:
            for x, y in ship.coordinates:
                grid[x][y] = "■"
        for x, y in self.hits:
            grid[x][y] = "X"
        for x, y in self.misses:
            grid[x][y] = "T"
        
        print("  1 2 3 4 5 6 7 8")
        for i, row in enumerate(grid):
            print(f"{i+1} {' '.join(row)}")
    
    def display_opponent_view(self):
        grid = [["O" for _ in range(8)] for _ in range(8)]
        for x, y in self.hits:
            grid[x][y] = "X"
        for x, y in self.misses:
            grid[x][y] = "T"
        
        print("  1 2 3 4 5 6 7 8")
        for i, row in enumerate(grid):
            print(f"{i+1} {' '.join(row)}")
    
    def take_shot(self, coord):
        if coord in self.hits or coord in self.misses:
            raise ValueError("This cell has already been shot at.")
        
        for ship in self.ships:
            if ship.hit(coord):
                self.hits.add(coord)
                return "hit"
        self.misses.add(coord)
        return "miss"
    
    def is_all_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)
