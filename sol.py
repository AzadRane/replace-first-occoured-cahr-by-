//coded by harish rane
s = input("enter the string")
fo = s[:1:]
s = s[1:]
replace  = s.replace(fo,'$')
s = fo+replace
print(s)
