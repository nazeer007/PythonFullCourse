numbers = [2, 2, 6,5,6,7,2,3,5]
unique =[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)