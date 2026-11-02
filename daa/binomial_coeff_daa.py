# Binomial Coefficient using Dynamic Programming

def binomial_coefficient(n, k):
    # Create a 2D DP table initialized to 0
    dp = [[0 for j in range(k + 1)] for i in range(n + 1)]

    # Fill the DP table in a bottom-up manner
    for i in range(n + 1):
        # j goes up to min(i, k) because k cannot be greater than n
        for j in range(min(i, k) + 1):
            
            # Base cases: C(i, 0) = 1 and C(i, i) = 1
            if j == 0 or j == i:
                dp[i][j] = 1
            
            # State transition: C(n, k) = C(n-1, k-1) + C(n-1, k)
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]

# Input n and k
n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))

# Validation
if k > n or k < 0:
    print("Invalid input: k cannot be negative or greater than n.")
else:
    result = binomial_coefficient(n, k)
    print(f"\nBinomial Coefficient C({n}, {k}) is: {result}")