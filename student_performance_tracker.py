n = int(input("Enter the total records you want to show : "))
list_of_students = []


for i in range(n):
        name = input("Enter your name : ")
        maths = int(input("Enter your maths  marks : "))
        science = int(input("Enter your science marks : "))
        eng = int(input("Enter your english marks : "))
      

        if 0 <= maths <= 100 and 0 <= science <= 100 and 0 <= eng <= 100:
                total_marks = (maths + science + eng)
                percent = (total_marks / 300) * 100
                print(f"Name : {name} ")
                print(f"total_marks : {total_marks}")
                print(f"percent : {percent}")
                if percent >= 90:
                        print("Congrats !! you have secured A Grade.")
                        grade = "A Grade"
                elif percent >= 80:
                        print("Congrats You have secured B Grade .")
                        grade = "B Grade"
                elif percent >= 70:
                        print("Congrats You have secured C Grade. You can score more good")
                        grade = "C grade"
                elif percent >= 60 :
                        print(" You have secured D Grade. Study More Hard")
                        grade = "D Grade"
                else:
                        print("You have secured F Grade. You need to study very hard orelse you will fail")
                        grade = "F Grade"
                student = {
                                "name": name,
                                "total_marks": total_marks,
                                "percentage": percent,
                                "grade": grade
                                }
                list_of_students.append(student)
        
        else:
              print("Please enter valid marks ")
        
print(list_of_students)

for i in list_of_students:
    print(f"Name: {i['name']}")
    print(f"Total Marks: {i['total_marks']}")
    print(f"Percentage: {i['percentage']}")
    print(f"Grade: {i['grade']}")
    print("-------------------")





