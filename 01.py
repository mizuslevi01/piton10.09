lepesek = [6500, 8200, 4300, 10100, 7600, 12000, 5400, 9800, 3900, 11200]

ossz = 0
for lepes in lepesek:
    ossz = ossz + lepes

atlag = ossz / len(lepesek)
print(f"2. feladat: Összesen {ossz} lépés, átlag: {atlag}")

legtobb = lepesek[0]
max_nap = 1                      
for i in range(1, len(lepesek)):
    
    if lepesek[i] > legtobb:
        legtobb = lepesek[i]
        max_nap = i + 1          
print(f"3. feladat: A legtöbb lépés: {legtobb}, a {max_nap}. napon.")

darab = 0
for lepes in lepesek:
    if lepes >= 10000:
        darab = darab + 1
print(f"4. feladat: {darab} napon volt legalább 10000 lépés.")
