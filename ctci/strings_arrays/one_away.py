

def one_away(str1,str2,m=0,n=0,count=0):
    if m == len(str1):
        return len(str2) -n + count <= 1
    if n == len(str2):
        return len(str1) -n + count <= 1
    if str1[m] == str2[n]:
        return one_away(str1,str2,m+1,n+1,count)
    else:
        return one_away(str1,str2,m,n+1,count+1) or one_away(str1,str2,m+1,n,count+1) or one_away(str1,str2,m+1,n+1,count+1)


print(one_away('pale','ple'))
print(one_away('pale','pleb'))
print(one_away('word','ward'))
print(one_away('abcd','efgh'))
    
