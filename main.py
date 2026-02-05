# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Aayan Khan
# Date:04-02-2026

print("--- Factorial Finder ---\n")


# Write your code here
n = int(input("Enter Number: "))
if n < 0:
    print(f"Factorial of {abs(n)} is Not Defined")
else:
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f"Factorial of {n} is {f}")

