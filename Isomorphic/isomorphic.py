s = input()
t = input()

if (len(s) != len(t)):
    print("False")
if (len(sorted(set(s))) != len(sorted(set(t)))):
    print("False")
for i in range(len(s)):
    s = s.replace(s[i], t[i])
    print(s)
if (s == t):
    print("True")
print("False")
