from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays


setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
format1 = dt.strftime('%A, %d de %B de %Y')
format2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(format1)
print(format2)

print("\n")

"""Como saber a ultima data do mes """
dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
print(mes_atual, mdays[mes_atual])
