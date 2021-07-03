class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        if len(a)<len(b):
            a,b=b,a
        s=len(b)-1
        x=""
        for i in a[::-1]:
            if s>=0:
                c2=b[s]
            else:
                c2=0
            if i=='1':
                if c2=='1':
                    if carry==1:
                        x=x+"1"
                    else:
                        x+="0"
                        carry=1
                else:
                    if carry==1:
                        x+="0"
                        carry=1
                    else:
                        x+="1"
            else:
                if c2=='1':
                    if carry==1:
                        x=x+"0"
                        carry=1
                    else:
                        x+="1"
                            
                else:
                    if carry==1:
                        x+="1"
                        carry=0
                    else:
                        x+="0"
            s-=1
        if carry ==1:
            x+='1'
        return(x[::-1])
            
            