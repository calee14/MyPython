# Page 220 question 20
def foo(x):
 return x*x/4000.0-((0.6)*(x))+365.0
count=400.0
total = 0.0
while(count<=2000):
 cable = foo(count)
 total += cable
 print(cable)
 count+=20.0
print(total)
