dias = int(input('Idade em dias: '))
anos = int(dias / 365)
dias -= (anos * 365)
meses = int(dias/30)
dias -= meses*30
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
print()