last1 = 0
last2 = 1
soma = 1


for i in range(0, 100):
    print(last1)
    soma = last1 + last2
    last1 = last2
    last2 = soma
