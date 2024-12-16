grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average=sum(grades[0])/len(grades[0])
print(average)
average=sum(grades[1])/len(grades[1])
print(average)
average=sum(grades[2])/len(grades[2])
print(average)
average=sum(grades[3])/len(grades[3])
print(average)
average=sum(grades[4])/len(grades[4])
print(average)
grades_2=[[4.0], [2.25], [4.0], [3.6666666666666665], [4.8]]
names=list(students)
print(names)
names.sort()
print(names)
result={}
for i in range(len(names)):
    result[names[i]] = grades_2[i][0]
print(result)