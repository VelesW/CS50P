owing = 50
while owing > 0:
    print(f'Amount Due: {owing}')
    x = int(input('Insert Coin: '))
    if x == 25 or x == 10 or x == 5:
        owing = owing - x
print(f'Change Owed: {abs(owing)}')