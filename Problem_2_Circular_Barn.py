import sys
T = int(input())

n = 5 * (10**6) + 1
primes = [True] * n
primes[0], primes[1] = False, False
for i in range(n):
    if primes[i]:
        for j in range(2 * i, n, i):
            primes[j] = False


def closest_prime(k):
    for index in range(k - 4, -1, -4):
        if primes[index]:
            return (k - index) // 4


for a in range(T):
    N = int(input())
    barn = list(map(int, input().split()))
    min_nohj = (sys.maxsize, sys.maxsize)
    min_john = (sys.maxsize, sys.maxsize)
    found = False
    for i in range(N):
        curr = barn[i]
        curr_m = curr % 4
        curr_c = curr // 4
        if primes[curr] or curr == 1:
            print("Farmer John")
            found = True
            break
        elif curr_m == 0:
            min_nohj = min(min_nohj, (curr_c + 1, i), key=lambda element: (element[0], element[1]))
        elif curr_m == 2:
            min_john = min(min_john, (curr_c + 1, i), key=lambda element: (element[0], element[1]))
        else:
            min_john = min(min_john, (closest_prime(curr) + 1, i))
    if found:
        continue
    if min_john[0] < min_nohj[0]:
        print("Farmer John")
    elif min_nohj[0] < min_john[0]:
        print("Farmer Nhoj")
    else:
        temp = "Farmer John" if min_john[1] < min_nohj[1] else "Farmer Nhoj"
        print(temp)
