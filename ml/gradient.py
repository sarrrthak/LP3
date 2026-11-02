# Gradient Descent Algorithm to find Local Minima

# Define the function
def f(x):
    return (x + 3) ** 2

# Define the derivative
def derivative(x):
    return 2 * (x + 3)

# Initial values
x = 2
learning_rate = 0.1
iterations = 100

# Gradient Descent
for i in range(iterations):
    x = x - learning_rate * derivative(x)

# Display Result
print("Local Minima of the function:")
print("x =", round(x, 4))
print("y =", round(f(x), 4))