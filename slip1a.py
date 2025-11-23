import numpy as np

def objective_function(x):
    # Define the objective function (in this case, f(x) = -x^2 + 4x)
    return -x**2 + 4*x

def hill_climbing(initial_x, step_size, max_iterations):
    current_x = initial_x
    
    for _ in range(max_iterations):
        current_value = objective_function(current_x)
        next_x = current_x + step_size
        next_value = objective_function(next_x)
        
        if next_value > current_value:
            current_x = next_x
        else:
            break
    
    return current_x, objective_function(current_x)

if __name__ == "__main__":
    # Set initial parameters
    initial_x = np.random.uniform(-10, 10)  # Initial random starting point
    step_size = 0.1
    max_iterations = 100
    
    # Run the hill climbing algorithm
    result_x, result_value = hill_climbing(initial_x, step_size, max_iterations)
    
    # Print the results
    print("Optimal x:", result_x)
    print("Optimal value:", result_value)
