username = input("Enter username:").strip()
password = input("Enter password:").strip()

def is_empy(a,b):
    if a and  b:
        return True
    else:
        return False

print(is_empy(username, password))