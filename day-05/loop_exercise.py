student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
# This is a list of student scores on an exam.
total_exam_score = sum(student_scores)
print(f"Total score via sum function: {total_exam_score}")
# This code calculates the total exam score by summing all the individual scores in the student_scores list.

sum = 0
for score in student_scores:
    sum += score
print(f"Total score: {total_exam_score}")

# This code does the same thing as the previous code, but it uses a for loop to iterate through each score in
# the student_scores list and adds it to a variable called sum. After the loop is done, it prints the total score. 
# The result should be the same as the previous code, which uses the built-in sum function.

highest_exam_score = max(student_scores)
print(f"Highest score via max function: {highest_exam_score}")
# This code finds the highest exam score by using the built-in max function on the student_scores list.

max = 0
for score in student_scores:
    if score > max:
        max = score
print(f"Highest score: {highest_exam_score}")
# This code does the same thing as the previous code, but it uses a for loop to iterate through each score in
# the student_scores list and compares it to a variable called max. If the score is greater than max, it updates 
# max to be that score. After the loop is done, it prints the highest score. The result should be the same as the 
# previous code, which uses the built-in max function.