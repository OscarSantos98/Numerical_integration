import sympy as sp

x = sp.Symbol('x')
f = (x**3)/(1+x**(1/2))
print('Integrate the following algebraic expression from 1 to 2')
sp.pprint(f)

lim_inf=1
lim_sup=2
# Numerical integration by Simpson 1/3 method
print('\nSimpson 1/3\n')
n = 2   # For Simpson 1/3 n=2
h = (lim_sup-lim_inf)/n
x0 = lim_inf
f0 = f.subs(x,x0)
x1 = x0+h
f1 = f.subs(x,x1)
x2 = x1+h
f2 = f.subs(x,x2)
print('h = ',h,'\nx0 = ',x0,'\nf0 = ',f0,'\nx1 = ',x1,'\nf1 = ',f1,'\nx2 = ',x2,'\nf2 = ',f2)
I = (h/3)*(f0+4*f1+f2)
print('Result = ',I)

# Numerical integration by Simpson 3/8 method
print('\nSimpson 3/8\n')
n = 3   # For Simpson 3/8 n=3
h = (lim_sup-lim_inf)/n
x0 = lim_inf
f0 = f.subs(x,x0)
x1 = x0+h
f1 = f.subs(x,x1)
x2 = x1+h
f2 = f.subs(x,x2)
x3 = x2+h
f3 = f.subs(x,x3)
print('h = ',h,'\nx0 = ',x0,'\nf0 = ',f0,'\nx1 = ',x1,'\nf1 = ',f1,'\nx2 = ',x2,'\nf2 = ',f2,'\nx3 = ',x3,'\nf3 = ',f3)
I = (3*h/8)*(f0+3*f1+3*f2+f3)
print('Result = ',I)
