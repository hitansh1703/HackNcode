n=int(input("enter the end limit "))
n1, n2=0,1
c=0
print( n1,"\n",n2)
for i in range(2,n):
    f=n1+n2
    print(" ",f)
    n1=n2
    n2=f
