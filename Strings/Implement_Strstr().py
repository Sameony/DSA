def strStr(self, haystack: str, needle: str) -> int:
    try:
        if len(needle)==0 or haystack==needle:
            return 0
        if len(haystack)==0:
            return -1
        return (haystack.index(needle))
    except ValueError:
        return -1


def strStrRabin(self, haystack: str, needle: str) -> int:
    if len(needle)==0 or haystack==needle:
        return 0
    if len(haystack)==0:
        return -1
        
    d={}
    i=97
    for j in range(26):
        a=chr(i+j)
        d[a]=j+1
        
    def h(word: str) -> int:
        s=0
        for i in word:
            s+=d.get(i)
        return s
        
        
    flag=0
    l1=h(needle)
    l2=len(needle)
    i,j=0,l2-1
    while haystack[j]:
        if h(haystack[i:j+1])==l1:
            if haystack[i:j+1]==needle:
                flag=1
                return i
        i+=1
        j+=1
    if flag==0:
        return -1
            
        
    