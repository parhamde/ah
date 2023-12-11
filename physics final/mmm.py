import matplotlib.pylab as plt

# Section 1
x0 = eval(input("please enter x0 : "))
v0 = eval(input("please enter v0 : "))
a = eval(input("please enter a : "))
ti = eval(input("plaese enter t : "))
time = range(ti+1)


# Section 2f
x = []

for t in time:
    x1 = (0.5*a*(t*t))+(v0*t)+x0
    x.append(x1)

# Section 3
v = []

for t in time:
    v1 = (a*t)+v0
    v.append(v1)

# Section 4
a = [a]*((ti+1))
plt.plot(time,x,maker="*",color="r",label="Displacement")
plt.plot(time,v,"bs",label="velocity")
plt.plot(time,a,label="Acceleration")
plt.legend(loc="upper left")
plt.xlabel("time")
plt.ylabel("X,V,A")
plt.title("full plot")
plt.show()