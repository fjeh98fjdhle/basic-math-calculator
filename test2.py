def true_map__true_map_2__false_map__list_map(true_map):
    true_map = {(0, 1): False, (2, 7): True, (7, 12): True, (12, 19): True, (19, 22): False}
    true_map_2 = {}
    false_map = {}
    count = 0
    for a in true_map:
        count += 1 
        value = true_map[a]
        value = str(value) + str(count)
        false_map[count] = a
        #   1: (0, 1)  false_map
    count = 0
    for a in true_map: 
        count += 1
        value = true_map[a]
        true_map_2[count] = value
        #   1: False  
    list_map = []
    for a in true_map_2: 
        list_map.append(a)



#print(true_map_2) # we map 1 to 5 to the correspoding boolean values.
#print(false_map) # we map 1 to 5 to the corresponding + indexes.
#print(true_map) # we map + indexes to the corresponding boolean values

test_true_map_2 = {1:True,2: True, 3: True}
test_false_map_2 = {1:(0, 1),2: (2, 7), 3: (7, 12)}
test_map = {1:"h", 2:"a" , 3:"a", 4:"l", 5:"b", 6:"b", 7:"e" }
count = 2




def chek(test): 
    new_test = {}
    list_test = []
    new_list_test = []
    value_count =[]
    break_count = 0


    count = 0
    for a in test:
        print(len(test))
        count += 1
        print(count)
        if count < len(test):
            if len(list_test)!= len(test):
                for a in test: 
                    list_test.append(a)
                    print(list_test)
            if test[count] == test[count +1]: 
                value_count.append(count)
                print(value_count)
                neu = test[count] + test[count +1]
                print(neu)
                #reconstruction_before
                new_count = value_count[0] -1
                print(new_count)

                for a in list_test[:new_count]:
                    new_list_test.append(a)
                for new_var in new_list_test:
                    new_test[new_var] = test[new_var]
                print("new_test")
                print(new_test)

                new_number = new_list_test[-1]
                new_number += 1
                new_test[new_number] = neu

                new_list_test.clear()
                #reconstruction_after
                for a in list_test[new_count + 2:]:
                    new_list_test.append(a)
                for new_var in new_list_test: 
                    new_test[new_var] = test[new_var]
                value_count.clear()
                break_count += 1
                if break_count == 1: 
                    break
        
    
    return new_test


def again(test):
    for n in range(len(test)):
        test = chek(test)
        test = chek(test)

    return test 
    
a = again(test_map)
print(a)



#this function takes in a mapping and if the two mapped values are both True(meaning if both paranthesis) then it will add them together so that you get the 1st value of the tuple of the first mapping and the second value of the second mapping.
def false_or_right(true_map_2,false_map, count): 
    a = len(true_map_2)-count +1 
    stationary_list = []
    real_list =[]
    fake_list = []
    for x in range(a):
        if true_map_2[count] == true_map_2[count +1]:
            tuple_1 = false_map[count]
            tuple_2 = false_map[count +1]
            for a in tuple_1:
                fake_list.append(a)
            stationary_list.append(fake_list[:1])
            fake_list.clear()
            for a in tuple_2:
                fake_list.append(a)
            stationary_list.append(fake_list[1:]) 
            fake_list.clear()

            for a in stationary_list: 
                for num in a:
                    real_list.append(num)
            
            print(real_list)




    return stationary_list
