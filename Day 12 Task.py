import json

myjsonfile = open(r'C:\Users\GIRISH\Desktop\Python Internship\Python-Internship\Day12Task.json','r')

jsondata = json.load(myjsonfile)

print(jsondata)

myjsonfile.close()

"""
#output = {'name': 'Girish', 'age': 19, 'Student': True, 'Department': 'Computer Science', 'Percentage': 97.6, 'Arrears': None,
'Course': {'Course ID': 1001, 'Subject': 'Operating system', 'Credits': 4}, 'Hobbies': ['Photography', 'Designing', 'Movies', 'Fitness']}

"""
"""
#created a .json file with the info given below
{
  "name": "Girish",
  "age": 19,
  "Student": true,
  "Department": "Computer Science",
  "Percentage": 97.6,
  "Arrears": null,
  "Course": {"Course ID": 1001, "Subject": "Operating system", "Credits": 4},
  "Hobbies": ["Photography","Designing","Movies","Fitness"]

}

"""
