student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇
for keys in student_scores:
    if student_scores[keys]>90:
        student_grades[keys] = "Outstanding"
    elif student_scores[keys]>80:
        student_grades[keys] = "Exceeds Expectations"
    elif student_scores[keys]>70:
        student_grades[keys] = "Acceptable"
    else:
        student_grades[keys] = "Fail"

print(student_grades)


"""
Connect with me on 
[LinkedIn](www.linkedin.com/in/gunta-srikanth) 
for more coding challenges, updates on my 100 days of learning journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""