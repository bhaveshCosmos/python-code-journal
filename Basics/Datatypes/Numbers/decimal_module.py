print(0.1 + 0.1 + 0.1 - 0.3) # 5.551115123125783e-17

from decimal import Decimal
res = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.2')
print(res) # 0.1
