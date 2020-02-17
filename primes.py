# Ian McLoughlin
# Computing the primes.
import math

def isprime(i):
  # Loop through all values j from 2 up to but not including i.
  for j in range(2, math.floor(math.sqrt(i))):
    # See if j divides i.
    if i % j == 0:
      # If it does, i isn't prime so exit the loop and indicate it's not prime.
      return False
  return True


# My list of primes - TBD.
P = []

# Loop through all of the numbers we're checking for primality. 
for i in range(2, 100000):
  # If i is prime, then append to P.
  if isprime(i):
    P.append(i)

# Print out our list.
print(P)
  
