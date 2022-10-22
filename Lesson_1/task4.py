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
 print ("does not exist");
