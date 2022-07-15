student = {'name': "Nabin Dhami", 'age': 22, 'courses': ["BECE", "ML"]}

# student['phone'] = "9889855"
# student['name'] = "Santosh Tiwari"
student.update({"name": "Hello", 'age': 26, 'phone': '985545'})
del student['age']


print(student)
print(student['courses'])
print(student.get('name'))


for key, value in student.items():
    print(key, value)
