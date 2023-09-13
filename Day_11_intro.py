######################### scope ################

friends = 2
def increase_friends():
    friends = 3
    print(f"Friends value inside function: {friends}")
    
increase_friends()
print(f"Friends value outside function: {friends}")


############# Local Variable #######################

def count_apple():
    apple = 5
    print(f"Apple value inside function: {apple}")

count_apple()
#we are trying to access apple variable which is declared inside the function count_apple
#since it is local to the function we can't access the variable 
#4print(f"apple value outside function: {apple}")

############# Global Variable #######################

apple = 4
def count_apple():
    print(f"Apple value inside function: {apple}")
    
count_apple()
print(f"Apple value outside function: {apple}")

############# local and global functions ##############

#global declared function
def count_apple():
    apple = 5
    print(f"Apple value inside function: {apple}")
    #locally declared function 
    def count_increased():
        increased_apple = 7
        print(f"Apple value inside nested function: {apple}")
        print(f"increased Apple value inside nested function: {increased_apple}")
    count_increased()
    
    #we can't access increased_apple as it is local to count_increased only
    #print(f"increased Apple value inside function: {increased_apple}")

#we can access count_apple(), since it is globally declared function
count_apple()

#we cannot access count_increased(), because it is declared locally inside count_apple() 
#and can access only in count_apple()
#count_increased()

########## No block scope in python ################

avatar = ['Rookie','Hallowen', 'Detective','War Commando']
game_level = 3
#There is no block scope in python, variables declared inside if, while or for blocks 
#can be accessed outside the block(globally)
'''
if game_level < 5:
    new_avatar = avatar[2]
print(new_avatar) '''

#If same variable declared inside if, while or for blocks is inside a function 
#than that variable is local to that function and can access only inside that function but not globally
def game():
    if game_level < 5:
         new_avatar = avatar[2]
    print(f"Avatar inside function: {avatar}")

#print(new_avatar)

############## editing global variable ###################
friends = 2
def increase_friends():
    #by using keyword 'global', we can 
    global friends 
    friends += 1
    print(f"Friends value inside function: {friends}")
    
increase_friends()
print(f"Friends value outside function: {friends}")