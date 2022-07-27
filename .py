m1+m2+m3=[int(x) for x in input("enter 3 subjects marks").split()]
t0tal=m1+m2+m3
avg=total/3
print("total=%d/n average = %f"%(total ,avg))
if m1>=40 and m2>=40 m3>=40:
print("student passed")
else:
print("student failed")