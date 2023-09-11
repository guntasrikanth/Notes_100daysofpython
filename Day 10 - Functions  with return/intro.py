'''def format(f_name, l_name):
    # title() method returns the titled string, to hold that value we assigning the value to a new variable
    #print(f_name.title())
    #print(l_name.title())
    
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    #we are returning the f string to the function call
    return f"{formatted_f_name} {formatted_l_name}"

#printing the value returned from the function
print(format("guntA","srikAnth")) '''

############# multiple return statements ################
''' def format(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Didn't provide valid inputs"
    # title() method returns the titled string, to hold that value we assigning the value to a new variable   
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    #we are returning the f string to the function call
    return f"{formatted_f_name} {formatted_l_name}"

#Taking values from the user
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
#printing the value returned from the function
print(format(f_name, l_name)) '''

############### Doc string #########################

def add(num1,num2):
    ''' This Function takes 2 arguments as input
    and returns the addition of both the arguments
    '''
    return num1+num2

print(add(4,6))
#accessing the doc string of Add function
print(add.__doc__)


"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""