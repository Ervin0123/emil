szamok=[3,4,5,6,7,8,91,2,3]
osszeg=0
szorzat=1
for x in szamok:
    osszeg=osszeg+x
    szorzat=szorzat*x
print(osszeg)
print(szorzat)
print (sum(szamok))
vane=False
for x in szamok:
    if (x==1):
        vane=True
if (vane==True):
    print("van")
else:
    print("nincs")