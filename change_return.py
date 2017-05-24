til = {'hundreds': 3,
        'fifties': 5,
        'twenties': 2,
        'tens': 3,
       'fives': 0,
        'ones': 3,
        'quarters': 2,
        'dimes': 7,
        'nickels': 5,
        'pennies': 20000}

def make_change(payment):
    dollars = payment // 1
    print(str(payment))
    cents = (payment - dollars) * 100
    dollars = int(dollars)
    cents = int(cents)
    change = {}
    extra = 0

    hundreds = dollars // 100
    if hundreds > til['hundreds']:
        extra = (hundreds - til['hundreds']) * 100
        hundreds = til['hundreds']
        til['hundreds'] = 0
    if hundreds > 0:
        change['hundreds'] = hundreds
    dollars = (dollars % 100) + extra
    extra = 0

    fifties = dollars // 50
    if fifties > til['fifties']:
        extra = (fifties - til['fifties']) * 50
        fifties = til['fifties']
        til['fifties'] = 0
    if fifties > 0:
        change['fifties'] = fifties
    dollars = (dollars % 50) + extra
    extra = 0

    twenties = dollars // 20
    if twenties > til['twenties']:
        extra = (twenties - til['twenties']) * 20
        twenties = til['twenties']
        til['fifties'] = 0
    if twenties > 0:
        change['twenties'] = twenties
    dollars = (dollars % 20) + extra
    extra = 0

    tens = dollars // 10
    if tens > til['tens']:
        extra = (tens - til['tens']) * 10
        tens = til['tens']
        til['tens'] = 0
    if tens > 0:
        change['tens'] = tens
    dollars = (dollars % 10) + extra
    extra = 0


    fives = dollars // 5
    if fives > til['fives']:
        extra = (fives - til['fives']) * 5
        fives = til['fives']
        til['fives'] = 0
    if fives > 0:
        change['fives'] = fives
    ones = (dollars % 5) + extra
    extra = 0

    if ones > til['ones']:
        extra = (ones - til['ones'])
        ones = til['ones']
        til['ones'] = 0
    if ones > 0:
        change['ones'] = dollars

    cents = cents + extra * 100

    quarters = (cents) // 25
    if quarters > til['quarters']:
        extra = (quarters - til['quarters']) * 25
        quarters = til['quarters']
        til['quarters'] = 0
    if quarters > 0:
        change['quarters'] = quarters
    left = (cents % 25) + extra
    extra = 0

    dimes = left // 10
    if dimes > til['dimes']:
        extra = (dimes - til['dimes']) * 10
        dimes = til['dimes']
        til['dimes'] = 0
    if dimes > 0:
        change['dimes'] = dimes
    left = left % 10 + extra
    extra = 0


    nickels = left // 5
    if nickels > til['nickels']:
        extra = (nickels - til['nickels']) * 5
        nickels = til['nickels']
        til['nickels'] = 0
    if nickels > 0:
        change['nickels'] = nickels

    pennies = left % 5 + extra
    if pennies > til['pennies']:
        short = str((pennies - til['pennies']) * 100)
        return 'short'
    elif pennies > 0:
        change['pennies'] = pennies
    return change


payment = float(input('How much money are you given?  '))
change = make_change(payment)
if change == 'short':
    print('We do not have enough money to make change')
else:
    text_return = 'Your change is '
    for k, v in change.items():
        text_return += '{}: {}, '.format(k,v)

    print(text_return[:-2])
