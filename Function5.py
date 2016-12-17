'''
5. Filter.
filter <type>
filter <type> <value>
e.g.
filter in  keep only in transactions.
filter in 100  keep only in transactions having an amount of money smaller than 100 RON.
'''

'''
The 'f_filter' function tests through 'filter_test' is the arguments that were input are valid, then
calls the correct function:
    - 'filter_type' to filter the 'transactions' list with only the specific <type>
    - 'filter_type_value to filter the 'transactions' from a specific <day> with a <type>
'''
def f_filter (transactions, args, undo_list):
    if filter_test(transactions, args) == True:
        undo_list.append(transactions[:])
        if len(args) == 1:
            filter_type(transactions,args)  
        else:
            filter_type_value(transactions, args)

'''
The function 'filter_type' updates the list transactions only with the elements which have the 'type'
that was specified.
'''        
def filter_type (transactions, args):
    if args[0] == 'in':
        transactions[:] = [entry for entry in transactions if entry.get("type") != 'out']
    else:
        transactions[:] = [entry for entry in transactions if entry.get("type") != 'in']
        
def test_filter_type():
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
            {"value":'375', "type":'out', "description":'laptop', "day":'13'},
             {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    filter_type(l, ['in'])
    assert l == [{"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    filter_type(l,['out'])
    assert l == []
'''
the function 'filter_type_value' removes all transactions from the list which do not respect the 
specifications of the user: type and value < value specified.
'''
def filter_type_value (transactions, args):
    if args[0] == 'in':
        transactions[:] = [entry for entry in transactions if entry.get("type") != 'out' 
                        and int(entry.get('value')) < int(args[1])]
    else:
        transactions[:] = [entry for entry in transactions if entry.get("type") != 'in' 
                        and int(entry.get('value')) < int(args[1])]

def test_filter_value():
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
            {"value":'375', "type":'out', "description":'laptop', "day":'13'},
            {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    filter_type_value(l, ['out', '2001'])
    assert l == [{"value":'2000', "type":'out', "description":'car', "day":'21'},
            {"value":'375', "type":'out', "description":'laptop', "day":'13'}]
    filter_type_value(l, ['out','100'])
    assert l == [] 

def undo(transactions, args, undo_list):
    #test_undo(undo_list)
    if not undo_list:
        undo_noaction_print()
    else:
        transactions[:] = undo_list[-1]
        del(undo_list[-1])
    
def test_undo(undo_list):
    l = [{"value":'2000', "type":'out', "description":'car', "day":'21'},
            {"value":'375', "type":'out', "description":'laptop', "day":'13'},
            {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    filter_type_value(l, ['out', '2001'])
    assert l == [{"value":'2000', "type":'out', "description":'car', "day":'21'},
            {"value":'375', "type":'out', "description":'laptop', "day":'13'}]
    undo(l, [], undo_list)
    assert l == [{"value":'2000', "type":'out', "description":'car', "day":'21'},
            {"value":'375', "type":'out', "description":'laptop', "day":'13'},
            {"value":'3500', "type":'in', "description":'salary', "day":'21'}]
    filter_type_value(l, ['out','100'])
    assert l == [] 
    undo(l, [], undo_list)
    assert l == [{"value":'2000', "type":'out', "description":'car', "day":'21'},
            {"value":'375', "type":'out', "description":'laptop', "day":'13'}]

def undo_noaction_print():
    print("There are no more actions to undo.")

'''
Test function for f_filter which validates the data input by user. Returns True if the data is correct
and False otherwise.
'''
def filter_test (transactions, args):
    if len(args) > 2 or (len(args) == 1 and args[0] not in ['in', 'out']) or (len(args) == 2 and args[1].isdigit() == False) :
        print ("Please input a command with the following syntax: filter <type> (<value>).")
        return False
    return True

test_filter_type()
test_filter_value()