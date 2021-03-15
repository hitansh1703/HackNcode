l=[]
n=int(input("enter the no. of element "))
print("enter elements ")
for k in range(0,n):
    e = int(input())
    l.append(e)
print("*"*50)
for i in l:
    if i >=0:
        print(i," ")
