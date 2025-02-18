str="kalki 2898ad"
print(id(str[1]))
print(id(str[0]))
print(id(str[2]))
print(id(str[3]))
print(id(str[4]))
print(id(str[5]))
print(id(str[6]))

#
a=[1,2,3,4,5]
print((list(a)))
print(id(list[0]))
print(id(list[1]))
print(id(list[2]))
print(id(a[1]))

#range
print(list(range(100,0,-1)))
print(list(range(0,100,-1)))
print(list(range(0,100,3)))
print(list(range(0,5)))
print(list(range(100,47,-1)))

#
list1=[1,2,3,6,99]
for i in list1:
    print(len(list1))
    for i in range(0, len(list1)):
     print(i,list[i])
     num1=10
     for j in range(0,num1):
        print(j)

    #dictionary
    dict1={1:'darling',2:'mirchi',3:'sahoo',4:'bahubali',5:'salaar'}
    print(dict1)
    print(dict1[1])
    dict1[3]='kalki'
    print(dict1)
    dict1['key1']='value'
    print(dict1)
    dict1['key1']='updated value'
    print(dict1)

    #set
    set={1,2,3,1,2,3,3,3,3,}
print(set)
set1={35872,549687,74569238,63436,63436,63436,'vani1','vani2'}
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)
print(set1)

#order
set2={1,1,2,2,3,3,4,4,5,5}
print(set2)

num1=5
num1=None
print(num1)
print(type(num1))
print(id(num1))

a=int(input("enter a number1"))
b=int(input("enter a number2"))
print(type(a))
print(type(b))
print(a+b)