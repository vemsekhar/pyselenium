
f = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2, f)) # [1, 1, 3, 5, 13, 21, 55]
even_numbers = list(filter(lambda x: x % 2 == 0, f)) #[0, 2, 8, 34]

print(odd_numbers)
print(even_numbers)