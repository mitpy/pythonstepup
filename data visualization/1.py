import matplotlib.pyplot as plt

subjects=['Maths','English','Science','Social']
s1=[100,80,33,60]
s2=[33,60,100,80]
s3=[60,100,33,80]

plt.plot(subjects,s1,color='r')
plt.plot(subjects,s2,color='g')
plt.plot(subjects,s3,color='b')

plt.xlabel('Subject')
plt.ylabel('Marks')
plt.title('Student Marks ')
plt.show()