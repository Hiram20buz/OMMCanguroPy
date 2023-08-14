class FlowerDictionary:
    def __init__(self):
        self.flores = {
            "Flor1": "azul",
            "Flor2": "verde",
            "Flor3": "roja",
            "Flor4": "amarilla",
        }
        self.keys = list(self.flores.values())
    
    def position(self, n):
        m = int(n) % 4
        return self.keys[m - 1]

# Create an instance of the FlowerDictionary class
flower_dict = FlowerDictionary()

# Get input for nth flower
n = input("nth flower: ")

# Call the position method and print the result
print(flower_dict.position(n))

