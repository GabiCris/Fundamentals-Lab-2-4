'''
1. Add new transactions to the list.
add <value> <type> <description>
insert <day> <value> <type> <description>
e.g.
add 100 out pizza  adds to the current day an out transaction of 100 RON with the pizza description.
insert 25 100 in salary  insert to day 25 an in transaction of 100 RON with the salary description.
'''

import time
from copy import deepcopy

'''
The function "create_tran" takes the data from the user input and creates a new transaction to 
be added as a result of calling "f_add" or "f_insert".
'''
def create_tran (argum):
    if len(argum) == 3:
        return {"value" : argum[0],
            "type" : argum[1],
            "description" : argum[2],
            "day" : time.strftime("%d")
            }

    elif len(argum) == 4:
        return {"day" : argum[0],
            "value" : argum[1],
            "type" : argum[2],
            "description" : argum[3]
            }
        
def f_add(transactions, argum, undo_list):
    if add_verify(argum) == True:
        undo_list.append(deepcopy(transactions))
        transactions.append(create_tran(argum))

def f_insert(transactions, argum, undo_list):
    if insert_verify(argum) == True:
        undo_list.append(deepcopy(transactions))
        transactions.append(create_tran(argum))

'''
The functions "add_verify" and "insert_verify" check the validiy of the data introduced by the user.
If the data is not legit, False will be returned along with a message that will prompt the user 
to retype the command.
'''
def add_verify (argum):
    if len(argum) != 3:
        print("Please input a valid instruction.")
        return False
    if argum[0].isdigit() == False:
        print ("Please input a positive integer number for the value of the transaction.")
        return False
    if argum[1] not in ['in', 'out']:
        print ("Please specify the type of the transaction using 'in' or 'out'.")
        return False
    return True
    
def insert_verify (argum):
    if len(argum) != 4:
        print("Please input a valid instruction.")
        return False
    if argum[0].isdigit() == False or int(argum[0]) not in range(1,31):
        print("Please input a valid day in the interval 1 - 30.")
        return False
    if argum[1].isdigit() == False:
        print ("Please input a positive integer number for the value of the transaction.")
        return False
    if argum[2] not in ['in', 'out']:
        print ("Please specify the type of the transaction using 'in' or 'out'.")
        return False
    return True

def test_add():
    a = []
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    f_add(l,['25','in','pizza'], a)
    assert l == [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'},
                {"value":'25', "type":'in', "description":'pizza', "day":time.strftime("%d")}]
    l = []
    f_add(l,['25','in','pizza'], a)
    assert l == [{"value":'25', "type":'in', "description":'pizza', "day":time.strftime("%d")}]

def test_insert():
    a = []
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    f_insert(l,['25','100','in','pizza'], a)
    assert l == [{"value":'2000', "type":'out', "description":'car', "day":'21'},
                {"value":'375', "type":'out', "description":'laptop', "day":'13'},
                {"value":'3500', "type":'in', "description":'salary', "day":'21'},
                {"value":'100', "type":'in', "description":'pizza', "day":'25'}]
    l = []
    f_insert(l,['25','100','in','pizza'], a)
    assert l == [{"value":'100', "type":'in', "description":'pizza', "day":'25'}]

test_insert()
test_add()    