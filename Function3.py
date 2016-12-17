'''
3. Write the transactions having different properties.
list
list <type>
list [ < | = | > ] <value>
list balance <day>
e.g.
list  write the entire list of transactions.
list in  write all the in transactions.
list > 100  writes all transactions having an amount of money > 100.
list = 67  write all transactions having an amount of money = 67
list balance 10  computes the accounts balance on day 10. This is the sum of 
all in transactions, from which we subtract out transactions occurring before or on day 10.
'''
'''
The function "f_list" calls the test function to confirm the validity of the arguments, then calls 
the correct function, depending on the operation that is desired:
    -'print_all' if all the transactions are to be printed = 'list'
    -'print_inout' if all transactions of a type are to be printed = 'list <type>'
    -'print_operation' if transactions following a certain rule are to be printed
      = 'list [>,=,<] <value>'
    -'print_balance' to print the account's ballance on a certain day = 'list balance <day>'
If the "transactions" list is empty, a message will be printed. 
'''

def f_list (transactions, args, undo_list):
    if not transactions:
        print_list_empty()
    if print_test(args) == True:
        if not args:
            print_all(transactions, args)
        elif args[0] in ['>', '<', '=']:
            print_all(print_operations(transactions, args),args)
        elif args[0] == 'balance':
            total = print_balance(transactions, args)
            balance_show(total)
        elif args[0] in ['in', 'out']:
            print_all(print_inout(transactions, args), args)    
        
        
'''
The function f_list takes as arguments the lists "transactions" and args (easier to call) and then
prints all transactions, one per row.
'''
def print_all (transactions, args):
    if transactions:
        print_list_full()
        for i in transactions:
            for x in i:
                print (x ,": ", i[x],"; ", end = " ", sep = '')
            print ()

def print_list_empty():
    print ("The list of transactions is empty.")
    
def print_list_full():
    print ("The list of transactions: ")

'''
Function that creates a new list with all transactions of a specific type ('in' or 'out'), and then 
uses the the function "print_all" to print the new transaction's list.
'''
def print_inout (transactions, args):
    if args[0] == 'in':
        l = [entry for entry in transactions if entry.get("type") != 'out']
    else:
        l = [entry for entry in transactions if entry.get("type") != 'in']
    return l

def test_print_inout ():
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    t = print_inout(l, ['in'])
    assert t == [{"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    assert print_inout(l,['out']) == [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'}]
    assert print_inout(t, ['out']) == []

'''
Function that creates a new list with all transactions with a specified value (<,=,>), and then 
uses the the function "print_all" to print the new transaction's list.
'''
def print_operations (transactions, args):
    if args[0] == '>':
        transactions = [entry for entry in transactions if int(entry.get("value")) > int(args[1])]
    elif args[0] =='<':
        transactions = [entry for entry in transactions if int(entry.get("value")) < int(args[1])]
    else:
        transactions = [entry for entry in transactions if entry.get("value") == args[1]]
    return transactions
    #TODO FUNCTION RETURNS TRANSACTIONS LIST AND PRINTS IN ANOTHER FUNCTION

def test_print_operations():
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    t = print_operations(l,["<",1000])
    assert t == [{"value":'375', "type":'out', "description":'laptop', "day":'13'}]
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
            {"value":'375', "type":'out', "description":'laptop', "day":'13'},
            {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    t = print_operations(l,[">",2300])
    assert t == [{"value":'3500', "type":'in', "description":'salary', "day":'21'}]

'''
Function which computes the total sum of the <type> transactions on a specified day in the var 'total'.
The function then returns 'total'
'''
def print_balance (transactions, args):
    day = args[1]
    total = 0
    for entry in transactions:
        if int(entry["day"]) <= int(day):
            if entry["type"] == 'in':
                total += int(entry['value'])
            else:
                total -= int(entry['value'])
    return total

def balance_show (total):
    print ("The balance of the account is ", total, ".")


def test_print_balance ():
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    assert print_balance(l,['balance','14']) == -375
    assert print_balance(l,['balance','22']) == 1125
    assert print_balance(l,['balance','5']) == 0

'''
Test function for the f_print 
'''
def print_test (args):
    if len(args) != 0:
        if len(args) > 2:
            print ("Please input a valid command.")
            return False
        elif args[0] not in ['in','out','>','<','=', 'balance']:
            print ("Please input a command with the following syntax: list <type><balance>.")
            return False
        elif len(args) == 2 and args[0] in ['>','<','='] and args[1].isdigit() == False:
            print("Please input a command with the following syntax: list ['>','=','<'] <value>.")
            return False
        elif len(args) == 2:
            if (args[0] == 'balance'):
                if args[1].isdigit() == False or args[1].isdigit()==True and(int(args[1]) not in range (1, 31)):
                    print("Please input a command with the following syntax: list balance <day>.")
                    return False
        elif args[0] == 'balance' and len(args) == 1:
            print ("Please also specify the day after 'balance'.")
            return False
        elif args[0] in ['in', 'out'] and len(args) != 1:
            print ("Please input a command with the following syntax: list <type>.")
            return False
    return True
                                            
test_print_operations() 
test_print_balance()
test_print_inout()