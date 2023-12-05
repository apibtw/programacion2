import random

estudiante = ["Franco", "Jorge", "Federico", "Sabrina", "Sofia"]

orden = random.sample(estudiante, len(estudiante))

print("Orden de exposición:")
for i, estudiante in enumerate(orden, start=1):
    print(str(i) + ". " + estudiante)
