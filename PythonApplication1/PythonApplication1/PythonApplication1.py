szamok=[3,4,5,6,7,8,91,2,3]
osszeg=0
szorzat=1
megsz=0
for x in szamok:
    osszeg=osszeg+x
    szorzat=szorzat*x
    megsz=megsz+1
print("összeg:", osszeg)
print("szorzat:", szorzat)
print("megszámlálás:", megsz)
print (sum(szamok))
print("max:", max(szamok))
print("min:", min(szamok))
print()
vane=False
for x in szamok:
    if (x==1):
        vane=True
if (vane==True):
    print("van")
else:
    print("nincs")
#
db=0
a=int(input("melyik számot keresed?"))
for x in szamok:
    if (x==a):
        db=db+1
print ("ennyi", a, "van a listában:", db)
