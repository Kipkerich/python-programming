def prime_check(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    prime_result = prime_check(n)
    if prime_result:
        print("Prime")
    else:
        print("Not prime")

    
