def get_grade(*marks):
   # print("Subject:", subject)
   print("Marks:", marks)       
   print(type(marks))

   for mark in marks:
       if mark < 0 or mark > 100:
           print("Invalid marks:", mark)
       elif mark >= 90:
           print("Grade: A for", mark)
       elif mark >= 80:
           print("Grade: B for", mark)
       elif mark >= 70:
           print("Grade: C for", mark)
       elif mark >= 60:
           print("Grade: D for", mark)
       else:
           print("Grade: F for", mark)        


get_grade(95,89,65)

