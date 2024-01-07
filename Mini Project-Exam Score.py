# Weighted Exam Score Average Calculation Code

# Enter how many exams you have done
number_of_exams = int(input("Enter number of exams: "))
# Enter how many these exams cover
total_credits = int(input("Enter number of credits these exams cover: "))
# Begin with average of 0 then add up percentages from exams
average = 0
for exam in range(number_of_exams):
    score = int(input("Enter exam scores: "))
    exam_credits = int(input("Enter how many credits this exam covered: "))
    average = average + score*exam_credits/total_credits
print("Your average is", average)