from basis_functions import function
from basis_functions import count_of_total_index
from basis_functions import list_to_functions
from test4_assistant import ttj
from test4_assistant import true_marked


equation = [[1, "*","x"],["+"],[12, "*", "x"],["+"],[3, "*", "y", "**", 2], ["+"], [27, "*", "c"]]

initial_equation = [1, "+", 3, "*","(", "x", "+", 12,")", "*", "x", "+", 3,")", "*", "y", "**", 2,"+", 27, "*", "c"]

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


def true(initial_equation): 
    lena = len(initial_equation) + 1
    list_x = []
    list_x.append(0)
    kon = index_plus_finder(initial_equation)
    for a in kon: 
        list_x.append(a)
    list_x.append(lena)

    list_paranthesis =[]
    true_map = {}

    count = -1
    for a in list_x: 
        count += 1
        if count +1 < len(list_x): 
            a = check_for_paranthesis(list_x[count], list_x[count+1], initial_equation)
            list_paranthesis.append(a)


    count = -1
    for a in list_paranthesis:
        count +=1
        x = list_x[count] 
        true_map[x] = a
    
    return true_map
  
        

# finds the right intervalls for the application of the sum rule.
def finding_the_right_intervalls(initial_equation):
    index_plus = index_plus_finder(initial_equation)
    value_list = {}
    list = []
    true_map = {}
    local_true_marked ={}

    #by default all the true's in the initial_equation are undone.
    for a in index_plus:
        local_true_marked[a] = "undone"

    total_count_of_equation = count_of_total_index(initial_equation)   
    in_range = len(index_plus)

    func_1st_paranthesis = check_for_paranthesis(0, index_plus[0] -1, initial_equation)
    if func_1st_paranthesis == False: 
        value_list[0] = func_1st_paranthesis
        list.append(0)
        list.append(index_plus[0]-1)
    elif func_1st_paranthesis == True: 
        ttj_var = ttj(index_plus, total_count_of_equation, index_plus)
        value_1 = ttj_var[0]
        list.append(value_1)
        value_2 = ttj_var[1]
        list.append(value_2)
        count_finished_x = ttj_var[2]
        int_true_marked = true_marked(count, count_finished_x, index_plus)
        for a in int_true_marked: 
            local_true_marked[a] = "done"

    count = -1
    initial_equation.append("+")
    index_plus.append(total_count_of_equation + 1)
    for n in range(in_range):    
        for var in index_plus:
            count += 1 
            if count < in_range-1:
                paranthesis = check_for_paranthesis(index_plus[count], index_plus[count+1] - 1, initial_equation)
                value_list[count] = paranthesis
                if paranthesis == False: 
                    list.append(index_plus[count]) # adjusted start and stop value, not real start and stop values. Difference is that you use the adjusted start and stop value to call a section in a list so that you do not get the "+" sign as well. It is not the real index of where "+" sign lies.
                    list.append(index_plus[count+1]-1)
                elif paranthesis == True:
                    temp = index_plus[count]
                    if local_true_marked[temp] == "undone":
                        ttj_var = ttj(index_plus, count, initial_equation)
                        value_1 = ttj_var[0]
                        list.append(value_1)
                        value_2 = ttj_var[1]
                        list.append(value_2)
                        count_finished_x = ttj_var[2]
                        int_true_marked = true_marked(count, count_finished_x, index_plus)
                        for a in int_true_marked: 
                            local_true_marked[a] = "done"
            elif count == in_range-1: 
                paranthesis = check_for_paranthesis(var, total_count_of_equation, initial_equation)
                value_list[count] = paranthesis
                if paranthesis == False: 
                    list.append(index_plus[count]) # adjusted start and stop value, not real start and stop values.
                    list.append(total_count_of_equation+1)
                elif paranthesis == True:
                    temp = index_plus[count]
                    if local_true_marked[temp] == "undone":
                        ttj_var = ttj(index_plus, total_count_of_equation, index_plus)
                        value_1 = ttj_var[0]
                        list.append(value_1)
                        value_2 = ttj_var[1]
                        list.append(value_2)
                        count_finished_x = ttj_var[2]
                        int_true_marked = true_marked(count, count_finished_x, index_plus)
                        for a in int_true_marked: 
                            local_true_marked[a] = "done"
    print(list)
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



a = finding_the_right_intervalls(initial_equation)
b = containerized_function(a, initial_equation)
print(b)