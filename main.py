import random
import statistics

# Kintamieji ir sąlygos 2024-09-25

# 1 uzd.
# vardas = str( input('Mano vardas: '))
# pavardė = str( input('Mano pavardė: '))
# gimMetai = int( input('Mano gimimo metai: '))
# todayY= int( input('Šie metai: '))
# print(f'Jūsų amžius: {todayY - gimMetai}')
# veikia

# 2 uzd
# kint1 = random.randint(0, 4)
# kint2 = random.randint(0, 4)

# print(kint1)
# print(kint2)
#
# if kint1 != 0 and kint2 != 0:
#     if kint1 > kint2: print(int(kint1 / kint2))
#     else: print(int(kint2 / kint1))
# else: print('Dalyba iš 0 negalima')
# veikia

# 3 uzd.

# randSk1 = random.randint(0, 25)
# randSk2 = random.randint(0, 25)
# randSk3 = random.randint(0, 25)
#
# print(randSk1)
# print(randSk2)
# print(randSk3)
#
# # print(statistics.median([randSk1, randSk2, randSk3]))
#
# if (randSk1 > randSk2 and randSk1 < randSk3) or (randSk1 > randSk3 and randSk1 < randSk2):
#     print("skaičius 1")
# if (randSk2 > randSk1 and randSk2 < randSk3) or (randSk2 > randSk3 and randSk2 < randSk1):
#     print('Skaičius 2')
# else: print('Skaičius 3')

# 4 uzd.

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)

print('a kraštinė:', a)
print('b kraštinė:', b)
print('c kraštinė:', c)

if a + b > c and a + c > b and b + c > a:
    print('Susidaro trikampis')
else: print("Nesusidaro trikampis")

# veikia