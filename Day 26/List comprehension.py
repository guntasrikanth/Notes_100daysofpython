# Creating new list from existing list using normal method
# number = [1, 2, 3]
# new_list =[]
# for n in number:
#     new_list.append(n*2)
# print(new_list)


# Creating new list from existing list using list comprehension method
# number = [1, 2, 3]
# new_list =[n*2 for n in number]
# print(new_list)


# creating letter list from a name
# name = "SRIKANTH"
# char_list = [letter for letter in name]
# print(char_list)


# doubling the number value from a given range of numbers
# double_num = [num*2 for num in range(1,5)]
# print(double_num)


# applying if condition in list comprehension and getting strings whose length is less than or equal to 4
# names =['siri', 'sai', 'srikanth', 'renu', 'harsha', 'Srijani']
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
# upper_case_names = [name.upper() for name in names if len(name)>5]
# print(upper_case_names)