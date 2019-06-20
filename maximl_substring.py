def distinct_char(st):
    c=0
    li=[]
    st=list(st)
    for i in range(len(st)):
        if st.count(st[i])==1:
            c+=1
        else:
            c=0
            break
    return c

def substr(st):
    ans=0
    n=len(st)
    for i in range(n):
        for j in range(n+1):
            ele=st[i:j]
            max=distinct_char(ele)
            if max!=0:
                if max>ans:
                    ans=max
    return ans
    
if __name__ == "__main__":
    st=input()
    print(substr(st))
    
