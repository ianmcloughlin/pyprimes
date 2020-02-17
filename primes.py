# Ian McLoughlin
# Computing the primes.
from functions import isprime

# My list of primes - TBD.
P = []

# Loop through all of the numbers we're checking for primality. 
for i in range(2, 100000):
  # If i is prime, then append to P.
  if isprime(i):
    P.append(i)

# Print out our list.
print(P)
  
