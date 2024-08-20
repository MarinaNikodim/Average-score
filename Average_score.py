grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=list(students)
sorted_students_list=sorted(students_list)
print(sorted_students_list)
average_grades=(sum(grades[0])/len(grades[0])), float((sum(grades[1])/len(grades[1]))), (sum(grades[2])/len(grades[2])), float((sum(grades[3])/len(grades[3]))), float((sum(grades[4])/len(grades[4])))
average_grades_list=list(average_grades)
print(average_grades_list)
my_dict={}
for i in range(0, len(average_grades_list)):
    my_dict[sorted_students_list[i]]=average_grades_list[i]
print(my_dict)
#2nd version
my_dict=(dict(zip(sorted_students_list, average_grades_list)))
print(my_dict)















