#Written By Michael Mark

def start():
    d = {}
    name = input('What is your name? ')
    pin = input('What is your pin? ')
    amount = input('How much money is currently in your account? ')
    amount = float(amount)
    d[pin] = [name, amount]
    return d

def verifyPin(d):
    i = 0
    while True:
        pin = input('Enter pin number: ')
        i += 1
        if pin in d:
            name = d[pin][0]
            return(pin, name)
        else:
            print('Invalid pin, try again: ')
        if i == 3:
            msg = 'Please call customer support at 800-000-0000'
            return(None, msg)

def displayMenu(name):
    print('Welcome {}, Menu Options:'.format(name))
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Balance')
    print('4. Quit')
    verify = verifyMenuChoice()
    return verify

def verifyMenuChoice():
    while True:
        try:
            choice = int(input('Enter a menu number: '))
            if choice in [1,2,3,4]:
                return choice
            else:
                print('Enter 1 or 2 or 3 or 4, try again')
        except ValueError:
            print('{} invalid choice, non-numeric characters not allowed, try again.'.format(choice))

def verifyAmount():
    while True:
        try:
            amount = float(input('Enter amount: '))
            if amount < 0:
                print('Negative amount. Try again.')
            else:
                return amount
        except ValueError:
            print('Invalid amount. Use digits only.')

def deposit(pin, d):
    amount = verifyAmount()
    d[pin][1] += amount
    return

def withdraw(pin, d):
    amount = verifyAmount()
    currentBalance = d[pin][1]
    while amount > currentBalance:
        print('Insufficient funds to complete the transaction.')
        return
    while amount == 0:
        print('Invalid, enter amount you would like to withdraw.')
        amount = verifyAmount()
    d[pin][1] -= amount
    return

def balance(pin, d):
    return(d[pin][1])

def quit(pin, d):
    while True:
        ans = input('Do you want to leave the transaction? "y" for yes "n" for no ')
        if ans == 'y':
            print('Thanks {}, Your balance is: {}, thank you for using the MichaelBoss banking system.'.format(d[pin][0], d[pin][1]))
            return(ans)
        else:
            return(ans)

def ATM():
    dict = start()
    if dict == None:
        return
    pin, msg = verifyPin(dict)
    if pin == None:
        print(msg)
        return 'Goodbye' 
    name = msg

    while True:
        print()
        choice = displayMenu(name)
        if choice == 1:
            deposit(pin, dict)
        elif choice == 2:
            withdraw(pin, dict)
        elif choice == 3:
            b = balance(pin, dict)
            msg = 'Current balance is ${:,.2f}'
            print('\n', msg.format(b))
        elif choice == 4:
            reply = quit(pin, dict)
            if reply == 'n':
                pass
            else:
                break
            
    return 'Goodbye'
    
        
            
        
            
                
    

    

