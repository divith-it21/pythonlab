def add(a,b):
    print(a,'+',b,'=',(a+b))
def sub(a,b):
    print(a,'-',b,'=',(a-b))
def mul(a,b):
    print(a,'*',b,'=',(a*b))
def div(a,b):
    print(a,'/',b,'=',(a/b))
a=input("Enter a choice:")
b=int(input("Enter num1"))
c=int(input("Enter num2"))
if a=='+':
   add(b,c)
elif a=='-':
   sub(b,c)
elif a=='*':
   mul(b,c)
elif a=='/':
   div(b,c)
else:
   print("Enter a valid choice")
