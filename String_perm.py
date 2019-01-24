def string_perm(string1,string2):
    i=0
    j=0
    #check which string is smaller
    if(len(string1)<len(string2)):
        m=len(string1)
        n=len(string2)
        a=1
    else:
        m=len(string2)
        n=len(string1)
        a=0

    while j < m and i < n:
        if(a==1):
            if string1[j] == string2[i]:
                j = j + 1
            i = i + 1
        elif(a==0):
            if string1[i] == string2[j]:
                j = j + 1
            i = i + 1
    return j == m

if __name__ == '__main__':

    s1 = ""
    s2 = "a"
    if (string_perm(s1, s2)):
        print("YES")
    else:
        print("NO")