# section 1

v0 = eval(input("Please enter v0 : "))
v0 *=1600/3600 # v0 = v0 * 1600 +-*/**

a = eval(input("Enter a (enter positive): "))

# v = at+v0 ==> t=v0/a
t = v0/a

t_delay = eval(input("Please enter t delay : "))

print(f"Total time is : {t+t_delay} s")

# section 2

# x=vt+x0
x_delay = v0*t_delay

x_break = ((1/2)*(-a)*(t**2)) + (v0*t)

x_total = x_delay + x_break
print(f"Total x is : {x_total} m")