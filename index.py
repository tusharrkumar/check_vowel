# check number of vowels

s = input("Enter The String: ")
c = 0
vowel = 'aeiou'
for i in s:
    if i.lower() in vowel:
        c += 1
print(f'Number of vowel present {c}')
