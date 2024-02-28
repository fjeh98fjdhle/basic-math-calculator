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

#marked: concept. when something is done you mark it.

#This function stores all the values in a dictionary that have already been done so that when you have multiple "true's" in a sequence you do not append multiple times the same number to the right_intervalls list.
def true_marked(count_x, count_finished_x, index_plus):
    marked_x = []
    #should store all the marked x

    for a in index_plus[count_x:count_finished_x + 1]: 
        marked_x.append(a)
    
    return marked_x

    
#this function goes through the index list and checks for parenthesis in the intervalls. if there are no paranthesis's in the intervall it will break the loop
#In addition to that, it will store the start of the loop, meaning the start "x-value" and the end, the last number before the intervall gave false, so no paranthesis's. 
def ttj(index_list, index_count, initial_equation): 
    index_list = index_list[index_count:]
    return_list = []
    open_paran = []
    closed_paran = []

    count = -1 
    for a in index_list:
        count += 1 
        if count +1 < len(index_list):
            for w in initial_equation[index_list[0]:index_list[count +1]]:
                if w == "(":
                    open_paran.append(index_list[count])
                elif w == ")": 
                    closed_paran.append 
                if len(open_paran) == len(closed_paran):
                    last = index_list[count+1]
                    return_list.append(w)
                    break

    return last
