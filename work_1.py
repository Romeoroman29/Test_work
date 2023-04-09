t=True
while t:
    num=int(input("Введите число:"))
    if 0<num<=65535:
        t=False
    else:
        print("Введите правильное число")
def perevod(n,s):
    if n>0:
        s+=str(n%2)
        perevod(n//2,s)
        return s
    else:
        return 0
s=[]
result=perevod(num,s)
while len(s)<16:
    result.append("0")
result="".join(result)
result=result[::-1]
result=result[8:16]+result[0:8]
result=int(result,2)
print(result)

#или бинарными операциями
num=10111
b1 = num & 0xff
b2 = num >> 8
result = (b1 << 8) | b2
print(result)
