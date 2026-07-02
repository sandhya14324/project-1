a="hello 1234 @#$"
# b=a.split()
# sum=0
# print(b)
# for i in range(len(b)):
#     for j in range(len(b[i])):
#         if b[i][j]>="0"and b[i][j]<="9":
#             sum=sum+int(b[i][j])
# print(sum)    
# ch=""
# for i in range(len(b)):
#     if "hello"in a:
# print(a)        
sum=0
ch=""
sc=""
for i in range(len(a)):
    if a[i]>="a" and a[i]<="z":
        ch=ch+a[i]
    elif a[i]>="0" and a[i]<="9":
        sum=sum+int(a[i])
    else:
        sc=sc+a[i]
print("word",ch)
print("sum of numbers",sum)
print("special characters",sc)                    
        
       
                 

