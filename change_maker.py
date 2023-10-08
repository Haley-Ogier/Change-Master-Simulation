#Welcome and starting statements
import string
import math
print('Welcome to the vending machine change maker program')
print('Change maker initialized.')
purchase_price = True
#Creating the stock of coins along with setting the variables
num_nickels = 25
num_dimes = 25
num_quarters = 25
num_ones = 0
num_fives = 0


deposit_menu = ['n','d','q','o','f','c']
letter_value = [5,10,25,100,500,0]
stock = [num_nickels, num_dimes, num_quarters, num_ones, num_fives,0]
change_list = [5,10,25]
coins_list = ['nickels', 'dimes', 'quarters',0]
range_list = list(range(0,100))


while purchase_price == True:
    runs = True
    change = []
    illegal_price = True
    index_of_change = 0
    #printing the stocks
    print('Stock contains:')
    print(f'   {num_nickels} nickels')
    print(f'   {num_dimes} dimes')
    print(f'   {num_quarters} quarters')
    print(f'   {num_ones} ones')
    print(f'   {num_fives} fives')
    print()

    #retreiving the price and checking that it is a valid input
    price = input("Enter the purchase price (xx.xx) or `q' to quit:")
    #FIX ME - if price = q end program and add statment
    if price == 'q':
        purchase_price = False
        total = 0
        for i in letter_value:
            value = stock[letter_value.index(i)]
            total += i * value
        total_dollars = total//100
        total_cents = total%100
        print(f'Total: {total_dollars} dollars and {total_cents} cents')
        #print total - must create list that collects the total
        break
    else:
        #This checks to make sure the price is legal
        #must use price because wecannot declare it as int or float
        #how do we check to see if a string can be turned into a float
        check = price.replace('.','',1).isdigit()
        if check == False:
            print('Invalid purchase price. Try again')
            price = input("Enter the purchase price (xx.xx) or `q' to quit:")

        price = float(price)
        price_in_cents = int(float(price)*100)
        while illegal_price == True:
            if price_in_cents%5 != 0:
                print('Illegal price: Must be a non-negative multiple of 5 cents.')
                print()
                price_in_cents = float(input("Enter the purchase price (xx.xx) or `q' to quit:"))
                price_in_cents = int(price_in_cents*100)
                illegal_price = True
                check = False
                continue
            elif price_in_cents < 0:
                print('Illegal price: Must be a non-negative multiple of 5 cents.')
                print()
                price_in_cents = float(input("Enter the purchase price (xx.xx) or `q' to quit:"))
                price_in_cents = int(price_in_cents*100)
                illegal_price = True
                check = False
                continue
            else:
                illegal_price = False

                
        
        original_price = int(price_in_cents)
        
        #printing and creating variables for the menu
        print()
        print(f'Menu for deposits:')
        print(f"  'n' - deposit a nickel")
        print(f"  'd' - deposit a dime")
        print(f"  'q' - deposit a quarter")
        print(f"  'o' - deposit a one dollar bill")
        print(f"  'f' - deposit a five dollar bill")
        print(f"  'c' - cancel the purchase")
        print()
        dollars = price_in_cents//100
        cents = price_in_cents%100

        #making payments
        print (f'Payment due: {dollars} dollars and {cents} cents')
        deposit = input('Indicate your deposit:')
        for i in deposit_menu:
            if deposit == i:
                break
        else:
            print(f'Illegal selection: {deposit}')
            print (f'Payment due: {dollars} dollars and {cents} cents')
            deposit = input('Indicate your deposit:')
            
        while runs == True:
            for letter in deposit_menu:
                #Fix ME Must add a cancel command

                if price_in_cents > 0: #This is making deposits
                    if deposit == letter:
                        index = deposit_menu.index(letter)
                        value = letter_value[index]
                        price_in_cents -= value
                        dollars = int(price_in_cents)//100
                        cents = int(price_in_cents)%100
                        stock[index] = stock[index] + 1
                        change.append(value)
                        if deposit == 'c':
                            #this returns the change and updates the stock
                            sum_of_change = sum(change)
                            return_change = (sum_of_change) - (original_price)

                            print()
                            print(f'Please take the change below.')
                            if return_change == 0:
                                    print(f'  No change due.')
                                    print()
                                    runs = False
                            else:
                                for i in reversed(change_list):
                                    if (sum_of_change//i) > 0:
                                        index_of_change = change_list.index(i)
                                        type_of_coin = coins_list[index_of_change]
                                        num_of_coins = sum_of_change//i
                                        index_of_change -=6
                                        stock_type = stock[index_of_change]
                                        stock_type = int(stock_type-num_of_coins)
                                        if stock_type >= 0:
                                            print(f'   {int(num_of_coins)} {type_of_coin}', end ='\n')
                                            sum_of_change -= (i*num_of_coins)
                                            stock[index_of_change] = stock_type
                                        else:
                                            stock_type = int(stock_type + num_of_coins)

                                else:
                                    if return_change > 0:
                                        print('Machine is out of change.')
                                        print('See store manager for remaining refund.')
                                        cancel_return = return_change*100
                                        cancel_dollars = cancel_return//100
                                        cancel_cents = cancel_return%100
                                        print(f'Amount due is: {cancel_dollars} dollars and {cancel_cents} cents')
                                print()
                            runs = False
                            break
                        elif dollars > 0: #continues to ask for deposits
                            print (f'Payment due: {dollars} dollars and {cents} cents')
                            deposit = input('Indicate your deposit:')
                        elif dollars == 0 and cents > 0:
                            print (f'Payment due: {cents} cents')
                            deposit = input('Indicate your deposit:')
                        else:
                            #this returns the change and updates the stock
                            sum_of_change = sum(change)
                            return_change = (sum_of_change) - (original_price)
                            print()
                            print(f'Please take the change below.')
                            if return_change == 0:
                                    print(f'  No change due.')
                                    print()
                                    runs = False
                            else:
                                for i in reversed(change_list):
                                    if (return_change//i) > 0:
                                        index_of_change = change_list.index(i)
                                        type_of_coin = coins_list[index_of_change]
                                        num_of_coins = return_change//i
                                        index_of_change -=5
                                        stock_type = stock[index_of_change]
                                        stock_type = int(stock_type-num_of_coins)
                                        if stock_type > 0:
                                            print(f'   {int(num_of_coins)} {type_of_coin}', end ='\n')
                                            return_change -= (i*num_of_coins)
                                            return_change = round(return_change,2)
                                            stock[index_of_change] = stock_type
                                        else:
                                            stock_type = int(stock_type + num_of_coins)

                                else:
                                    if return_change > 0:
                                        print('Machine is out of change.')
                                        print('See store manager for remaining refund.')
                                        cancel_return = return_change*100
                                        cancel_dollars = cancel_return//100
                                        cancel_cents = cancel_return%100
                                        print(f'Amount due is: {cancel_dollars} dollars and {cancel_cents} cents')
                                print()

                            runs = False
        num_nickels = stock[0]
        num_dimes = stock[1]
        num_quarters = stock[2]
        num_ones = stock[3]
        num_fives = stock[4]
