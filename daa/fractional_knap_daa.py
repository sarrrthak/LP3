# Fractional Knapsack using Greedy Method

# Input number of items
n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight = int(input("Enter weight of item: "))
    value = int(input("Enter value of item: "))

    ratio = value / weight
    items.append((weight, value, ratio))

# Input knapsack capacity
capacity = int(input("Enter knapsack capacity: "))

# Sort items by value/weight ratio
items.sort(key=lambda x: x[2], reverse=True)

total_value = 0

# Greedy selection
for weight, value, ratio in items:

    if capacity >= weight:
        total_value += value
        capacity -= weight

    else:
        total_value += ratio * capacity
        break

# Display result
print("\nMaximum value in Knapsack:", total_value)