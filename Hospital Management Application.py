class Doctor:
    Doctor_dict={}
    Hospital_name = "diana"

    def __init__(self):
        self.ID = input("\t Enter The ID Number : ")
        self.Name = input("\t Enter The Name : ")
        self.Phone_no = input("\t Enter The Phone Number : ")
        self.Address = input("\t Enter The Address : ")

        print("\n Details added Sucessfully\n")
        self.get_doctor()

    def get_doctor(self):
        print("---DOCTORS DETAILS---\n")
        print("ID no : ",self.ID)
        print("Name : ",self.Name)
        print("_Phone No : ",self.Phone_no)
        print("Address : ",self.Address)
        print("Hospital : JB Hospital")

    def update_doctors(self):
        print("select option to update doctors")
        print("\t\t\t1)to change a name of the doctor")
        print("\t\t\t2)to change a phone of the doctor")
        print("\t\t\t3)to change a address of the doctor")
        option = input("enter the option to change : ")
        print()
        if option in ["1","2","3"]:
            if option == "1":
                self.Name = input("enter the doctor new name : ")
                print("name change successfully ")
            elif option == "2":
                self.Phone_no = input("enter the  doctor new phone number : ")
                print("doctor phone number  changed successfuly ")
            else :
                self.Address = input("enter the doctor new address : ")
                print("doctoe address changed successfully ")
            self.get_doctor()
        else:
            print("something went worng ")

    @classmethod
    def gettotaldoctorcount(cls):
        return len(cls.Doctor_dict)

    @classmethod
    def updatehospitalname(cls, new_hospital_name):
        cls.Hospital_name = new_hospital_name


class Nurse:
    nurse_dict={}

    def __init__(self):
        self.ID = input("\t Enter The ID Number : ")
        self.Name = input("\t Enter The Name : ")
        self.Phone_no = input("\t Enter The Phone Number : ")
        self.Address = input("\t Enter The Address : ")

        print("\n Nurse added Sucessfully\n")
        self.get_nurse()

    def get_nurse(self):
        print("---nurse DETAILS---\n")
        print("ID no : ", self.ID)
        print("Name : ", self.Name)
        print("Phone No : ", self.Phone_no)
        print("Address : ", self.Address)
        print("Hospital : JB Hospital")

    def update_Nurse(self):
        print("select option to update Nurse")
        print("\t\t\t1)to change a name of the nurse")
        print("\t\t\t2)to change a phone of the nurse")
        print("\t\t\t3)to change a address of the nurse")
        option = input("enter the option to change : ")
        print()
        if option in ["1","2","3"]:
            if option == "1":
                self.Name = input("enter the nurse new name : ")
                print("name change successfully ")
            elif option == "2":
                self.Phone_no = input("enter the  doctor new phone number : ")
                print("nurse phone number  changed successfuly ")
            else:
                self.Address = input("enter the doctor new address : ")
                print("nurse address changed successfully ")
            self.get_nurse()
        else:
            print("something went worng ")


    @classmethod
    def gettotalnursecount(cls):
        return len(cls.nurse_dict)




def main():
    print("===================================================")
    print("\t--------Welcome To JB Hospital----------\t\t")
    print("===================================================")
    print("\t ) To Change The Hospital Name")
    print("\t 1) To Get Doctor Details")
    print("\t 2) Add Doctors")
    print("\t 3) Remove Doctors")
    print("\t 4) Update Doctors")
    print("\t 5) To Get Total number of doctor")
    print("\t 6) To Get All Doctors Details")
    print("*********************************************************")
    print("\t 7) To Get Nurse Details")
    print("\t 8) Add Nurse")
    print("\t 9) Remove Nurse")
    print("\t 10) Update Nurse")
    print("\t 11) To Get Total number of nurse")
    print("\t 12) To Get All Doctors Nurse")

    option = input("Enter Any Above Given Option : ")
    print()

    if option =="1":
        ID = input("Dnter The Id Of The doctor : ")
        try:
            Doctor.Doctor_dict[ID].get_doctor()
        except:
            print("You Are Enter The Worng Id ")
    elif option == "2":
        new_member = Doctor()
        Doctor.Doctor_dict[new_member.ID] = new_member
    elif option == "3":
        ID = input(" enter the id that you want to delete : ")
        try:
            student_doc = Doctor.Doctor_dict.pop(ID)
            print(f"{ID} deleted successfully")
        except:
            print("there is no one on the id ")
    elif option == "4":
        ID = input("enter the id of the doctor : ")
        print()
        try:
            Doctor.Doctor_dict[ID].update_doctors()
        except:
            print("you have enter the worng id")
    elif option == "5":
        print("Total number of doctors in the hospita : ",Doctor.gettotaldoctorcount())
    elif option == "6":
        if Doctor.Doctor_dict:
            print("total number of doctor in the hospital ",Nurse.gettotalnursecount())
            print("total Doctors lists with details")
            print()
            for dno,doctor in enumerate(Doctor.Doctor_dict.values()):
                print("Doctor - ",dno + 1)
                doctor.get_doctor()
                print()
    elif option == "7":
        ID = input("enter the id of the nurse : ")
        try:
            Nurse.nurse_dict[ID].get_nurse()
        except:
            print("something went wrong ")
    elif option == "8":
        new_member = Nurse()
        Nurse.nurse_dict[new_member.ID] = new_member
    elif option == "9":
        ID = input("enter the id that you want to delete : ")
        try:
            Staff_nurse = Nurse.nurse_dict.pop(ID)
            print(f"{ID} deleted successfully")
        except:
            print("there no one on the id")
    elif option == "10":
        ID = input("enter the id of the nurse to update : ")
        print()
        try:
            Nurse.nurse_dict[ID].update_Nurse()
        except:
            print("you are enter the worng id")
    elif option == "11":
        print("total number of nurse in the hospital : ",Nurse.gettotalnursecount())
    elif option =="12":
        if Nurse.nurse_dict:
            print("total number of doctor in the hospital is",Nurse.gettotalnursecount())
            print("\n total doctor with there details \n")
            for nurno,nur in  enumerate(Nurse.nurse_dict.values()):
                print("Nurse",nurno+1)
                nur.get_nurse()
                print()
    else:
        new_hospital_name = input("\tEnter The New hospital Name : ")
        Doctor.updatehospitalname(new_hospital_name)
        print("Hospital Name Changed Successfilly")

if __name__=='__main__':
    option = "y"
    while option == "y":
        main()
        option = input("\n Do You Want To Continue [Y/N?]:")
        print()
