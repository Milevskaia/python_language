#task1--------------------------
"""
���� ������ �������������� �����: x1, y1, x2, y2.
 �������� ������� distance(x1, y1, x2, y2),
 ����������� ���������� ����� ������ (x1,y1) � (x2,y2).
 �������� ������ �������������� ����� � �������� ��������� ������ ���� �������.
"""
def distance(x1, y1, x2, y2):

    res = 0
    res = ((x1 - x2)**2 + (y1 - y2)**2) ** (1/2)

    return res



x1 = float(input())

y1 = float(input())

x2 = float(input())

y2 = float(input())

dis = distance(x1, y1, x2, y2)

print (dis)
#-----------------------------
#task2--------------------------
"""
���� �������������� ������������� ����� a � ����e ����� n.

��������� an. ������� �������� � ���� ������� power(a, n).

����������� �������� ���������� � ������� ������������ ������.
"""

def power(a, n):

    res = 1

    for i in range(abs(n)):

        res *= a

    if n >= 0:

        return res
    else:

        return 1 / res



a = float(input())

n = int(input())


print (power(a, n))


#-----------------------------

#task3--------------------------
"""
���� �������������� ������������� ����� a � ����� ��������������� ����� n.
 ��������� an �� ��������� �����, ���������� � ������� ����� ** � ������� math.pow(),
 � ��������� ������������ ����������� an=a?an-1.
"""

def power(a, n):

    if n == 0:

        return 1

    else:

        return a * power(a, n - 1)



a = float(input())

n = int(input())


print (power(a, n))

#-----------------------------

#task4--------------------------
"""
�������� ������� fib(n),
 ������� �� ������� ������ ����������������
 n ���������� n-e ����� ���������.
"""

def fib(n):

    if n == 1 or n == 2:

        return 1
    else:

        return fib(n - 1) + fib(n - 2)



n = int(input())


print (fib(n))
#-----------------------------