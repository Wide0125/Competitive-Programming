import sys, os.path
if(os.path.exists('revegetate.in')):
    sys.stdin = open("revegetate.in", "r")
    sys.stdout = open("revegetate.out", "w")

