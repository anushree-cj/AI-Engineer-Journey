num_list = [5,6,78,98,34]

def largestNumber(number_list):
    if number_list:
        largest_number = number_list[0]
        for item in number_list:
            if item >largest_number:
                largest_number = item
        return largest_number
    return None

result = largestNumber(num_list)
print("Largest number is : ",result)