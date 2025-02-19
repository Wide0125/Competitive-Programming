n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))


def check(r):
    tower = 0
    for city in cities:
        