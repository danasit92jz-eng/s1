numbers = [1,2,3,4,5,6,7]

odd = [x for x in numbers if x % 2 != 0]
even = [x for x in numbers if x % 2 == 0]

print("Original List:", numbers)
print("Odd List:", odd)
print("Even List:", even)
