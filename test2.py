from test import check_for_paranthesis
initial_equation = [1, "+", 3, "*","(", "x", "+", 12,")", "*", "x", "+", 3,")", "*", "y", "**", 2,"+", 27, "*", "c"]
true_map = {0: False, 2: True, 7: True, 12: True, 19: False}

def ttfl_map(true_map):
    true_map = true_map # we map + indexes to the corresponding boolean values
    true_map_2 = {} # we map 1 to 5 to the corresponding + indexes.
    false_map = {} # we map 1 to 5 to the correspoding boolean values.
    total_list = []
    count = 0
    total_list.append(true_map)
    for a in true_map:
        count += 1 
        value = true_map[a]
        value = str(value) + str(count)
        false_map[count] = a
        #   1: (0, 1)  false_map
    count = 0
    total_list.append(false_map)

    for a in true_map: 
        count += 1
        value = true_map[a]
        true_map_2[count] = value
    total_list.append(true_map_2)
        #   1: False  

    return total_list



#test_map = {1:"h", 2:"a" , 3:"a", 4:"l", 5:"b", 6:"b", 7:"e" }
#we have 2 dictionary's that are important. For one we have the dictionary that pairs the key counts from 1 to x wiht the corresponding boolean value. The second dictionary maps the same counts but the actual values fo the x-indexes. 
def chek(true_map): 
    a = ttfl_map(true_map)
    compute = a[1] #maps count to boolean values
    checker = a[2] #maps count to x-indexes
    map_values = {}
    list = []
    for a in checker: 
        list.append(a)
    
    
    count = 0 
    for a in checker: 
        count += 1
        if count < len(checker):
            if checker[count] == checker[count +1]: 
                var = compute[count] + compute[count +1]
                #reconstruction before. 
                for a in list[:count]: 
                    map_values[a] = compute[a]
                map_values[count] = var
                for a in list[count+1:]: 
                    map_values[a] = compute[a]
                break
    return map_values

#looks through an dictionary and counts for when sequential ones have the same value. 
def repetitions_count(test_map): 
    list_1 = []
    list_2 = []
    for a in test_map: 
        list_1.append(a)
    
    #a list full of the values(list_2)
    for a in list_1: 
        b = test_map[a]
        list_2.append(b)

    repetition_score = 0
    count = 0 
    for a in list_2: 
        count += 1
        if count +1 < len(list_2) :
            if list_2[count] == list_2[count + 1]:
                repetition_score += 1
    
    return repetition_score

def normalize_keys(test_map):
    list = [] 
    normalized_keys = {}

    for a in test_map: 
        b = test_map[a]
        list.append(b)
    
    count = 0
    for a in list:
        count += 1
        normalized_keys[count] = a

    return normalized_keys
 

def again(test_map): 
    rep = repetitions_count(test_map)
    for a in range(rep):
        test_map = chek(test_map)
        test_map = normalize_keys(test_map)
        print(test_map)
        

    return test_map

a = again(true_map)
print(a)
