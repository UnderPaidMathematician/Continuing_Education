student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# I also built a grade book, this may be more than she wanted.
grade_book = {
    "91-100" : "Outstanding",
    "81-90" : "Exceeds Expectations",
    "71-80" : "Acceptable",
    "0-70" : "Failure was an option, and you checked the box."
}

# getting a list of tuples for the min max of grades 
# Typically the gradebook never changes so tuple seems like a good choice.
min_max_list = []
for k in grade_book.keys():
    min_max_list.append(tuple(k.split("-")))

#TODO-2: Write your code below to add the grades to student_grades.👇

for key, value in student_scores.items():
    for tup in min_max_list:
        minimum, maximum = tup
        minimum = int(minimum)
        maximum = int(maximum)
        if (value >= minimum) and (value <= maximum):
            student_grades[key] = grade_book[f'{minimum}-{maximum}']
            

# 🚨 Don't change the code below 👇
print(student_grades)