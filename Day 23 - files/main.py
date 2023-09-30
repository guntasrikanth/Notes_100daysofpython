# operating files with open and close method
# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# operating files with keywords 'with', 'as'
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)


#opening file in write mode
# with open('my_file.txt', mode='w') as file:
#     file.write('\nThis is Srikanth.')


#opening file in append mode
# with open('my_file.txt', mode='a') as file:
#     file.write('\nThis is Srikanth.')


#opening file in write mode, creates new file if provided file doesn't  exists
with open('my_new_file.txt', mode='w') as file:
    file.write('\nThis is Srikanth.')


