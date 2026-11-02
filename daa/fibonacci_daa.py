
import time
import tracemalloc

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Non-Recursive Fibonacci
def fibonacci_nonrecursive(n):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


n = int(input("Enter number of terms: "))

# Non-Recursive Analysis
tracemalloc.start()
start = time.perf_counter()

result1 = fibonacci_nonrecursive(n)

time1 = time.perf_counter() - start
memory1 = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

# Recursive Analysis
tracemalloc.start()
start = time.perf_counter()

result2 = [fibonacci_recursive(i) for i in range(n)]

time2 = time.perf_counter() - start
memory2 = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

# Display Results
print("\nNon-Recursive Fibonacci:")
print(result1)
print("Execution Time:", time1, "seconds")
print("Memory Usage:", memory1 / 1024, "KB")

print("\nRecursive Fibonacci:")
print(result2)
print("Execution Time:", time2, "seconds")
print("Memory Usage:", memory2 / 1024, "KB")
