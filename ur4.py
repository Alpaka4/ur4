###If1. Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае не изменять его. Вывести полученное число.
##print("введите целое число")
##a=int(input())
##if a>0:
##    a=a+1
##print(a)
###If2. Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае вычесть из него 2. Вывести полученное число.
##print("введите целое число")
##a=int(input())
##if a>0:
##    a=a+1
##else:
##    a=a-2
##print(a)
####If3. Дано целое число. Если оно является положительным, то прибавить к нему 1; если отрицательным, то вычесть из него 2; если нулевым, то заменить его на 10. Вывести полученное число.
##print("введите целое число")
##a=int(input())
##if a>0:
##    a=a+1
##elif a<0:
##    a=a-2
##else:
##    a=10
##print(a)
###If4◦ Даны три целых числа. Найти количество положительных чисел в исходном наборе.
##print("введите три целых числа")
##a=int(input())
##b=int(input())
##c=int(input())
##k=0
##if a>0:
##    k+=1
##if b>0:
##    k+=1
##if c>0:
##    k+=1
##print(k)
###If5. Даны три целых числа. Найти количество положительных и количество отрицательных чисел в исходном наборе.
##print("введите три целых числа")
##a=int(input())
##b=int(input())
##c=int(input())
##k=0
##o=0
##if a>0:
##    k+=1
##else:
##    o+=1
##if b>0:
##    k+=1
##else:
##    o+=1
##if c>0:
##    k+=1
##else:
##    o+=1
##print(k)
##print(o)
###If6◦Даны два числа. Вывести большее из них
##print("введите два числа")
##a=int(input())
##b=int(input())
##if a>b:
##    print(a)
##else:
##    print(b)
###If7. Даны два числа. Вывести порядковый номер меньшего из них.
##print("введите два числа")
##a=int(input())
##b=int(input())
##if a>b:
##    b=2
##    print(b)
##else:
##    a=1
##    print(a)
###If8◦Даны два числа. Вывести вначале большее, а затем меньшее из них.
##print("введите два числа")
##a=int(input())
##b=int(input())
##if a>b:
##    print(a)
##    print(b)
##else:
##    print(b)
##    print(a)
###If9. Даны две переменные вещественного типа: A, B. Перераспределить значения данных переменных так, чтобы в A оказалось меньшее из значений,а в B — большее. Вывести новые значения переменных A и B.
##print("введите два числа вещественного типа")
##a=float(input())
##b=float(input())
##t=0
##if a>b:
##    t=a
##    a=b
##    b=t
##    print(a)
##    print(b)
##elif a<b:
##    print(a)
##    print(b)
##If10. Даны две переменные целого типа: A и B. Если их значения не равны,то присвоить каждой переменной сумму этих значений, а если равны,
##то присвоить переменным нулевые значения. Вывести новые значения переменных A и B.
##print("введите два числа целого типа")
##a=int(input())
##b=int(input())
##if a!=b:
##    a=a+b
##    b=a+b
##elif a==b:
##    a=0
##    b=0
##print(a)
##print(b)
##If11. Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной большее из этих значений, а если равны,
##то присвоить переменным нулевые значения. Вывести новые значения переменных A и B
##print("введите два числа целого типа")
##a=int(input())
##b=int(input())
##if a!= b:
##    if a > b:
##        b = a
##    else:
##        a = b
##else:
##    a=0
##    b=0
##print(a)
##print(b)
###If12◦Даны три числа. Найти наименьшее из них    
##print("введите три числа")
##a=int(input())
##b=int(input())
##c=int(input())
##if a>b>c:
##    print(c)
##if c>b>a:
##    print(a)
##if a>c>b:
##    print(b)
###If13. Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим).
##print("введите три числа")
##a=int(input())
##b=int(input())
##c=int(input())
##if a<b<c:
##    print(b)
##elif c>b>a:
##    print(b)
##if b<c<a:
##    print(c)
##elif a>c>b:
##    print(c)
##if b<a<c:
##    print(a)
##elif c>a>b:
##    print(a)
###If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.
##print("введите три числа")
##a=int(input())
##b=int(input())
##c=int(input())
##if a>b>c:
##    print(c)
##    print(a)
##elif b>a>c:
##    print(c)
##    print(b)
##elif c>b>a:
##    print(a)
##    print(c)
###If15. Даны три числа. Найти сумму двух наибольших из них.
##print("введите три числа")
##a=int(input())
##b=int(input())
##c=int(input())
##if a>b>c:
##    res=a+b
##    print(res)
##elif a>c>b:
##    res=a+c
##    print(res)
##elif c>b>a:
##    res=c+b
##    print(res)
###If16. Даны три переменные вещественного типа: A, B, C. Если их значения упорядочены по возрастанию, то удвоить их; в противном случае заменить значение каждой переменной на противоположное. Вывести новые значения переменных A, B, C
##print("введите три числа вещественного типа")
##a=float(input())
##b=float(input())
##c=float(input())
##if a<b<c:
##    a=a*2
##    b=b*2
##    c=c*2
##    print(a)
##    print(b)
##    print(c)
##else:
##    a=a*(-1)
##    b=b*(-1)
##    c=c*(-1)
##    print(a)
##    print(b)
##    print(c)
##If17. Даны три переменные вещественного типа: A, B, C. Если их значения упорядочены по возрастанию или убыванию, то удвоить их; в противном случае заменить значение каждой переменной на противоположное.
##Вывести новые значения переменных A, B, C.   
print("введите три числа вещественного типа")
a=float(input())
b=float(input())
c=float(input())
if (a<b<c) or (a>b>c):
    a=a*2
    b=b*2
    c=c*2
    print(a)
    print(b)
    print(c)
else:
    a=a*(-1)
    b=b*(-1)
    c=c*(-1)
    print(a)
    print(b)
    print(c)
    

