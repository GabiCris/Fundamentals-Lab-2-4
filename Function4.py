'''
4. Obtain different characteristics of the transactions.
sum <type>
max <type> <day>
e.g.
sum in write the total amount from in transactions
max out 15 write the maximum out transaction on day 15.
'''

'''
The 'f_sum' function computes the total amount from the <type> operation that was specified
by the user. Then, this amount is printed with an appropriate message.
'''
def f_sum (transactions, args, undo_list):
    if sum_test(args) == True:
        value_print(compute_sum(transactions, args))

def compute_sum (transactions, args):
    total = 0
    for entry in transactions:
        if entry['type'] == args[0]:
            total += int(entry['value'])
    return total

def value_print (total):
    print ("The value is:", total, ".")
    
def test_f_sum ():
    l = [{"value":'150', "type":'in', "description":'bears', "day":'15'},
                {"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'},
                {"value":'875', "type":'in', "description":'grant', "day":'7'}]
    assert compute_sum(l,['in']) == 4525
    assert compute_sum(l,['out']) == 2375
    l = [{"value":'150', "type":'in', "description":'bears', "day":'15'}]
    assert compute_sum(l,['out']) == 0
    assert compute_sum(l,['in']) == 150
    
'''
The 'f_max' function computes the max value of the <type> transaction in the specified <day>. 
A new copy of a transactions list in created with only the transactions with the specified arguments, 
and the max value is then stored in the 'max_value' variable.
'Max_value' is then printed.
'''
    
def f_max (transactions, args, undo_list):
    if max_test(args) == True:
        value_print(compute_max(transactions, args))
        
def compute_max (transactions, args):
    max_value = 0
    type = args[0]
    day = args [1]
    transactions = [entry for entry in transactions if entry.get("type") == type and entry.get("day") == day]
    for entry in transactions:
        max_value = max (max_value, int(entry['value']))
    return max_value

def test_compute_max():
    l = [{"value":'150', "type":'in', "description":'bears', "day":'15'},
                {"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'},
                {"value":'875', "type":'in', "description":'grant', "day":'7'}]
    assert compute_max(l, ['in','15']) == 150
    assert compute_max(l, ['out','15']) == 0
    assert compute_max(l, ['out','21']) == 2000
    assert compute_max(l, ['out','22']) == 0
'''
Test functions for 'f_max' and 'f_sum', which validate the arguments introduced by the user.
In case of invalid data, the functions print a message and return False. 
'''
def sum_test(args):
    if args[0] not in ['in', 'out'] or len(args) != 1:
        print ("Please input a valid command with the following syntax: sum <type>.")
        return False
    return True

def max_test(args):
    if len(args) != 2 or args[0] not in ['in', 'out'] or args[1].isdigit()== False or args[1].isdigit()== True and int(args[1]) not in range (1, 31):
        print ("Please input a valid command with the following syntax: max <type> <day>.")
        return False
    return True

test_f_sum()
test_compute_max()