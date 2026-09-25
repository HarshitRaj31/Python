while True:
     print("1/ for student grade\n")
     print("2/ for getting leap year\n")
     print("else you got nothing\n")
     choose=int(input("Enter your choice "))
     match choose:  
          case 1:
               n=int(input("Enter student marks"))

               if n<=100 and n>=90:
                    print("Grade O")
               elif n<=89 and n>=80:
                    print("Grade A+")
               elif n<=79 and n>=70:
                    print("Grade A")
               else:
                    print("Fail")
          case 2:
               year=int(input("Enter the year"))
               if (year%100!=0 and year%400==0)or year%4==0:
                    print("Leap year")
               else:
                    print("Not leap")
          case _:
               print("Invalid")
               break                                  


