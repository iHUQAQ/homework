#ax^2+bx+c=0
import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
dlt=b*b-4*a*c
if dlt>=0:
    as1=(-b+math.sqrt(dlt))/2/a
    as2=(-b-math.sqrt(dlt))/2/a
    if dlt==0:
        print("有唯一根：x=",as1)
    else:
        print("x1=",as1,"x2=",as2)
else:
    print("无实数根")
