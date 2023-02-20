class Student:
    student_dict={}
    college_name="jothi"

    def __init__(self):
        self.Rollno=input("\t Enter The Roll Number : ")
        self.Name=input("\t Enter The Name : ")
        self.Phone_no=input("\t Enter The Phone Number : ")
        self.Address=input("\t Enter The Address : ")
        stu_year = input("\t Enter The Year[ex:1,2,3,4] : ")

        if stu_year in Studentclass.classes:
            Studentclass.classes[stu_year].studentlist.append(self)
        else:
            new_class = Studentclass(stu_year)
            new_class.studentlist.append(self)
            Studentclass.classes[stu_year]=new_class

        self.stu_year = Studentclass.classes[stu_year]

        print("\n Student Added Sucessfully\n")
        self.get_student()

    def get_student(self):
        print("---STUDENT DETAILS---\n")
        print("Roll no : ",self.Rollno)
        print("Name : ",self.Name)
        print("Phone No : ",self.Phone_no)
        print("Address : ",self.Address)
        print("Year : ", self.stu_year.Name)
        print("College : Jothi College")

    def update_student(self):
        print("\t\tSelect Option To Update Students")
        print("\t\t\t1)To Change Student Name")
        print("\t\t\t2)To Change Student Phone Number")
        print("\t\t\t3)To Change Student Address")
        print("\t\t\t4)To Change Student Year")
        option=input("Enter Any Above Given Option : ")
        print()
        if option in ["1","2","3","4"]:
            if option=="1":
                self.Name = input("\t\t\tEnter The Student New Name : ")
                print("\n\t\tStudent Name Changed Successfully\n")

            elif option=="2":
                self.Phone_no = input("\t\t\t Enter The Student New Phone Number : ")
                print("\n\t\tStudent Phone Number Changed Successfully\n")

            elif option=="3":
                self.Address = input("\t\t\tEnter The Student New Address : ")
                print("\n\t\tStudent Address Changed Successfully\n")

            else:
                new_class = input("\t\t\tEnter The Student Year : ")
                self.stu_year.studentlist.remove(self)
                try:
                    self.stu_year = Studentclass.classes[new_class]
                    self.stu_year.studentlist.append(self)
                except:
                    addclass = Studentclass(new_class)
                    self.stu_year = addclass
                    addclass.studentlist.append(self)
                print("\n\t\tStudent Year Changes Successfully\n")
            self.get_student()
        else:
            print("You Are Choosen Worng Option")

    @classmethod
    def updatecollegename(cls,new_college_name):
        cls.college_name=new_college_name

    @classmethod
    def gettotalstudentcount(cls):
        return len(cls.student_dict)


class Studentclass:

    classes={}
    def __init__(self,Name):
        self.Name = Name
        Studentclass.classes[Name] = self
        self.studentlist=[]

def main():

    print(f"---Welcome To {Student.college_name} College Of Art & Science---\n")
    print("\t1) To Get Students Details")
    print("\t2) To Add New Student")
    print("\t3) To Remove Student")
    print("\t4) To Update Student Details")
    print("\t5) To Update College Name")
    print("\t6) To Get Number of Students in College")
    print("\t7) To Get All Students Details")
    print("\t8) To Get Any Class Students Details\n")

    option=input("Enter Any Above Given Option : ")
    print()

    if option=="1":
        Roll_no = input("Enter The Roll Number : ")
        try:
            Student.student_dict[Roll_no].get_student()
        except:
            print("You Are Enter The Wrong Roll Number ")
    elif option=="2":
        new_student = Student()
        Student.student_dict[new_student.Rollno] = new_student
    elif option=="3":
        Roll_no = input("\tEnter The Roll Number Of The Student : ")
        try:
            people = Student.student_dict.pop(Roll_no)
            people.stu_year.studentlist.remove(people)
            print(f"\t\t{Roll_no} Student Deleted Successfully")
        except:
            print("\t\tNo Student There To Delete")
    elif option=="4":
        Roll_no=input("Enter The Roll Number Of The Student : ")
        print()
        try:
            Student.student_dict[Roll_no].update_student()
        except:
            print("\n\t\t You Have Enter The Wrong Roll Number ")
    elif option=="5":
        new_college_name = input("\tEnter The New College Name : ")
        Student.updatecollegename(new_college_name)
        print("College Name Changed Successfilly")
    elif option=="6":
        print("Total Number Of Student In The College : ",Student.gettotalstudentcount())
    elif option=="7":
        if Student.student_dict:
            print("Total Number Of Student In College : ",Student.gettotalstudentcount())
            print("\n Total Student List With Details \n ")
            for sNo,student in enumerate(Student.student_dict.values()):
                print('Student - ',sNo+1)
                student.get_student()
                print()
        else:
            print("No Students Here")
    else:
        try:
            student=Studentclass.classes[input("\t Enter The Class Name : ")]
            print("\n Student Of Class - ",student.Name)
            print(f"\n Total Number Of Students In Class {student.Name} : {len(student.studentlist)}")
            print()
            for sNo, student in enumerate(Student.studentlist):
                print('Student - ', sNo + 1)
                student.get_student()
                print()
        except:
               print("\n You Entered Worng Class Name Of No Of Students There")


if __name__=='__main__':
    option = "y"
    while option == "y":
        main()
        option = input("\n Do You Want To Continue [Y/N?]:")
        print()
