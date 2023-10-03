# getting length of an individual word in a sentence using dict comprehension
# sentence = input("Enter any senetnce:  ")
# new_list = sentence.split(' ')
#
# result = {word:len(word) for word in new_list}
# print(result)


#converting temperature to F
# {'Monday' : 23, 'Tuesday' : 45, 'Wednesday' : 34, 'Thursday' : 37, 'Friday' : 29, 'Saturday' : 31, 'Sunday' : 34}
# weather_c = eval(input("enter temperature of every day in last week:  "))
# weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

import pandas
student_dict = {
    'students' : ['Srikanth', 'Siri', 'Harish'],
    'score' : [87, 76, 62],
}
student_dataframe = pandas.DataFrame(student_dict)
#print(student_dataframe)

# looping through dataframe
# for (key, value) in student_dataframe.items():
#     print(value)

# looping through rows of dta frame
for (index, row) in student_dataframe.iterrows():
    # if row.score > 60:
    #     print(row.students)
    if row.students == 'Srikanth':
        print(row.score)
