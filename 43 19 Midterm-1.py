number=100

fib=[0,1]

if number<=0:
    print('Invalid number')

elif number == 1:
    print([0])
    print('\nThe sum of the fibonacci numbers is, 0')

else:
    for i in range(number-2):
        nxtfbn = fib[-1] + fib[-2]
        fib.append(nxtfbn)

print(fib)

Sum=sum(fib)
print('\nThe sum of the fibonacci numbers is,', Sum)
