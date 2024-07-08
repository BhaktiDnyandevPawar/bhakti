def add(x,y):
    return x+y

print("------------")     
a=int(input("enter value of a="))
b=int(input("enter value of b="))
c=int(input("enter value of c="))
d=int(input("enter value of d="))
e=add(a,b)
f=add(c,d)
print("------------")
print("add a+b=",e)
print("add c+d=",f)
print("add a+b+c+d=",add(e,f))
print("------------")
