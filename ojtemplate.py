import sys, os.path
if(os.path.exists('filename.in')):
    sys.stdin = open("filename.in", "r")
    sys.stdout = open("filename.out", "w")
