#Q1: Installed Python.
#Q2: Perform tasks on Shell.
print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a=20
a+=30
a%=3
print(a)
print(True*False)
print(True&False)
print(True and False)
print((6>3) and (7<4) or (18==3) and (9>3))
print(True is False)
#print(False in 'False')
#TypeError: 'in <string>' requires string as left operand, not bool
print(((True==False) or (False>True)) and (False<=True))
#Q3: addin strings;
s1="Nice to have it"
s2=" here"
print(s1+s2)
#Q4:grab "hello" from the list;
a= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])
#Q5:adding strings to list.
a=[s1]+a
a=a+[s2]
print(a)
#Q6: Subtracting sets
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)
#Q7: Program to find if given input is pangram or not;
string=input('Enter the string:')
l=[False]*26
for i in string.lower():
    if not i==' ':
        l[ord(i)-ord('a')]=True
for i in l:
    if(i==False):
        print('given string is not pangram')
        break
    else:
        print('It is a pangram')
        break
#Q8:
b= input('Enter an interger:')
b= '{0}+{0}{0}+{0}{0}{0}'.format(b)
print(eval(b))
#Q9:spit and arrange;
string=input('words separated by comma:')
s=string.split(',')
s.sort()
print(s)
#Q10:
d = {'Student': ['Rahul', 'Kishore','Vidhya', 'Raakhi'], 
'Marks': [57,87,67,79]}
Max=max(d['Marks'])
I=d['Marks'].index(Max)
print(d['Student'][I])


        
        
        




