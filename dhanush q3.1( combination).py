first=int(input("enter first number:"))
second=int(input("enter secod number:"))
third=int(input("enter the third number:"))

list=[ ]
list.append(first)
list.append(second)
list.append(third)
for i in range (3):
    for j in range (3):
        if  (i !=j and j! =k and i!=k):
            print (list [i],list [j],list[k])
