d={}
n=int(input("Enter no of students"))
for i in range(n):
    name=input("Enter student name:")
    marks=int(input("Enter student marks:"))
    d[name]=marks
print(d)
key=input("Enter name of the student to be searched::")
if key in d:
    print("The mark of ",key,"is",d[key])
else:
    print("Student not found")
