def every_three_nums(start) : 
    return list(range(start, 101, 3))

def remove_middle(lst, start, end) : 
    del lst[start:end+1]
    return lst

def more_frequent_item(lst, item1, item2) :
    if (lst.count(item1) > lst.count(item2)): 
        return item1
    elif (lst.count(item2) > lst.count(item1)) : 
        return item2
    else : 
        return item1 

def double_index(lst, index) :
    if (index >= -len(lst)) and (index <= len(lst)) : 
        new_list = lst
        new_list[index] = lst[index]*2
        return new_lst
    else : 
        return lst

def middle_element(lst) : 
    if (len(lst)%2 == 0) : 
        middle_index = (round(len(lst)/2))
        return (lst[middle_index-1] +  lst[(middle_index)])/2
    else : 
        return lst[(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))