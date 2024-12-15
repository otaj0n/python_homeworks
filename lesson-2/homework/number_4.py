# 4 Write a program that takes two numbers and prints out the result of integer division and the remainder.

a, b = map(int, input().split())

def div(a,b):
    c = a//b
    f = a%b
    return {
        "Integer divisin": c , 
        "Remainder": f
        }
print(div(a,b))