#Compares letters on basis of ascii values
x="ABX">"ABY"
#F coz Y>X
y="abx"<="ABX"
#F coz smaller cases have higher ascii (a=97, A=65)
z="sameer"!="SAmeer"
#true coz... sameer and SAmeer equality not true....
w="aab" == "baa"
#yeah...false
u="abce" >= "abcdef"
#True coz e>d
print(x,y,z,w,u)