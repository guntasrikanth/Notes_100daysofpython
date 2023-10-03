list_of_strings = input("Enter some numbers:  ").split(',')
num_list = [int(n) for n in list_of_strings]
result = [ num for num in num_list if num % 2 == 0]
print(f"Even numbers are: {result}")