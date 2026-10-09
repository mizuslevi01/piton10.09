meresek = [42, 55, -1, 61, 48, -1, 70, 66]
db = 0
ossz = 0
for meres in meresek:
    if meres != -1:
        db = db + 1
        ossz = ossz + meres
atlag = ossz / db               
print(f"2. feladat: Érvényes mérések: {db}, átlag: {atlag}")


szoveg = []
for ora in range(len(meresek) // 2):
    ora_osszeg = 0
    for index in (2 * ora, 2 * ora + 1):
        if meresek[index] != -1:     
            ora_osszeg = ora_osszeg + meresek[index]
    szoveg.append(f"{8 + ora} órától {ora_osszeg}")
print("3. feladat: " + ", ".join(szoveg))


legnagyobb = meresek[0]
legnagyobb_index = 0
for i in range(1, len(meresek)):
    if meresek[i] > legnagyobb:      
        legnagyobb = meresek[i]
        legnagyobb_index = i

percek = legnagyobb_index * 30
ora = 8 + percek // 60
perc = percek % 60
print(f"4. feladat: A legnagyobb érték: {legnagyobb}, időpontja: {ora}:{perc:02d}")
