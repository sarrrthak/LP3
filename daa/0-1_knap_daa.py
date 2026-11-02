# 0-1 Knapsack using Dynamic Programming

# Input number of items
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    w = int(input("Enter weight of item: "))
    v = int(input("Enter value of item: "))

    weights.append(w)
    values.append(v)

# Input knapsack capacity
capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

# Dynamic Programming
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Display maximum value
print("\nMaximum value in Knapsack:", dp[n][capacity])

# Display selected items
print("Selected Items:")

w = capacity
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        print("Item", i)
        w -= weights[i - 1]