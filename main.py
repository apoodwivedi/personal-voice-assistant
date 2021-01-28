import matplotlib.pyplot as plt
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
total_students = 0
for item in students:
 total_students +=item
student_percentage = []
for item in students:
 percentage=(item*100)/(total_students*1.0)
 student_percentage.append(percentage)
explode = (0, 0, 0, 0.1,0) # only "explode" the 4th slice (i.e. 'Python')
#print(student_percentage)
fig1, ax1 = plt.subplots()
ax1.pie(student_percentage, explode=explode, labels=langs, autopct='%1.1f%%',
 shadow=True, startangle=90)
plt.show()