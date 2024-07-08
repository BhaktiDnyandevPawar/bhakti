s=input("Enter the string = ")
lc=0
uc=0
nc=0
sc=0
for i in range (len(s)):
    if 'A'<= s[i] <='Z':
       lc+=1
    elif 'a'<=s[i] <='z':
       uc+=1
    elif'0'<= s[i] <='9':
        nc+=0 
    else :
         sc+=1
if(lc!=0 and uc!=0 and nc !=0 and sc!=0):
    print("valid password")
else:
    print("invalid password")    