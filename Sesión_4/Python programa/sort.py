import random
score = random.sample(range(1000), 1000)

print(f"Lista de números: {score}")

score.sort()
print(f"\nLista números: {score}")