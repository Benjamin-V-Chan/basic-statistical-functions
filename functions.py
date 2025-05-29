def sum(data):
    total = 0
    for data_point in data:
        total += data_point
    return total

def length(data):
    length = 0
    for _ in data:
        length += 1
    return length

def merge_sorted_lists(list1, list2):
    result_list = []
    result_list_length = 0 # Using a counter since more efficient then using length() each time
    total_list_length = length(list1) + length(list2) # Total number of items
    while result_list_length < total_list_length:
        return
        
def sort(data): # Merge sort
    return

def average(data):
    return sum(data) / length(data) 

def min(data):
    lowest = data[0]
    for data_point in data[1:]:
        if data_point < lowest:
            lowest = data_point
    return lowest

def max(data):
    highest = data[0]
    for data_point in data[1:]:
        if data_point > highest:
            highest = data_point
    return highest

def median(data):
    return

def quartile(data):
    return

def standard_deviation(data):
    mean = average(data)
    difference_squared_data = []
    for data_point in data:
        difference_squared_data.append((data_point - mean) ** 2)
    return (sum(difference_squared_data) / (length(data) - 1)) ** 0.5