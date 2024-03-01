def true_index_list(index_list): 
    #takes in the list and restores the true values for it. Given in this program where the indexes I work with are not noramlized to indexes in the list.
    true_index_list = []

    for a in index_list: 
        a = a -1
        true_index_list.append(a)
    
    return true_index_list



#this function searches for the opposing close bracket of the opening bracket. That way I can make sure that, the +_sign that comes after it is not within the equation and that it can be treated by itself.
def ttj(index_list, index_count, initial_equation): 
    open_paranthesis = []
    closed_paranthesis = []
    return_list = []
    
    index_list = index_list[index_count:]
    #zum Bearbeiten der originallen Funktion.
    real_index_list = true_index_list(index_list)

    #marked concept
    #need to store for the index of the thing
    marked_dictionary = {}
    count = -1
    for a in initial_equation[real_index_list[0]:]:
        count += 1
        marked_dictionary[count] = "undone" 
    count = -1 
    for a in real_index_list:
        count += 1
        if count < len(index_list):
            local_count = -1
            for w in initial_equation[real_index_list[0]:real_index_list[count]]:
                local_count += 1 
                if w == "(":
                    if marked_dictionary[local_count] == "undone":
                        open_paranthesis.append(w)
                        marked_dictionary[local_count] = "done"
                if w == ")":
                    if marked_dictionary[local_count] == "undone":
                        closed_paranthesis.append(w)
                        marked_dictionary[local_count] = "done"
        if len(open_paranthesis) == len(closed_paranthesis): 
            if len(open_paranthesis) != 0:
                return_list.append(real_index_list[0] +1) #  the adjusted value for the list.
                return_list.append(real_index_list[count]) # the adjusted stop value for the list.
                break
