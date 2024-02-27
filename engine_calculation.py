list_format = [1.0, '*', 1.0, '+', 1.0, 2.0, '*', 1.0]

# writes an equation as a list. 
def list_encoding(a):
    a = str(a)
    list = []
    for w in a: 
        if w == "1":
            w = float(w)
            list.append(w)
        elif w == "2":
            w = float(w)
            list.append(w)
        elif w == "3":
            w = float(w)
            list.append(w)
        elif w == "4":
            w = float(w)
            list.append(w)
        elif w == "5":
            w = float(w)
            list.append(w)
        elif w == "6":
            w = float(w)
            list.append(w)
        elif w == "7":
            w = float(w)
            list.append(w)
        elif w == "8":
            w = float(w)
            list.append(w)
        elif w == "9":
            w = float(w)
            list.append(w)
        elif w == "0":
            w = float(w)
            list.append(w)
        else: 
            list.append(w)

    return list 


#necessary for calculations with paranthesis. checks the index in a list of the nearest paranthesis")". 
def closest_bracket(list):
    count_index = []
    index = -1  
    for a in list: 
        index += 1
        if a == ")": 
            print(count_index)
            count_index.append(index) # list of the indexes of the list. 
    count_index = sorted(count_index)
    closest_bracket = count_index[0]

    return closest_bracket




def count_of_total_index(list): 
    count_total_index = -1
    for a in list: 
        count_total_index += 1
    
    return count_total_index



def more_than_2_new(list):  
    return_list = ["this is a mistake. Your functions has become nonexistent."]
    recon_struction_list = []
    index_a = -1
    count = 0 
    count_total = count_of_total_index(list)
    for a in list: 
        index_a += 1 
        if index_a != count_total:
            if isinstance(list[index_a], (float, int)) == True:
                if isinstance(list[index_a +1], (float, int)) == True:
                    count += 1 # counts the operations performed. I did this to eliminate the iterations_needed completely. Becuase eveytime there is a change in the list there one iteration needed. 
                    new_num = str(int(list[index_a])) + str(int(list[index_a +1]))
                    new_num = float(new_num)
                    #reconstruction 
                    for a in list[:index_a]:
                        recon_struction_list.append(a)
                    recon_struction_list.append(new_num)
                    if index_a+2 <= count_total: #if 2 numbers from now on there is another value in the list, then append everything from there on in the list. 
                        for a in list[index_a+2:]:
                            recon_struction_list.append(a)
            elif list[index_a] == "*":
                if list[index_a +1] == "*":
                    count += 1
                    new_op = list[index_a] + list[index_a +1]
                    for a in list[:index_a]:
                        recon_struction_list.append(a)
                    recon_struction_list.append(new_op)
                    if index_a+2 <= count_total:
                        for a in list[index_a+2:]:
                            recon_struction_list.append(a)
            elif list[index_a] == ",":
                if isinstance(list[index_a +1], (float, int)) == True:
                    count += 1
                    num_before = list[index_a -1]
                    comma = "."
                    num_after = list[index_a +1]
                    new_num = str(int(num_before)) + comma + str(int(num_after))
                    new_num = float(new_num)
                    for a in list[:index_a -1]:
                        recon_struction_list.append(a)
                    recon_struction_list.append(new_num)
                    if index_a+2 <= count_total:
                        for a in list[index_a+2:]:
                            recon_struction_list.append(a)

        if len(recon_struction_list) != 0: # this is key. Because as long as the list is not none-existent it will return it. 
            return recon_struction_list
    
    return return_list
    
        
def iterations_needed(list):
    counter_iterations = 0
    counter = -1
    count_total = count_of_total_index(list)
    for a in list: 
        counter += 1
        if counter != count_total: 
            if isinstance(list[counter], (int, float)):
                if isinstance(list[counter+1], (int, float)):
                    counter_iterations += 1
            elif a == ",":
                counter_iterations += 1
            if list[counter] == "*":
                if list[counter +1] == "*": 
                    counter_iterations += 1

    return counter_iterations


def more_than_2_complete(list):
    in_range = iterations_needed(list)
    for a in range(in_range):
        list = more_than_2_new(list)

    return list 



#calculation
def priority(list):
    list  = list
    count_op = 0
    value_op ={'(':4, '**': 3, "*":2, "/":2, "+":1, "-":1 ,")": 0}
    op_priority = {"current_op": 0}
    list_op = []
    for a in list:
        if isinstance(a, (str)) == True:
            list_op.append(a)
    for a in list_op: 
        count_op += 1
        if value_op[a] > op_priority["current_op"]:
            op_priority["current_op"] = value_op[a]   

    return op_priority["current_op"]

def op_selection(list): 
    print(list)
    op_prioritizer = priority(list)
    value_op ={'(':4, '**': 3, "*":2, "/":2, "+":1, "-":1 ,")": 0}
    count_total = count_of_total_index(list) # total index_count.
    store_value = []  
    store_index_op = []

    index_count = -1
    for a in list:
        index_count += 1 # index of each value in list.
        if isinstance(a,(str)) == True: #these 2 if basically assure that (1) it is an operator/string and (2) that the value mapped to the operator is the op_prioritize/the highest priority operator. 
            if value_op[a] == op_prioritizer: # If this is the case, then one performs the operation with the value indexd before and after it. 
                if a == "(": # I need to check for priororization within the brackets. To do that I need to go to the end of the brackets and apply priorization again. 
                    cb = closest_bracket(list) 
                    bracket_count = 0
                    prioritizer = priority(list[index_count +1:cb])
                    for var in list[index_count +1 :cb]: 
                        bracket_count += 1
                        if len(list[index_count+1:cb]) == 1: 
                            a = list[index_count+1:cb]
                            store_value.append(a[0])
                            store_index_op.append(index_count + 1) #indem ich das ergebnis als rechnung speichere, geht es durch dasselbe Verfahren wie bei einer Rechnung, wo die zwei werte um den indexierten wert eliminiert werden und der indexierte Wert stattdessen mit dem ergebnis der Rechnung gerechnet wird. 
                        if isinstance(var,(str)) == True:
                            if value_op[var] == prioritizer: 
                                if list[index_count + bracket_count] == "+":
                                    num_before = list[index_count+bracket_count -1]
                                    num_after = list[index_count+bracket_count + 1]
                                    num_total = num_before + num_after
                                    store_value.append(num_total)
                                    store_index_op.append(index_count + bracket_count)

                                elif list[index_count + bracket_count] == "*":
                                    num_before = list[index_count+bracket_count -1]
                                    num_after = list[index_count+bracket_count+ 1]
                                    num_total = num_before * num_after
                                    store_value.append(num_total)
                                    store_index_op.append(index_count + bracket_count)

                                elif list[index_count + bracket_count] == "/":
                                    num_before = list[index_count+bracket_count -1]
                                    num_after = list[index_count+bracket_count + 1]
                                    num_total = num_before / num_after
                                    store_value.append(num_total)
                                    store_index_op.append(index_count + bracket_count)

                                elif list[index_count + bracket_count] == "-":
                                    num_before = list[index_count+bracket_count-1]
                                    num_after = list[index_count+bracket_count+1]
                                    num_total = num_before - num_after
                                    store_value.append(num_total)
                                    store_index_op.append(index_count + bracket_count)

                                elif list[index_count + bracket_count] == "**":
                                    num_before = list[index_count+bracket_count-1]
                                    num_after = list[index_count+bracket_count+1]
                                    num_total = num_before ** num_after
                                    store_value.append(num_total)
                                    store_index_op.append(index_count + bracket_count)
                                else:
                                    print("What the fuck is that for an operation?")
                else: 
                    if list[index_count] == "+":
                        num_before = list[index_count-1]
                        num_after = list[index_count+1]
                        num_total = num_before + num_after
                        store_value.append(num_total)
                        store_index_op.append(index_count)
                    elif list[index_count] == "*":
                        num_before = list[index_count-1]
                        num_after = list[index_count+1]
                        num_total = num_before * num_after
                        store_value.append(num_total)
                        store_index_op.append(index_count)
                    elif list[index_count] == "/":
                        num_before = list[index_count-1]
                        num_after = list[index_count+1]
                        num_total = num_before / num_after
                        store_value.append(num_total)
                        store_index_op.append(index_count)
                    elif list[index_count] == "-":
                        num_before = list[index_count-1]
                        num_after = list[index_count+1]
                        num_total = num_before - num_after
                        store_value.append(num_total)
                        store_index_op.append(index_count)
                    elif list[index_count] == "**":
                        num_before = list[index_count-1]
                        num_after = list[index_count+1]
                        num_total = num_before ** num_after
                        store_value.append(num_total)
                        store_index_op.append(index_count)
                    elif list[index_count] == ")": 
                        a = a

    return [list, store_value[0], store_index_op[0], count_total]


def recon_struction(list):

    list_new = list[0]
    num_total = list[1]
    index_count = list[2]
    list_count = list[3] # represents the total number of indexes.
    list = list_new # doing it so because otherwise it would not store the value with index 0 as the new list and so the values would be wrong.


    re_con_list = []


    #recon_before
    for a in list[:index_count-1]: 
        re_con_list.append(a)
    #checks if the the value before it is an equation or if the computed value is part of the equation:
    if list[index_count -2] == "+" or "*" or "-" or "/" or "**":
        re_con_list.append(num_total)
    elif isinstance(list[index_count -2], (int, float)) == True:
        if num_total <= 0:
            re_con_list.append("-")
        elif num_total >= 0:
            re_con_list.append("+")
            re_con_list.append(num_total)
    else:
        print("Here, there is a mistake.")
    #recon_after 
    if index_count +2 <= list_count:
    #if 2 values added to the index of the operation is still lower than the list_count. In other words if there comes something after this operation. 
        if list[index_count +2] == "*" or "+" or "-" or "/" or "**" or ")":
            for a in list[(index_count + 2):]:
                re_con_list.append(a)
        elif isinstance(list[index_count + 2],(float, int)): 
            re_con_list.append("+")
            for a in list[(index_count + 2):]:
                re_con_list.append(a)

    return re_con_list  


#for the number of iterations
def list_counter(list):
    list = list
    list = more_than_2_complete(list)
    count = 0
    for a in list:
        if isinstance(a, (str)):
            count += 1
        
    return count


def calculate(list):
    in_range = list_counter(list)
    if in_range == 0: 
        return list 
    else:
        for a in range(in_range):
            total = len(list)
            if total != 1:
                list = more_than_2_complete(list)
                #actual calculation
                op_prioritizer = priority(list)
                list = op_selection(list)
                list = recon_struction(list)
                

    return list[0]
