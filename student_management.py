students=[]
n=int(input("Enter no of students:"))
for i in range(n):
    s_id=int(input("Enter student id:"))
    name=(input("Enter student name:"))
    marks=int(input("Enter student marks:"))
    s1=(s_id,name,marks)
    students.append(s1)
students=tuple(students)
print("\n\tStudent Details:")
for s in students:
    print("ID:",s[0],"Name:",s[1],"Marks:",s[2])
key=int(input("\nEnter student id:"))
f=0
for s in students:
    if s[0]==key:
        print("Student found..")
        print("ID:",s[0],"Name:",s[1],"Marks:",s[2])
        f=1
if not f:
    print("Student not found..")
m=students[0]
for s in students:
    if s[2]>m[2]:
        m=s
print("\nStudent with highest marks:")
print("ID:", m[0], "Name:", m[1], "Marks:", m[2])
print("\nStudent with less than 40 marks:")
for s in students:
    if s[2]<40:
        print("ID:",s[0],"Name:",s[1],"Marks:",s[2])
t=0
for s in students:
    t=t+s[2]
avg=t/len(students)
print("\n Average marks:",avg)
