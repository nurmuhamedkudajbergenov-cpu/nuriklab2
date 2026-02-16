n=int(input())
s=list(str, input().split())
c=0
for i in range(n):
    for j in range(n):
        if s[j]==s[i]:
            c+=1
print(n-c)    
