#Write your function here
def odd_indices(my_list):
    new_list = []
    for index in range(1, len(my_list), 2):
       new_list.append(my_list[index])
    print(new_list)
    return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
