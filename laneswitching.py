from random import randint

N = 50
out = []
for i in range(N):
    out.append(randint(0, i))
print(*out)