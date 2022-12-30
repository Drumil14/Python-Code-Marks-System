choice =0
class Exam(object):
    def __init__(self):
        self.name=None
        self.collegename=0
        self.classroom = 0
        self.rollno=0
        self.login()
    def login(self):
        print("===================")


        username=input("Enter username")
        password=input("Enter password")

        print("====================")
        print()
#login section

        if username==password:
            print("Login successfully")
            self.getdata()
        else:
            print("Login fail try again")

    print()
#Enter your profile detail
    def getdata(self):
        self.name = input("Enter your name ")
        self.collegename = input("Enter your college name")
        self.classname = input("Enter your class name")
        self.rollno = input("Enter your roll number")
        print()

#static subject declartion
        print("choose any branch for giving exam")
        print("1. Mechanical Engineering")
        print("2. Information Technology")
        print("3. Computer Science")
        print("4. Civil Engineering")
        print()

        choice = int(input("Enter your choice"))

        if choice == 1:
            self.mechanical()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("you have entered wrong choice")

    def mechanical(self):
        print("1. First Semester")
        print("2. Second Semester")
        print("Enter your semester number")

        choice = int(input("Enter your choice"))
        if choice == 1:
            print("Math")
        elif choice == 2:
            pass
    
    def information(self):
        print("1. First Semester")
        print("2. Second Semester")
        choice = int(input("Enter your choice"))
        if choice == 1:
            pass
        elif choice == 2:
            pass

    def computer(self):
        print("1. First Semester")
        print("2. Second Semester")
        choice = int(input("Enter your choice"))
        if choice == 1:
            pass
        elif choice == 2:
            pass

    def civil(self):
        print("1. First Semester")
        print("2. Second Semester")
        choice = int(input("Enter your choice"))
        if choice == 1:
            pass
        elif choice == 2:
            pass

#object creation of class
# #obj = Exam()
# obj.login()
    

#Examination Calculation part
class Calcution(object):
    def __init__(self):
        self.stat=0
        self.dmgt=0
        self.cg=0
        self.toc=0
        self.math=0
        self.total=0
        self.percentage=0
        self.ps=0
        print()
        print("Do you want to put examination marks enter YEs/No")
        print()
        Yes = input("Enter yes/no")    
        if Yes == "yes":
            self.calculatemarks()
        else:
            print("Thank You for visiting here")
        print()

#taking marks for subject
    def calculatemarks(self):
        self.stat = int(input("Enter Marks of statistics: "))
        self.dmgt = int(input("Enter Marks of DMGT: "))
        self.cg = int(input("Enter Marks of cg: "))
        self.toc = int(input("Enter Marks of TOC: "))
        self.math = int(input("Enter Marks of Math1: "))
        print()
        
        if self.stat>=40 and self.dmgt>=40 and self.cg>=40 and self.toc>=40 and self.math>=40:
            self.ps="pass"
            print("You are pass")
        else:
            self.ps="Fail"
            print("You are fail")

        self.total = self.stat+self.dmgt+self.cg+self.toc+self.math
        self.percentage = self.total/5.0

#obj1 = Calculation()

#Assesment class
class Assesment(Exam, Calcution):

    def __init__(self):
        Exam.__init__(self)
        Calcution.__init__(self)

    def result(self):
        
        print("=============================================================================================")
        print("                                                                                             ")
        print("                           College Name: ",self.collegename,"                                ")
        print("                                                                                             ")
        print("=============================================================================================")

        print("|                          Student Name: ",self.name,"                                      |") 
        print("|                          Class Name  : ",self.classname,"                                 |") 
        print("|                          Roll No     : ",self.rollno,"                                    |")
        print("=============================================================================================")
        print("                                                                                             ")
        print(" Subject Name           :         Total Marks        :    Obatined Marks :                   ")

        print("                                                                                             ")
        print(" Statistic              :"        "    100   "       "       |",  self.stat,                "|")                                                                               
        print(" DMGT                   :"        "    100   "       "       |",  self.dmgt,                "|")                                                                               
        print(" CG                     :"        "    100   "       "       |",  self.cg,                  "|")                                                                               
        print(" TOC                    :"        "    100   "       "       |",  self.toc,                 "|")                                                                               
        print(" Math                   :"        "    100   "       "       |",  self.math,                "|")
        print("=============================================================================================")
        print("                                                                                             ")
        print("Result Status           :",                                       self.ps,"                  ")                                                           
        print("Total Marks             :",           "500",                                               "  ")
        print("Obtained Mraks          :",                                       self.total,              "  ")
        print("Percentage              :",                                       self.percentage,         "  ")
        print("=============================================================================================")
        
obj2 = Assesment()
obj2.result()



         
         

       