grade = float(input("Enter your Grade: "))

if grade >= 1 and grade < 6: 
       print('You are in Elementary School!', end = " ")
elif grade >= 6 and grade < 9: 
       print('You are in Middle School!', end = " ")
elif grade >= 9 and grade < 13: 
       print('You are in High School!', end = " ")
elif grade >= 13 and grade < 17: 
       print('You are in College!', end = " ")
else: 
       print('You may be done with school and college OR too little to goto School!!', end = " ")