import random
import pandas

# Dictionary Comprehension with Lists
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)

# Dictionary Comprehension with Dictionary
passed_students = {student: score for (student, score) in students_score.items() if score > 70}
# print(passed_students)

# Dictionary Comprehension exercise 1 - Get length of each word in sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
letter_count = {word: len(word) for word in sentence.split()}
# print(letter_count)

# Dictionary Comprehension exercise 2 - Convert temperature to Fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temperature_c * 9 / 5) + 32 for (day, temperature_c) in weather_c.items()}
print(weather_f)

# Iterate over Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.score)

    # Print row that has the name Angela
    if row.student == "Angela":
        print(row.student, row.score)
