saldo_awal=200000000
tahun=0
while saldoawal<=400000000:
 bunga=saldo_awal*0.1
 saldo_awal=saldo_awal+bunga
 tahun=tahun+1
 print(saldo_awal)
 print("tahun",tahun)