l = input()

vowels = "aeiou"
vowels_count = consonants_count = 0
for char in l:
    if char.lower() in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print(f"Vowels = {vowels_count}, Consonants = {consonants_count}")