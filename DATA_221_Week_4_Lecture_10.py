import matplotlib.pyplot as plt

#Bar Graph
my_winter_semester_courses =["DATA 221", "MATH 211", "MATH 265",
                                  "GRST 211", "CPSC 219"]
my_final_course_grades = [93, 90, 95, 96, 93]

plt.bar(x=my_winter_semester_courses, height = my_final_course_grades)
plt.show()

#Line Graph
height_of_data_science_students_in_centimeters = [152, 165, 182, 183]
weight_of_data_science_students_in_kilograms = [56, 67, 72, 76]

plt.plot(height_of_data_science_students_in_centimeters, weight_of_data_science_students_in_kilograms,
         'o-', label="Data Science Students", color ="red")
plt.show()

#Scatter Plot
data_221_students_final_gpa = [4.00, 3.75, 3.67, 2.50, 3.10]
data_221_students_final_course_grade = [4.00, 4.00, 3.30, 2.70, 3.30]

plt.scatter(data_221_students_final_gpa, data_221_students_final_course_grade, label = 'Data 221 Student', color = 'red')
plt.legend()
plt.show()

#Contour Plot
x = [[1,1,1,1],
    [2,2,2,2],
    [3,3,3,3]]
y = [[1,2,3,4],
     [1,2,3,4],
     [1,2,3,4]]
heights = [[1,2,3,4],
           [2,3,4,5],
           [3,4,5,6]]
plt.contourf(x, y, heights)
plt.show()
