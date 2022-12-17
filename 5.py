Xa = float(input("Введите Хa: "))
Ya = float(input("Введите Ya: "))
Xb = float(input("Введите Xb: "))
Yb = float(input("Введите Yb: "))
from math import sqrt
result=sqrt(((Xb-Xa)**2)+((Yb-Ya)**2))
print (f"Растояние между точками равна {result}")