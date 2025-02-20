# num=input("enter a number : ")
# sum=0
# for i in range(0,len(num)):
#     # print(i,num[i])
#     sum=sum+i
# print(sum)

# 2nd quesn :
def even_odd(a):
    if a%2==0:     
        print("even")
    else:
        print("odd") 
even_odd(5)
# without funcns:
num=float(input("enter a number : "))
if num%2!=0:
    print("odd")
else:
    print("even")

# 3rd quesn:
age=int(input("enter a number : "))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible, eligible after",18-age,"years")

# 4th quesn :
def greatest_num(num1,num2):
    if num1>num2:
        print(num1,"is greater than",num2)
    elif num1==num2:
        print("equal")
    else:
        print(num2,"is greater than",num1)
greatest_num(9,9)       

# 5th quesn :
marksOfStudents=float(input("enter your marks : "))
if marksOfStudents > 40:
    print("pass")
else:
    print("fail")

# using terinary operator:
n=90
res="pass" if n>=40 else "fail"
print(res)

# 6th quesn :
dayOfTheWeek=int(input("enter a number : "))
if dayOfTheWeek==1:
    print("monday")
elif dayOfTheWeek==2:
    print("tuesday")
elif dayOfTheWeek==3:
    print("wednesday")
elif dayOfTheWeek==4:
    print("thurssday")
elif dayOfTheWeek==5:
    print("friday")
elif dayOfTheWeek==6:
    print("saturday")
elif dayOfTheWeek==7:
    print("sunday")
else:
    print("enter blw 1-7 numbers")

# 8th quesn :
monthNumber=int(input("enter a number : "))
if monthNumber==1:
    print("january")
elif monthNumber==2:
    print("feb")
elif monthNumber==3:
    print("march")
elif monthNumber==4:
    print("april")
elif monthNumber==5:
    print("may")
elif monthNumber==6:
    print("june")
elif monthNumber==7:
    print("july")
elif monthNumber==8:
    print("august")
elif monthNumber==9:
    print("sep")
elif monthNumber==10:
    print("oct")
elif monthNumber==11:
    print("nov")
elif monthNumber==12:
    print("dec")  
else:
    print("enter blw 1-12 numbers")

# 7th quesn : 
operation=input("enter operation to perform : ").lower()
num1=int(input("enter a number : "))
num2=int(input("enter another number : "))
if operation=="add" or operation=="+":
    print(num1 + num2)
elif operation=="sub" or operation=="-":
    print("num1-num2")
elif operation=="mul" or operation=="*":
    print("num1*num2")
elif operation=="div" or operation=="/":
    if num2==0:
        print("invalid")
    else:
        print(num1/num2)


#     medium questions :
#     -------------------

# Write a program to find the greatest of three numbers. (1st quesn)
def greatest_of_numbers(n1,n2,n3):
    if n1>n2 and n1>n3:
       return n1,'is greatest'
    elif n2>n3:
       return n2,"is greatest."
    elif n3>n1:
        return n3,"is greatest."
res=greatest_of_numbers(9,1,8)  
print(res)

# Check if a year is a leap year (2nd quesn)
def leap_year(year):
    if (year%100==0) and (year%400==0):
        return "leap year"
    elif (year%100!=0) and(year%4==0):
        return "leap year"
    else:
        return "not a leap year"
temp=leap_year(2024)
print(temp)

# 4th quesn :
marks=int(input("enter your marks : "))
if marks>=90 and marks<=100 :
    print("Grade A")
elif marks>=80 and marks<90  :
    print("Grade B")
elif marks>=70 and marks<80 :
    print("Grade C")
elif marks<70 and marks>=0:
    print("fail")
else:
    print("invalid")

# 5th quesn :
def triangle(s1,s2,s3):
    if (s1+s2)<s3 or (s2+s3)<s1 or (s3+s1)<s2:
       return "triangle formed"
    else:
        return "not possible"
res=triangle(10,20,40)
print(res)