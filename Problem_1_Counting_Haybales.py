import bisect
import sys, os.path
if(os.path.exists('haybales.in')):
    sys.stdin = open("haybales.in", "r")
    sys.stdout = open("haybales.out", "w")


N, Q = map(int, input().split())
locations = sorted(list(map(int, input().split())))
queries = [list(map(int, input().split())) for _ in range(Q)]

for i in queries:
    a, b = bisect.bisect_left(locations, i[0]), bisect.bisect_right(locations, i[1])
    print(b - a)
