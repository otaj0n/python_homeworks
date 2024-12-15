import datetime

name = input("Please enter your name: ").strip()
year = int(input("Please enter your birht year: "))
current_year = datetime.datetime.now().year

age = current_year - year
print(f"Your name is {name}, and you are {age} years old")