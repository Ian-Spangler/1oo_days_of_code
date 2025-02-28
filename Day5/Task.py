fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
print(fruits)

student_scores = [180 ,124, 165, 173, 189, 169, 146]

# Sum of exam score
total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)

# Highest exam score
max = 0
for score in student_scores:
    if score > max:
        max = score
print(max)

# Range function
gauss_sum = 0
for number in range(1, 101):
    gauss_sum += number
print(gauss_sum)