#task1------------------------------------------------------------
"""
�������� ��������, ��� ������ ��� ����� � ����� �� ����. ����� ����� ���������� ������� � �������� �����. 
������ ����: 3 ������ �����. ����� ����� ���������� ������� � �������� �����. 
������� ����: ������� ���� ����� ����� �� �����. 
"""
a1=input('vvedite pervoe chislo: ')
a2=input('vvedite vtoroe chislo: ')
a3=input('vvedite trete chislo: ')
print('vash resultat: ', float(a1)+float(a2)+float(a3))

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
�������� ��������, ��� ������ ������� ���� ������ ������������ ���������� �� �������� ���� �����. ���������� ������� ������� ������ � ������� ������. 
������ ����: 2 ������ �����. ����� ����� ���������� ������� � �������� �����. 
������� ����: ������� ����� ���������� �� �����. 
"""
a1=input('vvedite dlinu pervogo kateta: ')
a2=input('vvedite dlinu vtorogo kateta: ')
print('ploshad vashego treugolnika ravna: ', (float(a1)*float(a2))/2)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
N �������� �������� K ����� � ���������� �� �� ����� ������. ��������� ������ ���������� � ������. ������ ����� ������ ����� �������?  ������ ����� �������� � ������? 
�������� ������ ����� N � K. ���� ������� ������� ��� �����: ������ �� ���������� ���� �������. 
������ ����: 2 ����� �����. ����� ���������� ������� � �������� �����. 
������� ����: ������� ��� �����. ����� � ������� ����� � ��������, ����� � ������� �����, �� �������� � ������. 
"""
N=input('vvedite kol-vo studentov: ')
K=input('vvedite kol-vo yablok: ')
print('kol-vo yablok u studenta: ', int(K)//int(N))
print('kol-vo yablok ostavshihsya v koshiku: ',int(K)%int(N))

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
�����: ����� ����� N - ������� ������, ����������� ���� ������. ������ ����� � ������ ���� ���������� �������� ��������, ���� �� ���� ����� 00:00?
�������� ������� �������� ��� �����: ������� ����� (�� 0 �� 23) � ������� ������ (�� 0 �� 59). ³����� �� �����, �� ��������� � ������ ���� ������ ������� ����, ���� ����� N ���� ���� ��������� �������.
������ ����: 1 ���� �����, �� ������� ����������
������� ����: ������� ��� �����. ����� - ������, ����� - �������.
"""
n=int(input( �vvedite kol-vo proshedshih minut�))
print(�kol-vo chasov: �,(n//60)%24)
print(�kol-vo secund: �,(n*60))


#-----------------------------------------------------------------


#task5------------------------------------------------------------
"""
�������� ��������, ��� ��� �����������, �������� ����� "Hello", ��'� ����������� � ���� ������ ���� �����. ��������� �Hello, Mike!�
������ ����: ��'� �����������
������� ����: ������� ����� ���������
"""
x=input( �vvedite imya:  �)
print("Hello,"+x+"!")
#-----------------------------------------------------------------


#task6------------------------------------------------------------
"""
�������� ��������, ��� ����� ���� ����� � ����� ���� ��������� � �������� �������� �� ��������:
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
������ ����: ���� �����
������� ����: ��� ����� �� ��������� � �������� ��������.
"""
x=input("vvedite chislo ")
print("The next number for the number "+x+" is "+str(int(x)+1)+".")
print("The previous number for the number "+x+" is "+str(int(x)-1)+".")

#-----------------------------------------------------------------


#task7------------------------------------------------------------
"""
����� ������� ���������� ��� ��� ����� ����� �� ������ �� ����� �����. � ������� ���� ��������� ���������� ����� ��� �����, � ����������, �� �� ����� ������ ���� ����� �� ����� ���� �����. ��� ��������� ������� ����� ��������� ��������?
������ ����: 3 ����� ����� - ������� ����� � ������ ����.  ����� ����� ���������� ������� � �������� �����.
������� ����: ����� - ������� �����.
"""
x1=int(input('vvedite kol-vo chelovek v pervoi gruppe: '))
x2=int(input('vvedite kol-vo chelovek vo vtoroy gruppe: '))
x3=int(input('vvedite kol-vo chelovek v tretey gruppe: '))
y=(x1+x2+x3)
z=y/2
if (y%2=1) :
            z=z+1
print('obshee kol-vo stolov: ',z)
#-----------------------------------------------------------------

