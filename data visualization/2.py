import matplotlib.pyplot as plt

students=['s1','s2','s3']
mathsMarks=[100,33,60]
plt.bar(students,mathsMarks)
plt.xlabel('Students')
plt.ylabel('Maths Marks')
plt.title('Maths Marks')
plt.show()