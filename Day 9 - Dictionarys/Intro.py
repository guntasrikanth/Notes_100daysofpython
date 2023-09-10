
#creating dict with key,value pair
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}
#print(programming_dictionary)

#reterving items from dict
#print(programming_dictionary["Function"])

#adding new items to dict
programming_dictionary['Loops'] = "The action of doing something over and over"

#editing existing item
programming_dictionary['Bug'] = 'Edited with new item'

#accessing dict items using for loop
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key]+"\n")

#creating empty dict
new_dict ={}
#print(f"created new_dict: {new_dict}")

#clearing the existing dict
programming_dictionary = {}
#print(f"cleared programming_dict: {programming_dictionary}")

#################  Nesting  ##################

travel = {
  'India': "Delhi",
  'USA' : "D.C",
}

#nesting a list in dict
travel_list = {
  'India': ["Delhi","Hyderabad","Bangalore"],
  'USA' : ["D.C","Illinois","New York","Maryland"],
}

#nesting a dict in a dict

travel_dict ={
  'India': {"Delhi":1,"Hyderabad":4,"Bangalore":3},
  'USA' : {"Cities_visited":["D.C","Illinois","New York","Maryland"],"Total_visits":15},
}

#nesting a dict in a list
travel_list_dict =[
   {
    "Country":"India",
    "Cities_visited":["Delhi","Hyderabad","Bangalore"],
    "Total_visits":10,
   },
   {
      "Country":'USA',
      "Cities_visited":["D.C","Illinois","New York","Maryland"],
      "Total_visits":15,
    },
]

print(travel)
print(travel_list)
print(travel_dict["USA"]["Cities_visited"])
print(travel_list_dict[3]["Cities_visited"])
