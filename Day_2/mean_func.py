from script import app_data 

def get_data(dataset, indexValue):
    columnSet = []
    output = dataset[1:]

    for element in output:
        columnSet.append(float(element[indexValue]))
    return columnSet

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += element
    return a_sum

def find_lenght(a_list):
    a_length = 0
    for element in a_list:
        a_sum += 1
    return a_length

def mean(list_column, indexValue):
    a_list = get_data(list_column, indexValue)
    sum_list = find_sum(a_list)
    lenght_list = find_lenght(a_list)

    return sum_list/lenght_list
print(round(mean(app_data, 3)), 2)