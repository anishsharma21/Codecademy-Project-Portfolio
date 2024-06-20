count = 0
def sieve(n):
    global count
    primes = [[i, True] for i in range(n+1) if i > 1]
    idx_prime, idx_compare = 0, 1
    while idx_prime != len(primes)-1:
        count += 1
        if primes[idx_compare][0] % primes[idx_prime][0] == 0:
            primes[idx_compare][1] = False
        if idx_compare == len(primes) - 1:
            idx_prime += 1
            idx_compare = idx_prime + 1
        else:
            idx_compare += 1
    return [prime[0] for prime in primes if prime[1] == True]

print(sieve(20))
print(count)

def sieve_better(n):
    global count
    primes = [i for i in range(n+1) if i > 1]
    idx_prime, idx_compare = 0, 1
    while idx_prime != len(primes)-1:
        count += 1
        if primes[idx_compare] % primes[idx_prime] == 0:
            primes.pop(idx_compare)
            if idx_compare == len(primes) - 1:
                continue
        if idx_compare >= len(primes) - 1:
            idx_prime += 1
            idx_compare = idx_prime + 1
        else:
            idx_compare += 1
    return primes

# not really better because pop causes unshifting and shifting, the dictionary version is actually better because its basically like using a hashmap, which has O(1) runtime
count = 0
print(sieve_better(20))
print(count)