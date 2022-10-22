<<<<<<< HEAD
=======
<<<<<<<< HEAD:Lesson_1/task3.py
Seconds = int (input ("Enter number of seconds: ") )
Seconds = Seconds % (24 * 3600)
Hour = Seconds // 3600
Seconds %= 3600
Minutes = Seconds // 60
Seconds %= 60
Days = Seconds % 86400
print ("Days:",Days,"Hours:",Hour,"Minutes:",Minutes,"Seconds:",Seconds);
"Days:",Days
"Minutes:",Minutes
========
>>>>>>> 5c168d45c0a900506b3518d9ee334463fe5b08ab
coefficient_a = float(input("enter coefficient a:"))
coefficient_b = float(input("enter coefficient b:"))
coefficient_c = float(input("enter coefficient c:"))
discriminant = coefficient_b ** 2 - 4 * coefficient_a * coefficient_c
print ("D = " + str(discriminant))
if discriminant == 0:
 x1 = (- coefficient_b / (2 * coefficient_a))**0.5
 print ("x1 = " + str(x1))
elif discriminant > 0:
 x1 = (- coefficient_b + (discriminant**0.5)) / (2 * coefficient_a)
 x2 = (- coefficient_b - (discriminant**0.5))  / (2 * coefficient_a)
 print ("x1 = " + str(x1))
 print ("x2 = " + str(x2))
else:
<<<<<<< HEAD
 print ("does not exist");
=======
 print ("does not exist");
>>>>>>>> 5c168d45c0a900506b3518d9ee334463fe5b08ab:Lesson_1/task4.py
>>>>>>> 5c168d45c0a900506b3518d9ee334463fe5b08ab
