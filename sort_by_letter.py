def sort_by_letter(list):

    sorted_list = []

    while len(list) != 0:
        min_element = list[0]
        for letter in min_element:
            if letter.isalpha():
                min_char = letter

        for element in list:
            for letter in element:
                if letter.isalpha():
                    target = letter
            if target < min_char:
                min_element = element

        sorted_list.append(min_element)
        list.remove(min_element)

    return sorted_list

output = sort_by_letter(["932c", "832u32", "2344b"])
print(output)

output = sort_by_letter(["99a", "78b", "c2345", "11d"])
print(output)

output = sort_by_letter(["572z", "5y5", "304q2"])
print(output)

output = sort_by_letter([])
print(output)