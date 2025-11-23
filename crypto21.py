from itertools import permutations
def solve_cryptarithmetic(equation):
    unique_letters = set("".join(equation))
    if len(unique_letters) > 10:
        return "Invalid equation: More than 10 unique letters."

    for perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        if sum(mapping[letter] * 10**i for i, letter in enumerate(equation[0][::-1])) + \
           sum(mapping[letter] * 10**i for i, letter in enumerate(equation[1][::-1])) == \
           sum(mapping[letter] * 10**i for i, letter in enumerate(equation[2][::-1])):
            return {letter: mapping[letter] for letter in unique_letters}

    return "No solution found."

if __name__ == "__main__":
    equation = ["GO", "TO", "OUT"]
    solution = solve_cryptarithmetic(equation)
    
    if isinstance(solution, dict):
        print("Solution found:")
        for letter, value in solution.items():
            print(f"{letter}: {value}")
    else:
        print(solution)
