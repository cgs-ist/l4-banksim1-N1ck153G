# Non OOP
# Bank Version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')    
    print('Press q to quit')
    
    action = input("What do you want to do? ")
    action = action.lower() #
    action = action[0]
    
    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your balance is: ', accountBalance)

    if action == 'd':
        print('make a deposit')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            deposit = int(input('Please enter your deposited amount: '))
            accountBalance = deposit + accountBalance
            print(f'your balance is now, {accountBalance}.')

    if action == 'w':
        print('make a withdrawl')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            withdrawl = int(input('Please enter your withdrawl amount: '))
            accountBalance = accountBalance - withdrawl
            print(f'your balance is now, {accountBalance}.')

    if action == 's':
        print('show account')
        userPassword = input('please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print(f'Account name: {accountName}')
            print(f'Account balance: {accountBalance}')

    if action == 'q':
        confirmation = input('Are you sure you want to quit (Y/N): ')
        if confirmation.upper() == 'Y':
            exit()
        else:
            print('OK')