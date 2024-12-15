# 2 Write a Python file that asks for three numbers and outputs the largest and smallest.

a, b, c = map(int, input().split())

def max_min(a,b,c):
    return max(a,b,c), min(a,b,c)
print(max_min(a,b,c))