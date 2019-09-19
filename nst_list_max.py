''' list1 = [1,2,37,67,[45,78],[90,10]]
list2= []
for i in list1:
    if type(i)==list:
        list2.append(max(i))
    else:
        list2.append(i)
print(max(list2))
'''


list4 = []
def get_max(list3):
    for i in list3:
        if type(i)==list:
            get_max(i)
        else:
            list4.append(i)
    return max(list4)

list3 =[[1,2,3,[5,6,7]],[17,16,5]]
print(get_max(list3))

