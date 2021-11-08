seg = int(input('Segundos = '))
hrs = int(seg/3600)
seg -= hrs*3600
min = int(seg/60)
seg -= min*60
print(f'{hrs}:{min}:{seg}')
print()