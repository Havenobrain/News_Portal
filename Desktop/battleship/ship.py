class Ship:
    def __init__(self, coordinates):
        self.coordinates = coordinates  
        self.hits = set()  
    
    def is_sunk(self):
        return set(self.coordinates) == self.hits
    
    def hit(self, coord):
        if coord in self.coordinates:
            self.hits.add(coord)
            return True
        return False
