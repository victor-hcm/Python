medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
print('A média de {}m corresponde a {}cm e {}mm e {}km'.format(medida, cm, mm, km))