#Make a program that reads two grades from a student and calculates the average between them

grd1 = float(input('Type the first grade: '))
grd2 = float(input('Type the second grade: '))
avr = (grd1 + grd2) / 2

print('The student got {:.2f}'.format(avr))
