x=[1,2,3,4,["students","records","course",
            ("my course",("python","sql","DS","ML","DevOps"))]]


i = x[4][3]

i = list(i)

print(i)

z = x[4][3][1]
print(z)

z=list(z)

z[3] = "AI"

print(z)

x[4][3] = z

print(z)

z = tuple(z)


print(x)



