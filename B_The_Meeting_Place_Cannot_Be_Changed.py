n = int(input())
locations = list(map(int, input().split()))
speeds = list(map(int, input().split()))


def check(meeting_place):
    for i in locations:
        if 