n, m = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))


def check(r):
    for city in cities: