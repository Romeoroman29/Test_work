import random
t=True
while t:
    n=int(input("Введите количество корзин:"))
    if n>0:
        t=False
    else:
        print("Вы ввели отрицательное число")
t=True
while t:
    w=int(input("Введите вес одной монеты:"))
    if w>0:
        t=False
    else:
        print("Вы ввели отрицательное число")
t=True
while t:
    d=int(input("Введите разницу между фальшивой и настоящей монетой:"))
    if d<w:
        t=False
    else:
        print("Вы ввели разницу между монетами либо равную самой монете,"
              "либо больше самой монеты")
rand=random.randint(0,n-1)
p=0
sum=((2*w+w*(n-2))/2)*(n-1) #сумма монет до n-1 если все монеты не фальшивки
mas=[]
for i in range(0,n):
    if i!=rand:
        mas.append(w)
    else:
        mas.append(w-d)
print("Вес одной монеты в каждом мешке:")
print(*mas)
for i in range(1,n):
    p+=i*mas[i-1] #вес монет до n-1 которые находятся в мешках
if p!=sum:
    print("Корзина, в которой фальшивые монеты имеет номер:",int((sum-p)/d))
else:
    print("Корзина, в которой фальшивые монеты имеет номер:",n)

