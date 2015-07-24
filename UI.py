from cash_desk import CashDesk


kasa = CashDesk()

print('Welcome to our store.')
for each in kasa.items:
    print (each, '-', kasa.items[each])

cashout = False
while cashout is False:
    command = input('>>> ').strip().split()
    if command[0] == 'scan':
        scan_item = command[1]
        kasa.scan(scan_item)
        print (kasa.scanned_items)
    elif command[0] == 'cashout':
        cashout = True
        print (kasa.calculate_all())
    else:
        print ('Invalid Command.')
