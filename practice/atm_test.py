import atm_interface

new_account = atm_interface.BankAccount()

query = 0
while query != 'q':
    query = input(' 1. Check checking balance \n'
                  '2. Check Savings balance \n'
                  '3. Withdrawl from checking \n'
                  '4. Withdrawl from savings \n'
                  '5. Show checking interest earned \n'
                  '6. Show savings interest earned \n'
                  '7. Deposit to checking \n'
                  '8. Deposit to savings \n'
                  'q. Quit \n')

    if query == '1':
        print('You have ${} in your checking'.format(new_account.checking.get_funds()))
    if query == '2':
        print('You have ${} in your savings'.format(new_account.savings.get_funds()))
    if query == '3':
        amount = int(input('Enter the amount to withdrawl \n'))
        new_account.checking.withdraw(amount)
    if query == '4':
        amount = int(input('Enter the amount to withdrawl \n'))
        new_account.savings.withdraw(amount)
    if query == '5':
        print('Your checking interest earned is ${} '.format(new_account.checking.calc_interest()))
    if query == '6':
        print('Your savings interest earned is ${} '.format(new_account.savings.calc_interest()))
    if query == '7':
        amount = int(input('Enter the amount to deposit: '))
        new_account.checking.deposit(amount)
        print('Thanks for the deposit, your new checking balance is ${}'.format(new_account.checking.get_funds()))
    if query == '8':
        amount = int(input('Enter the amount to deposit: '))
        new_account.savings.deposit(amount)
        print('Thanks for the deposit, your new savings balance is ${}'.format(new_account.savings.get_funds()))




