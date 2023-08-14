flores = {
    "Flor1": "azul",
    "Flor2": "verde",
    "Flor3": "roja",
    "Flor4": "amarilla",
}

n=input("nth flower: ")
keys = list(flores.values())

def position(n):
    m = int(n)%4
    return keys[m-1]
    
print(position(n))
