#Make a program that reads a number and shows its double, triple and square root
num = float(input('Type a number: '))
print('The double of {} is {}'.format(num, num * 2))
print('The triple of {} is {}'.format(num, num * 3))
print('The square root of {} is {:.2f}'.format(num, (num ** (1 / 2))))
