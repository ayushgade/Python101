a = int(input())
b=input()
c=input()
st=[]
for x in b:
    for y in c:
        if( x == " "):
            break
        elif(x >= y):
            print(x)
            print(y)
            st.append(1)
            break
        else:
            st.append(0)
            break

print(st)