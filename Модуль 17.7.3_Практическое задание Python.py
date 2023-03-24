money = float(input('Укажите размер суммы денежного вклада:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
list_of_per_cent = list(per_cent.values())
TKB_deposit = list_of_per_cent [0] * (money / 100)
SKB_deposit = list_of_per_cent [1] * (money / 100)
VTB_deposit = list_of_per_cent [2] * (money / 100)
SBER_deposit = list_of_per_cent [3] * (money / 100)
deposit = [TKB_deposit, SKB_deposit, VTB_deposit, SBER_deposit]
map(int, deposit)
print (list(map(int, deposit)))
print ('Максимальная сумма, которую вы можете заработать -', int(max(deposit)))
