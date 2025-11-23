from itertools import permutations

solutions = []
for G, O, T, U in permutations(range(10), 4):
    # leading letters cannot be zero
    if G == 0 or T == 0 or O == 0:
        continue
    GO = 10 * G + O
    TO = 10 * T + O
    OUT = 100 * O + 10 * U + T
    if GO + TO == OUT:
        solutions.append((G, O, T, U, GO, TO, OUT))

for G, O, T, U, GO, TO, OUT in solutions:
    print(f"G={G} O={O} T={T} U={U} -> {GO} + {TO} = {OUT}")

print(f"Total solutions: {len(solutions)}")