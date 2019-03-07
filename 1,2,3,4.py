for i in range(56,101):
    y=2*i**2+2*i+2
    print(y)

############################

def silnia(s):
    if s<2 and s>=0:
        return 1
    else:
        for i in range(2,s):
            s*=i
        return s

i=0
while i==0:
        try:
            s=int(input('Podaj liczbe nieujemną:'))
            if s<0:
               print('Podałeś liczbę ujemną')
            else:
               print('Podałeś:',s,'jego silnia wynosi:',silnia(s))
               i+=1
        except ValueError:
            print('Musisz podać poprawną lizcbę')

############################

def minimum():
    array=[]
    number = int(input("Ile chcesz miec elementów na liscie?"))
    for i in range(number):
        n = int(input('Wprowadź liczbe:'))
        array.append(n)
    print(array)
    x = 0
    z=[]
    for j in range(len(array)):
        if array[x]> array[j]:
            x=j
    for i in range(len(array)):
        if array[x] == array[x + i]:
            z.append(i)

    return array[x],z

print(minimum())

#############################

from numpy import *
from matplotlib.pyplot import*
a = float(input("W jakim punkcie zacząć wykres?"))
b = float(input("Jaka ma być długosc wykresu?"))
x = linspace(a,a+b)
y = 5*x
plot(x,y)
show()