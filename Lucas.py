num1,first,second,count=int(input("Number: ")),1,3,1
print("\n",first,"\n","\n",second)
while count<=num1:
    third=first+second
    print("\n",third)
    first=second
    second=third    
    count+=1