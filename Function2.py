'''
2. Modify transactions from the list.
remove <day>
remove <start day> to <end day>
remove <type>
replace <day> <type> <description> with <value>
e.g.
remove 15  remove all transactions from day 15
remove 5 to 10  removes all transactions between day 5 and day 10.
remove in  remove all the in transactions from the current month
replace 12 in salary with 2000  replace the amount for the in transaction 
having the salary description from day 12 with 2000 RON
'''

from copy import deepcopy
'''
The function f_remove takes as arguments the list of transactions and the arguments with commands
The function then calls another required function depending on the scenario:
    -remove_day if we are required to remove all transactions made on "day"
    -remove_interval if we are required to remove all transactions between two days "day1" and "day2"
    -remove_inout if we are required to remove all transactions with the "type" in or out
After the call is made, the list "transaction" is modified accordingly
'''
def f_remove (transactions, args, undo_list):
    if remove_test(args) == True:
        undo_list.append(deepcopy(transactions))
        if len(args) == 3:
            remove_interval(transactions, args)
        elif args[0] == 'in' or args[0] == 'out':
            remove_inout(transactions,args)
        remove_day(transactions,args)

def test_remove ():
    a = []
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    f_remove(l,['out'], a)
    assert l == [{"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    f_remove(l,['20', 'to', '22'], a)
    assert l == [{"value":'375', "type":'out', "description":'laptop', "day":'13'}]
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    f_remove(l,['21'], a)
    assert l ==[{"value":'375', "type":'out', "description":'laptop', "day":'13'}]

def remove_day(transactions, args):
    transactions[:] = [entry for entry in transactions if entry.get("day") != args[0]]

def remove_interval(transactions, args):
    day1 = int(args[0])
    day2 = int(args[2])
    transactions[:] = [entry for entry in transactions if int(entry.get("day")) < day1 
                       or int(entry.get("day")) > day2]

def remove_inout(transactions, args):
    transactions[:] = [entry for entry in transactions if entry.get("type") != args[0]]

'''
The f_replace function takes as parameters the list of transactions and the data introduced by the 
user in the list "args" and replaces the specified transaction's value with a new one.
The list transactions is updated with the new value.
If the format of the input was correct, but no such transaction was found in the "transaction" list
the function prints an appropriate message.
'''
def f_replace (transactions, args, undo_list):
    if replace_test(args) == True:
        no_entry = True
        day, type, description, value = args[0], args[1], args[2], args[4]
        for entry in transactions:
            if entry["day"] == day and entry["type"] == type and entry["description"] == description:
                undo_list.append(deepcopy(transactions))
                entry["value"] = value
                no_entry = False
        if no_entry == True:
            print ("There is no transaction with the specifications that were provided.")
            
def test_replace ():
    a = []
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    f_replace(l,['13', 'out', 'laptop','with','1000'], a)
    assert l == [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'1000', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
'''
Test functions ("remove_test" and "replace_test") which verify the validity of the user commands. 
If the data is not legit, then the function returns False and prompts the user to retype the instruction.
'''
def remove_test(args):
    if len(args) not in [1, 3]:
        print ("Please input a valid command.")
        return False
    if args[0].isdigit() == True and int(args[0]) not in range (1,31):
        print ("Please input the command with the format 'remove <start day> to <end day>'. ")
        return False
    if args[0].isdigit() == False and args[0] not in ['in', 'out']:
        print ("Please input the command with the format 'remove <start day> to <end day>'. ")
        return False
    if len(args) == 3:
        if args[2].isdigit() == True and int(args[2]) not in range (1,31):
            print ("Please input a valid end day for the remove instruction in the range of 1 - 30")
            return False
        if args[1] != 'to' or (int(args[0]) > int(args[2])):
            print ("Please input the command with the format 'remove <start day> to <end day>'. ")
            return False
    return True

def replace_test(args):
    if len(args) != 5:
        print("Please type a command using the following format: 'replace <day> <type> <description> with <value>'.")
        return False
    if args[0].isdigit() == True and int(args[0]) not in range(1,31) or args[0].isdigit() == False:
        print("Please input a valid day in the interval 1 - 30.")
        return False
    if args[3] != 'with':
        print ("Please type a command using the following format: 'replace <day> <type> <description> with <value>'.")
        return False
    if args[4].isdigit() == False:
        print ("Please input a positive integer number for the new value of the transaction.")
        return False
    if args[1] not in ['in', 'out']:
        print ("Please specify the type of the transaction using 'in' or 'out'.")
        return False
    return True    

test_replace()
test_remove()