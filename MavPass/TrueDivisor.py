def divisorfinder(number):
    divisor = []
    for i in range (1, number):
        if (number % i) == 0 and (i%2)==0:
            divisor.append(i)
    return divisor

divisor = divisorfinder(520)
newlist = []

for i in range (4,len(divisor)):
    newlist.append(divisor[i])
