#1 5 11 20
n = int(input("Digite qual o valor do troco: "))
cont = []
i = 0


while (i != 1):
    if ((n-20) >=0):
        cont.append('20') 
        n -= 20
    elif ((n-11 >=0)):
        cont.append('11')
        n -= 11
    elif ((n-5) >=0):
        cont.append('5')
        n -= 5
    else:
        cont.append('1')
        n -=1
    if(n==0):
        i = 1
print(cont)