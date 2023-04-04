Ticket_cost = 0
Tickets_quanity = int(input('Введите количество билетов:'))
for i in range (1, Tickets_quanity + 1):
    Age = int(input('Укажите возраст:'))
    if Age < 18:
        Ticket_cost += 0
    elif 18 <= Age < 25:
        Ticket_cost += 990
    elif Age >= 25:
        Ticket_cost += 1390
print ('Всего билетов:', Tickets_quanity,', на общую сумму', Ticket_cost, 'рублей.')
if Tickets_quanity >= 3:
    Discount_cost = Ticket_cost * 0.9
    print('ИТОГО: к оплате', int(Discount_cost), 'рублей (скидка 10% за покупку 3-х и более билетов).')
else:
    print('ИТОГО: к оплате', Ticket_cost, 'рублей (без скидки 10% за покупку 3-х и более билетов).')




















