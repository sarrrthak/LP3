# Job Sequencing with Deadlines using Greedy Method

# Input number of jobs
n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    job_id = input(f"Enter Job ID (e.g., J{i+1}): ")
    deadline = int(input(f"Enter deadline for {job_id}: "))
    profit = int(input(f"Enter profit for {job_id}: "))
    
    jobs.append((job_id, deadline, profit))

# Sort jobs by profit in descending order (Greedy Choice)
jobs.sort(key=lambda x: x[2], reverse=True)

# Find the maximum deadline to set the size of our time slots
max_deadline = 0
for job in jobs:
    if job[1] > max_deadline:
        max_deadline = job[1]

# Array to keep track of free time slots (-1 means empty)
time_slots = [-1] * max_deadline
total_profit = 0
job_sequence = []

# Greedy selection
for i in range(n):
    job_id = jobs[i][0]
    deadline = jobs[i][1]
    profit = jobs[i][2]

    # Try to place the job in the latest possible free slot before its deadline
    # We use min(max_deadline, deadline) to avoid index out of bounds
    for j in range(min(max_deadline, deadline) - 1, -1, -1):
        if time_slots[j] == -1:
            time_slots[j] = job_id
            total_profit += profit
            job_sequence.append(job_id)
            break

# Display results
print("\nJob Sequence for Maximum Profit:")
for slot in time_slots:
    if slot != -1:
        print(slot, end=" ")

print(f"\n\nTotal Maximum Profit: {total_profit}")