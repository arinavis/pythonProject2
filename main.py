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

# a = random.randint(1, 10)
# b = random.randint(1, 10)
# c = random.randint(1, 10)
#
# print('a kraštinė:', a)
# print('b kraštinė:', b)
# print('c kraštinė:', c)
#
# if a + b > c and a + c > b and b + c > a:
#     print('Susidaro trikampis')
# else: print("Nesusidaro trikampis")

# veikia

# 5 uzd.
# num1 = random.randint(0,2)
# num2 = random.randint(0,2)
# num3 = random.randint(0,2)
# num4 = random.randint(0,2)
#
# print('Pirmas kintamasis:', num1)
# print('Antras kintamasis:', num2)
# print('Trečias kintamasis:', num3)
# print('Ketvirtas kintamasis:', num4)
#
# count0 = 0
# count1 = 0
# count2 = 0
#
# if num1 == 0:
#     count0 += 1
# if num2 == 0:
#     count0 += 1
# if num3 == 0:
#     count0 += 1
# if num4 == 0:
#     count0 += 1
#
# if num1 == 1:
#     count1 += 1
# if num2 == 1:
#     count1 += 1
# if num3 == 1:
#     count1 += 1
# if num4 == 1:
#     count1 += 1
#
# if num1 == 2:
#     count2 += 1
# if num2 == 2:
#     count2 += 1
# if num3 == 2:
#     count2 += 1
# if num4 == 2:
#     count2 += 1
#
# print('Nuliai: ', count0)
# print('Vienetai: ', count1)
# print('Dvejetai: ', count2)
#
# # veikia

# 6 uzd.

# ranNum1 = random.randint(-10, 10)
# ranNum2 = random.randint(-10, 10)
# ranNum3 = random.randint(-10, 10)
#
# print('Random number one =', ranNum1)
# print('Random number two =', ranNum2)
# print('Random number three =', ranNum3)
#
#
# if ranNum1 < 0:
#     print([ranNum1])
# if ranNum1 == 0:
#     print(f'({ranNum1})')
# if ranNum1 > 0:
#     print({ranNum1})
#
# if ranNum2 < 0:
#     print([ranNum2])
# if ranNum2 == 0:
#     print(f'({ranNum2})')
# if ranNum2 > 0:
#     print({ranNum2})
#
# if ranNum3 < 0:
#     print([ranNum3])
# if ranNum3 == 0:
#     print(f'({ranNum3})')
# if ranNum3 > 0:
#     print({ranNum3})

# Veikia

# 7 uzd

# zvKiekis = random.randint(5, 3000)
# # zvKiekis = 2200
# zvKaina = 1
# print('Žvakių kiekis:', zvKiekis)
# if 1000 < zvKiekis <= 2000:
#     print('Kaina su 3% nuolaida:', round(zvKiekis * zvKaina * 0.97, 2), 'eurai')
# elif zvKiekis > 2000:
#     print('Kaina su 4 % nuolaida:', round(zvKiekis * zvKaina / 0.96, 2), 'eurai')
# else:
#     print('Kaina:', zvKiekis * zvKaina, 'eurai')

# Veikia

# 8 uzd
# sk1 = random.randint(0, 100)
# sk2 = random.randint(0, 100)
# sk3 = random.randint(0, 100)
#
# print(f'random skaičiai: {sk1} {sk2} {sk3}')
# print('Aritmetinis vidurkis:', round((sk1 + sk2 + sk3) / 3))
# # sk1 = 11
# # sk2 = 80
# # sk3 = 30
# if 10 < sk1 < 90 and 10 < sk2 < 90 and 10 < sk3 <90:
#     print('Aritmetinis vidurkis [10, 90]:', round((sk1 + sk2 + sk3) / 3))
# else: print('Netinkamos reikšmės')

# Veikia

# 9 uzd
val = random.randint(00, 23)
min = random.randint(00, 59)
sek = random.randint(00, 59)
papSk = random.randint(0, 300)
print(f'Random skaičiai: {val}, {min}, {sek}, papildomas skaičius: {papSk}')
# print('Laikas:', ('0' + str(val))[-2:] + ':' + ('0' + str(min))[-2:] + ':' + ('0' + str(sek))[-2:])
print(f'Laikas: {val}:{min}:{sek}')

# nepavyko

# Sugeneruojame atsitiktines valandas, minutes ir sekundes
valandos = random.randint(0, 23)   # Valandos nuo 0 iki 23
minutes = random.randint(0, 59)    # Minutės nuo 0 iki 59
sekundes = random.randint(0, 59)   # Sekundės nuo 0 iki 59

# Sugeneruojame atsitiktinį papildomų sekundžių skaičių
papildomos_sekundes = random.randint(0, 300)

# Atspausdiname laikrodį prieš pridėjimą
print(f"Laikas prieš pridėjimą: {valandos:02d}:{minutes:02d}:{sekundes:02d}")
print(f"Pridedamos sekundės: {papildomos_sekundes}")

# Apskaičiuojame bendrą sekundžių skaičių pradinėje būsenoje
bendros_sekundes = valandos * 3600 + minutes * 60 + sekundes

# Pridedame papildomas sekundes
bendros_sekundes += papildomos_sekundes

# Paverčiame bendras sekundes atgal į valandas, minutes ir sekundes
naujos_valandos = (bendros_sekundes // 3600) % 24  # Moduliuojame 24, kad nebūtų daugiau nei 23 valandos
naujos_minutes = (bendros_sekundes % 3600) // 60   # Minutės
naujos_sekundes = bendros_sekundes % 60            # Sekundės

# Atspausdiname laikrodį po sekundžių pridėjimo
print(f"Laikas po pridėjimo: {naujos_valandos:02d}:{naujos_minutes:02d}:{naujos_sekundes:02d}")

# chatGPT