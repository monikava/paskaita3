import random

# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.
print("")
print("task 1")
zodis = "Labas"
for x in range(10):
    print(zodis)

# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

print("")
print("task 2")
for n in range(0, 10):
    print(n)

# 3. Sukurkite masyvą iš dešimties augalų pavadinimų.
print("")
print("task 3")

plants = ["Rose", "Tulip", "Cactus", "Sunflower", "Lavendera", "Orchid", "Aloe Vera", "Fern", "Bamboo", "Daisy"]
print(plants)

# 4. Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.
print("")
print("task 4")

for plant_names in plants:
    print(plant_names)

# 5. Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).
print("")
print("task 5")

# pirma versija
for plant_opposite in plants[::-1]:
    print(plant_opposite)

print("")

# antra versija
for c in reversed(plants):
    print(c)

# 6. Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);
print("")
print("task 6")

for x in range(10, 51)[::2]:
    print(x)

print("")
for x in range(10, 51):
    if x % 2 != 0:
        continue
    print(x)

# 7. Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. # ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)
print("")
print("task 7")

for x in range(10, 51)[::2]:
    if x % 10 == 0:
        continue
    print(x)

# 8. Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
print("")
print("task 8")

counter = 0
for y in range(0, 20):
    if y % 2 != 0:
        counter += 1
        continue
print(counter)

# 9. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)
print("")
print("task 9")
shorter_than_5 = 0
longer_than_7 = 0

# Naudojame ciklą per kiekvieną žodį
for plant in plants:
    if len(plant) < 5:
        shorter_than_5 += 1
        continue
print(f"Žodžių trumpesnių nei 5 simboliai: {shorter_than_5}")
for plant in plants:
    if len(plant) > 7:
        longer_than_7 += 1
        continue
print(f"Žodžių ilgesnių nei 7 simboliai: {longer_than_7}")

# 10. Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)
print("")
print("task 10")

print(plants)
counter = 0
for plant in plants:
    if (5 < len(plant) < 10):
        counter += 1
        continue
print(f"Žodžių ilgesnių nei 5 bet trumpesnių nei 10 simbolių: {counter}")

# SUNKESNI UŽDAVINIAI
print("")
print("SUNKESNI UŽDAVINIAI")

# 1. Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.
print("")
print("task 1")

counter = 0
atsitiktiniai = [random.randint(0, 300) for _ in range(0, 300)]
formated = [f"[{a}]" if a > 275 else str(a) for a in atsitiktiniai]

for a in atsitiktiniai:
    if a > 150:
        counter += 1
        continue

print(" ".join(formated))
print(f"Count of number higher than 150: {counter}")

# 2. Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos. Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.
print("")
print("task 2")

formatted = [str(numb) for numb in range(1, 3001) if numb % 77 == 0]
print(f", ".join(formatted))

results = []
for i in range(1, 3000):
    if i % 77 == 0:
        results.append(i)
print(results)

# 3. Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
# * * * *
# * * * *
# * * * *

print("")
print("task 3")

symbol = "*"
for i in range(0, 25):
    print(f" ".join(symbol * 25))

# n = 25
# row = ' '.join(['*'] * n)
# for _ in range(n):
#     print(row)

# 4. Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.
# % * * *
# * % * *
# * * % *
# * * * %
print("")
print("task 4")

symbol = "*"
symbol2 = "#"

print("")

number = 25
for i in range(number):
    row = ""
    for s in range(number):
        if s == i or s == (number - 1 - i):
            row += symbol2
        else:
            row += symbol
    print(f" ".join(row))

# 5. Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius. Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:

print("")
print("task 5")

print("a) Iškritus herbui")

while True:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        break
    else:
        print("S")

print("")
print("b) Tris kartus iškritus herbui")

count = 0
while count < 3:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        count += 1
    else:
        print("S")

print("")
print("c) Tris kartus iš eilės iškritus herbui")
count = 0
while count < 3:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        count += 1
    else:
        print("S")
        count = 0

# 6. Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25. Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: laimėtojo vardas. Taškų kiekį generuokite funkcija random.randint(x,x). Žaidimą laimi tas, kas greičiau surenka 222 taškus. Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.
print("")
print("task 6")

kazys_points = 0
petras_points = 0
kazys_tries = 0
petras_tries = 0

while petras_points < 222:
    petras = random.randint(10, 20)
    petras_points += petras
    petras_tries += 1

while kazys_points < 222:
    kazys = random.randint(10, 20)
    kazys_points += kazys
    kazys_tries += 1

if petras_tries > kazys_tries:
    print(f"Petras laimėjo. Petras surinko: {petras_points} ir Kazys surinko: {kazys_points}")
elif petras_tries < kazys_tries:
    print(f"Kazys laimėjo. Petras surinko: {petras_points} ir Kazys surinko: {kazys_points}")
else:
    print("Abu dalyviai atliko vienodą kiekį bandymų")

# while petras_points < 222 and kazys_points < 222:
#     petras = random.randint(10, 20)
#     kazys = random.randint(5, 25)
#     petras_points += petras
#     petras_tries += 1
#     kazys_points += kazys
#     kazys_tries += 1
#
# if petras_tries > kazys_tries:
#     print(f"Petras laimėjo. Petras surinko: {petras_points} ir Kazys surinko: {kazys_points}")
# elif petras_tries < kazys_tries:
#     print(f"Kazys laimėjo. Petras surinko: {petras_points} ir Kazys surinko: {kazys_points}")
# else:
#     print("Abu dalyviai atliko vienodą kiekį bandymų")

# 7. Reikia nupaišyti pilnavidurį rombą, taip pat, kaip ir pilnavidurį kvadratą (https://lt.wikipedia.org/wiki/Rombas), kurio aukštis 21 eilutė.
print("")
print("task 7")

symbol = "#"
symbol2 = " "

length = 21
for i in range(length):
    row = ""
    for s in range(length):
        if s > (i + length / 2 - 0.5) or s < (length - i - length / 2 - 0.5) or s < (i - length / 2 + 0.5) or s > (
                    length - i + length / 2 - 1.5):
            row += symbol2
        else:
            row += symbol
    print(f" ".join(row))

# 8. Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija. Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# a) “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
print("")
print("task 8 a)")
length = 85
counter = 0
pecks = []
while counter < length:
    pecks = random.randint(5,20)
    print(counter)
    counter += pecks
    break

    if counter > length:
        break


# b) “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.



# # 9. Sugeneruokite stringą, kurį sudarytų 50 atsitiktinių skaičių nuo 1 iki 200, atskirtų tarpais. Skaičiai turi būti unikalūs (t.y. nesikartoti). Sugeneruokite antrą stringą, pasinaudodami pirmu, palikdami jame tik pirminius skaičius (t.y tokius, kurie dalinasi be liekanos tik iš 1 ir patys savęs). Skaičius stringe sudėliokite didėjimo tvarka, nuo mažiausio iki didžiausio. (reikės split() funkcijos ir masyvų.)
#
#
#
