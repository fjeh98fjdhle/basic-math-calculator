from basis_functions import function
from basis_functions import count_of_total_index
from basis_functions import list_to_functions
from test4_assistant import ttj
from test4_assistant import true_index_list

equation = [[1, "*","x"],["+"],[12, "*", "x"],["+"],[3, "*", "y", "**", 2], ["+"], [27, "*", "c"]]

initial_equation = [1, "+", 3, "*","(", "x", "+", 12,")", "*", "x", "+", 3, "*", "y", "**", 2,"+", 27, "*", "c"]
initial_equation = [1, "+", "(", 1, "*","(", 3, "+", "(", 5, "+", 2, ")",")", "+", ")", "+"] #1

#gives back the indexes for all of the plus signs in a list. 
#the value of the individual index is given so that I want to a space in a list it is adjusted to the starting point.

def index_plus_finder(list):
    initial_equation = list
    #indexes of all the plus signs in the equation.
    index_plus = []
    index_count = -1 
    for a in initial_equation: 
        index_count += 1 
        if a == "+":
            index_plus.append(index_count + 1) # index is adjusted to "starting from" in a list so that when you start in a list you do not get the "+" as well.

    return index_plus



# this returns if there is a paranthesis inbetween a given space for the x's in a list
def check_for_paranthesis(index_1st, index_2nd, initial_equation): 
    parenthesis = False
    parenthesis_parts = []

    #initial_values
    parenthesis_parts.append(0)
    parenthesis_parts.append(0)


    for a in initial_equation[index_1st:index_2nd]: 
        if a == "(": 
            parenthesis_parts[0] += 1
        elif a == ")":
            parenthesis_parts[1] += 1

    #the problem is what if there is an paranthesis in the function but it closes before the next "+" sign.
    #To not write write for the case that one parenthesis is not closed we can generalize and say that if the number of parenthesises of both the start and the end are not equal, then it is true, that there is a paranthesis.     
    if parenthesis_parts[0] == parenthesis_parts[1]:
        parenthesis = False
    if parenthesis_parts[0] != parenthesis_parts[1]:
        parenthesis = True

    return parenthesis      
  
        

# finds the right intervalls for the application of the sum rule.
def finding_the_right_intervalls(initial_equation):
    print(initial_equation)

    #necessary list
    index_plus = index_plus_finder(initial_equation)
    list = []
    local_true_marked ={}
    total_count_of_equation = count_of_total_index(initial_equation)
    in_range = len(index_plus)
   
    #marks all the values as unmarked. It is necessary because if I iterate through the whole equation and I want to mark some of the paranthesis as already done, I can do that, but by default all should be unmarked.
    for a in index_plus:
        local_true_marked[a] = "unmarked"
    #once this is marked the paranthesis will not be added once more as it goes through that function, hence making sure that the count of paranthesis are correct.

    #first value is being tested that can not be tested in the list, because I did not append it to the last list.
    func_1st_paranthesis = check_for_paranthesis(0, index_plus[0] -1, initial_equation)
    if func_1st_paranthesis == False: 
        list.append(0)
        list.append(index_plus[0]-1)
    elif func_1st_paranthesis == True: 
        list_ttj = ttj(index_plus, count, initial_equation) 
        #marking the values that got out but also the ones in between them.
        list_ttj_1 = list_ttj[0]
        list_ttj_2 = list_ttj[1]
        #marking the values that got out but also the ones in between them.
        on_1 = index_plus.index(list_ttj_1)
        on_2 = index_plus.index(list_ttj_2 +1) # since the initial list gives values that are plus one, which is good 
        on_diff_len = on_2 - on_1 
        local_count_marked = -1
        for a in range(on_diff_len + 1): #since the for loop has to also mark the current one, one should normalize the count so that you get index_plus[0] in the first round. If we that however we need to add one round 
            local_count_marked += 1      #the for in range loop.
            current = index_plus[on_1 + local_count_marked]
            local_true_marked[current] = "marked"
        list.append(list_ttj_1)
        list.append(list_ttj_2)

    count = -1
    #always add to the function, because then it can check the last part of the equation as well. 
    initial_equation.append("+")
    index_plus.append(total_count_of_equation + 1)  
    
    #I will leave it in just in case, but the main point is that it goes through all the 
    #for n in range(in_range):  
    for var in index_plus:
        count += 1 

        if count < in_range-1:
            paranthesis = check_for_paranthesis(index_plus[count], index_plus[count +1]-1, initial_equation)
            if paranthesis == False: 
                list.append(index_plus[count]) # adjusted start and stop value, not real start and stop values. Difference is that you use the adjusted start and stop value to call a section in a list so that you do not get the "+" sign as well. It is not the real index of where "+" sign lies.
                list.append(index_plus[count+1]-1)
            elif paranthesis == True:
                if local_true_marked[var] == "unmarked":
                    list_ttj = ttj(index_plus, count, initial_equation) 
                    #marking the values that got out but also the ones in between them.
                    list_ttj_1 = list_ttj[0]
                    list_ttj_2 = list_ttj[1]
                    #marking the values that got out but also the ones in between them.
                    on_1 = index_plus.index(list_ttj_1)
                    on_2 = index_plus.index(list_ttj_2 +1) # since the initial list gives values that are plus one, which is good 
                    on_diff_len = on_2 - on_1 
                    local_count_marked = -1
                    for a in range(on_diff_len + 1): #since the for loop has to also mark the current one, one should normalize the count so that you get index_plus[0] in the first round. If we that however we need to add one round 
                        local_count_marked += 1      #the for in range loop.
                        current = index_plus[on_1 + local_count_marked]
                        local_true_marked[current] = "marked"
                    list.append(list_ttj_1)                        
                    list.append(list_ttj_2) 

        elif count == in_range-1: 
            paranthesis = check_for_paranthesis(var, total_count_of_equation, initial_equation)
            if paranthesis == False: 
                list.append(index_plus[count]) # adjusted start and stop value, not real start and stop values.
                list.append(total_count_of_equation+1)
            elif paranthesis == True:
                if local_true_marked[var] == "unmarked":
                    list_ttj = ttj(index_plus, count, initial_equation) 
                    list_ttj_1 = list_ttj[0]
                    list_ttj_2 = list_ttj[1]
                    #marking the values that got out but also the ones in between them.
                    on_1 = index_plus.index(list_ttj_1)
                    on_2 = index_plus.index(list_ttj_2 +1) 
                    on_diff_len = on_2 - on_1 
                    local_count_marked = -1
                    for a in range(on_diff_len + 1): #since the for loop has to also mark the current one, one should normalize the count so that you get index_plus[0] in the first round. If we that however we need to add one round 
                        local_count_marked += 1      #the for in range loop.
                        current = index_plus[on_1 + local_count_marked]
                        local_true_marked[current] = "marked"
                    list.append(list_ttj_1)                        
                    list.append(list_ttj_2) 
    return list



def containerized_function(right_intervalls, initial_equation):
    #two parallel lists, one with the first values for the start, the second for the values with the stop.
    first_list = []
    second_list = []
    #Es wird gemacht, indem man countet/zählt(ohne index) für jeden Wert und wenn dieser Wert in der Liste durch 2 einen int ergibt(gerade Zahl), dann wird der in die Liste gebracht und wenn er einen float ergibt dann zwei. 
    #So kann man effektiv einteilen in zwei Gruppen, eine mit den Anfangswerten und eine andere mit den Stoppwerten.
    
    total_lenght = len(right_intervalls) / 2
    total_lenght = int(total_lenght) -1 
    first_1_var = right_intervalls[0]
    first_list.append(first_1_var)
    second_1_var =  right_intervalls[1]
    second_list.append(second_1_var)
    count = 0
    for a in range(total_lenght):
        count +=2
        var_1_count = count
        var_1 = right_intervalls[var_1_count]
        first_list.append(var_1)
        var_2_count = var_1_count + 1
        var_2 = right_intervalls[var_2_count]
        second_list.append(var_2)
        
    round = -1
    part_equation = []
    whole_equation = []
    in_range = len(first_list)
    for a in range(in_range):
        round += 1 
        part_equation = initial_equation[first_list[round]: second_list[round]]
        whole_equation.append(part_equation)
        whole_equation.append(["+"])
    whole_equation = whole_equation[:-1]

    return whole_equation


