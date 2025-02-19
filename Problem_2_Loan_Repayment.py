import sys, os.path
if(os.path.exists("loan.in")):
    sys.stdin = open("loan.in", "r")
    sys.stdout = open("loan.out", "w")

N, K, M = map(int, input().split())


def check(X):
    k = K
    g = 0
    while k > 0 and g < N:
        Y = int((N - g) / X)
        if Y < M:
            return (N - g) / (k) <= M
        samedays = min(K - 1, max(1, -(((N - g) % X) // -Y)))
        k -= samedays
        g += Y * samedays
    return g >= N


left = 1
right = N
while left < right:
    mid = (left + right + 1) // 2
    if check(mid):
        left = mid
    else:
        right = mid - 1
print(left)
