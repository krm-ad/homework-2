# Exercise A

year = int(input())

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("YES")
else:
    print("NO")

# Exercise B

r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
if r1 == r2 or c1 == c2:
    print('YES')
else:
    print('NO')

# Exercise C

r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
if abs(r1 - r2) == abs(c1 - c2):
    print('YES')
else:
    print('NO')

# Exercise D

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")

# Exercise E

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("YES")
else:
    print("NO")

# Exercise F

n = int(input())
m = int(input())
k = int(input())

if 0 < k < n * m and (k % n == 0 or k % m == 0):
    print("YES")
else:
    print("NO")

# Exercise G

k = int(input())

if k == 1 or k % 4 == 0:
    print("YES")
else:
    print("NO")

# Exercise H

a = int(input())
b = int(input())

if a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
else:
    if b % a == 0:
        print(-b // a)
    else:
        print("NO")

# Exercise I

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0:
    if b == 0:
        print("INF")
    else:
        print("NO")
else:
    if b % a == 0:
        x = -b // a
        if c * x + d != 0:
            print(x)
        else:
            print("NO")
    else:
        print("NO")

# Exercise J

a = int(input())
b = int(input())
c = int(input())
d = int(input())

change = (c * 100 + d) - (a * 100 + b)
print(change // 100, change % 100)

# Exercise K

k = int(input())

if k in (1, 2, 4, 7):
    print("NO")
else:
    print("YES")

# Exercise L

k = int(input())
m = int(input())
n = int(input())

if n == 0:
    print(0)
else:
    rounds = (2 * n + k - 1) // k
    if rounds < 2:
        rounds = 2
    print(rounds * m)

# Exercise M

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 > 0) == (x2 > 0) and (y1 > 0) == (y2 > 0):
    print("YES")
else:
    print("NO")

# Exercise N

a = int(input())
b = int(input())

print(max(a, b))

# Exercise O

a = int(input())
b = int(input())

if a > b:
    print(1)
elif b > a:
    print(2)
else:
    print(0)

