# Type conversion 
# Explisit (manual)

a = 12.5
a = int(a)
print(a)
print(type(a))

b = "12"
b = float(b)
print(b)
print(type(b))

A = 1222
A = str(A)
print(type(A))
print(A)


# boolean

a = 12
b = 0
c = 12.4
e = ""
f = "hello"
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(e))
print(bool(f))

#  7 values false 
"""
False 
0,0.0,"",[],(),{}

True 
11,12.4,"helllo",

"""

# Implicit (automatic)

a = 12
print(a/2)

