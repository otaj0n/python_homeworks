# Write a Python program to:

# Take a string input from the user.
# Print the length of the string.
# Convert the string to uppercase and lowercase.

def user(l)->str:
    lenght = len(l)
    u = l.upper()
    low = l.lower()
    return lenght, u, low
l = input()
print(user(l))