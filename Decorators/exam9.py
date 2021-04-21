n = int(input('enter a number'))
a,b = 0,1
sum = 0
if n <=2:
    if n == 0:
        avg = float(n)
    elif n == 1:
        avg = n / n

    elif n == 2:
        avg = n / n

else:
    for i in range(n):
        a,b = b,a + b
        sum = sum + a
    if n != 0:
        avg = sum/n
    else:
        avg = 0.0
print(avg)