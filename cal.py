print("1-ADD")
print("2-SUBRACT")
print("3-MULTIPLY")
print("4-DIVIDE")
a=int(input("Enter a choice:"))
b=int(input("Enter a num1"))
c=int(input("Enter a num2"))
if a==1:
print("You had chosen addition")
print(b,'+',c,'=',(b+c))
elif a==2:
print("you had chosen subtraction")
print(b,'-',c,'=',(b-c))
elif a==3:
print("You had chosen multiplication")
print(b,'x',c,'=',(b*c))
elif a==4:
print("You had chosen division")
print(b,'/',c,'=',(b/c))
else:
print("Enter a valid choice")
