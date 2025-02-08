harga_emaspergram1 = 650000
harga_emaspergram2 = 685000
harga_emaspergram3 = 715000

harga_emas1 = harga_emaspergram1 * 25
harga_emas2 = harga_emaspergram2 * 25
harga_emas3 = harga_emaspergram2 * 15
harga_emas4 = harga_emaspergram3 * 40

modal1 = harga_emas1
modal2 = harga_emas1 + harga_emas3

keuntungan1 = harga_emas2 - modal1
keuntungan2 = harga_emas4 - modal2

persen1 = (keuntungan1 / modal1) * 100
persen2 = (keuntungan2 / modal2) * 100

print("Kasus Pertama:")
print("Keuntungan Gerald adalah =", keuntungan1)
print("Keuntungan Gerald dalam persen adalah =", round(persen1, 2))

print("Kasus Kedua:")
print("Keuntungan Gerald adalah =", keuntungan2)
print("Keuntungan Gerald dalam persen adalah =", round(persen2, 2))