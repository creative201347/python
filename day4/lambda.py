

list_ = [34, 12, 64, 55, 75, 13, 63]

odd_list = list(filter(lambda num: (num % 2 != 0), list_))
multiply = list(map(lambda x: x*2, list_))
filtering = list(filter(lambda x: x > 50, list_))

print(odd_list)
print(multiply)
print(filtering)
