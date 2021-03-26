from functools import total_ordering


@total_ordering
class Student:
   def __init__(self,name,rollnumber):
       self.name=name
       self.rollnumber=rollnumber

   def __le__(self,other):
       if isinstance(other,Student):
          return self.rollnumber<other.rollnumber

   def __eq__(self,other):
      if isinstance(other,Student):
         return self.rollnumber==other.rollnumber

   def __str__(self):
       return f"{self.name} and {self.rollnumber}"

if __name__=="__main__":
   l=[Student("s1",12),Student("s2",14),Student("s3",17),Student("s0",15)]
   l.sort()
   for s in l:
      print(s)



