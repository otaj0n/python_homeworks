def palindrome(l):
    h = len(l)
    if h%2 != 0:
        if l[:h//2]==l[-1:h//2:-1]:
            return True
        else:
            return False
    else:
        return False
l = input()

print(palindrome(l))