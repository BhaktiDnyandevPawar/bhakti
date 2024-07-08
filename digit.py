num=int(input("Enter the number"))
no=num
l=no%10
print("last digit=",int(l))
while no>10 :
    r=no/10
    no=no/10
    print("first digit=",int(r))
    no+=1


