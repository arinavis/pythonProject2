import random

# Kintamieji ir sąlygos 2024-09-25

# 1 uzd.
# vardas = str( input('Mano vardas: '))
# pavardė = str( input('Mano pavardė: '))
# gimMetai = int( input('Mano gimimo metai: '))
# todayY= int( input('Šie metai: '))
# print(f'Jūsų amžius: {todayY - gimMetai}')
# veikia

# 2 uzd
kint1 = random.randint(0, 4)
kint2 = random.randint(0, 4)

print(kint1)
print(kint2)

if kint1 != 0 and kint2 != 0:
    if kint1 > kint2: print(int(kint1 / kint2))
    else: print(int(kint2 / kint1))
else: print('Dalyba iš 0 negalima')
# veikia
