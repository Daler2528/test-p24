n = int(input("Enter number:"))
primes = []
for i in range(2 ,n+1):
    isPrime = True
    for j in range(2,i):
        if i % j == 0:
            isPrime = False
    if isPrime:
        primes.append(i)
print(*primes)
