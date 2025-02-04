# task-1

list1=[1,2,3,4,5]
list2=["a","b","c","2"]
print("list1 : ",list1)
print("list2 : ",list2)
for i in list1:
  if i%2==0:
     list2=list2+[i]
     print("new list : ",list2)

# task-3

input_list=["abcd","efgh","ghifh","dskf","sdddfsdf"]
fl=input_list[0][0]+input_list[1][0]+input_list[2][0]+input_list[3][0]+input_list[4][0]
print(f'"{fl}"')

# task-4

name="python"
print("length of name : ",len(name))
a=name[5]+name[4]+name[3]+name[2]+name[1]+name[0]
print("reverse name : ",a)