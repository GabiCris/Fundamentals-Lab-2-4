from s02p1.Function1 import f_add, f_insert
from s02p1.Function3 import f_list
from s02p1.Function2 import f_replace, f_remove
from s02p1.Function5 import f_filter,undo
from s02p1.Function4 import f_sum, f_max

def print_menu ():
    print("Choose any of the following commands:")
    print("    1. Add")
    print("    2. Insert")
    print("    3. Remove")
    print("    4. Replace")
    print("    5. List")
    print("    6. Sum")
    print("    7. Max")
    print("    8. Filter")
    print("    9. Undo")
    print("    10. Exit")

def print_success():
    print("Command processed.")
    
def menu ():
    dicts = {'1':ui_add,
            '2':ui_insert,
            '3':ui_remove,
            '4':ui_replace,
            '5':ui_list,
            '6':ui_sum,
            '7':ui_max,
            '8':ui_filter,
            '9':ui_undo
            }
    transactions = []
    init_transactions(transactions)
    undo_list = []
    
    while True:
        print_menu()
        w = read_cmd()
        if  w == '10':
            print("Thank you for using the application.")
            break
        dicts[w](transactions, undo_list)

def read_cmd():
    w = input ("Choose a command: ")
    return w

def init_transactions(transactions):
    transactions[:] = [{"value":'150', "type":'in', "description":'bears', "day":'15'},
                {"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'},
                {"value":'875', "type":'in', "description":'grant', "day":'7'}]


def ui_add(transactions, undo_list):
    args = []
    args.append(input("Value:"))
    args.append(input("Type:"))
    args.append(input("Description:"))
    f_add(transactions, args, undo_list)
    print_success()
    
def ui_insert(transactions, undo_list):
    args = []
    args.append(input("Day:"))
    args.append(input("Value:"))
    args.append(input("Type:"))
    args.append(input("Description:"))
    f_insert(transactions, args, undo_list)
    print_success()
    
def ui_remove(transactions, undo_list):
    print_remove_commands()
    w = read_cmd()
    args = commands_remove(w)
    f_remove(transactions, args, undo_list)
    print_success()

def print_remove_commands ():
    print("        1. Remove all transactions from a day.")
    print("        2. Remove all transactions between a start and end day.")
    print("        3. Remove all transactions of a type.")

def commands_remove(w):
    args = []
    if w == '1':
        args.append(input("Day:"))
    if w == '2':
        args.append(input("Start day:"))
        args.append("to")
        args.append(input("End day:"))
    if w == '3':
        args.append(input("Type:"))
    return args
    
def ui_replace(transactions, undo_list):
    args = []
    args.append(input("Day:"))
    args.append(input("Type:"))
    args.append(input("Description:"))
    args.append("with")
    args.append(input("New Value:"))
    f_replace(transactions, args, undo_list)
    print_success()
    
def ui_filter(transactions, undo_list):
    print_filter_commands()
    w = read_cmd()
    args = commands_filter(w)
    f_filter(transactions, args, undo_list)
    print_success()

def print_filter_commands():
    print("        1. Filter all the transactions of a type.")
    print("        2. Filter all transactions of a type with a value smaller than a given one.")
    
def commands_filter(w):
    args = []
    if w == '1':
        args.append(input("Type:"))
    elif w == '2':
        args.append(input("Type:"))
        args.append(input("Value:"))
    return args

def ui_list(transactions, undo_list):
    print_list_commands ()
    w = read_cmd()
    args = commands_list(w)
    f_list(transactions,args,undo_list)
    
def commands_list(w):
    args = []
    if w == '1':
        args = []
    elif w == '2':
        args.append(input("Type:"))
    elif w == '3':
        args.append(input("Operation:"))
        args.append(input("value: "))
    elif w == '4':
        args.append("balance")
        args.append(input("Day: "))
    return args

def print_list_commands():
    print("        1. List all transactions.")
    print("        2. List transactions of a type.")
    print("        3. List transactions <,=,> than a value.")
    print("        4. Lists the balance of all transactions before the given day.")    

def ui_sum(transactions, undo_list):
    args = []
    args.append(input("Type:"))
    f_sum(transactions, args, undo_list)
    print_success()
    
def ui_max(transactions, undo_list):
    args = []
    args.append(input("Type:"))
    args.append(input("Day:"))
    f_max(transactions, args, undo_list)
    print_success()
    
def ui_undo(transactions, undo_list):
    args = []
    undo(transactions,args,undo_list)

def welcome_print():
    print("Welcome to the application!")
    print("Choose between a text-based or a menu-based UI:")
    print("1. Text-Based")
    print("2. Menu-Based")
    