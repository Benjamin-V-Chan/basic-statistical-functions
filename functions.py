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

def sort(data):
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
    return