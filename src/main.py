from collections import Counter

with open("data/input.txt", "r") as f:
    text = f.read()

words = text.split()

print("Word count:", len(words))

freq = Counter(words)
print(freq)