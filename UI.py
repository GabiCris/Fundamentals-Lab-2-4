#LAB 02 - 04, Pb. 4

'''
Function read_cmds () - no parameters
Takes the input from the user and returns a list "args" with the arguments and a var "cmd" with 
the respective command;
'''

from Function1 import *
from Function2 import *
from Function3 import *
from Function4 import *
from Function5 import *


def read_cmds():
    print("Please input your command : ")
    line = input()
    args = line.split(" ")
    cmd = args[0]
    del args[0]
    return (cmd, args)

'''
Function which starts the loop for reading input values from the user. The function reads the command
from the user in the var "cmd", then calls the appropriate function, while also providing some initial
values in "transaction" for easier testing.
'''
def f_run():
    transactions = []
    add_test_var(transactions)
    undo_list = []
    commands = {"add": f_add, 
                "insert": f_insert, 
                "remove":f_remove, 
                "replace": f_replace, 
                "list": f_list,
                "sum": f_sum,
                "max": f_max,
                "filter": f_filter,
                "undo": undo
                }  
    while True:
        (cmd, args) = read_cmds()
        if cmd == "exit":
            break
            print ("Thank you for using the application.")
        while verify_command (cmd) == False:
            print ("Please input a valid command. ")
            (cmd, args) = read_cmds()
        commands[cmd](transactions, args, undo_list)
        

'''
A test function which verifies if the instructions provided by the user are valid. If "cmd" is not
a valid command, then the function return False. If the instruction is recognised, then the function
returns True
'''
def verify_command(cmd):
    values = ['add', 'insert', 'replace', 'remove', 'list', 'sum', 'max', 'filter', 'undo']
    if cmd not in values:
        return False
    return True

'''
Function that adds transactions in the list for test purposes:
'''
def add_test_var (transactions):
    transactions[:] = [{"value":'150', "type":'in', "description":'bears', "day":'15'},
                {"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'},
                {"value":'875', "type":'in', "description":'grant', "day":'7'},
                {"value":'250', "type":'out', "description":'heat', "day":'29'},
                {"value":'75', "type":'out', "description":'water', "day":'17'},
                {"value":'1000', "type":'out', "description":'fuel', "day":'1'},
                {"value":'578', "type":'out', "description":'food', "day":'13'},
                {"value":'298', "type":'in', "description":'b-day', "day":'30'},
                {"value":'250', "type":'out', "description":'clothes', "day":'21'},
                {"value":'900', "type":'in', "description":'financial', "day":'21'},
                {"value":'750', "type":'in', "description":'perks', "day":'17'},
                {"value":'850', "type":'out', "description":'rent', "day":'26'}]

