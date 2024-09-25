print("Дан объём фигуры x куб.ед")
print("Найдите радиус фигуры")
x=int(input("введите x:"))
import math
r = (3*(int(x)**(1/3))) / (4*math.pi)
print("Радиус фигуры:",float(r))

