def count_smileys(list):

    # List is empty
    if not list:
        return 0
    
    valid_eyes = [':', ';']
    valid_noses = ['-', '~']
    valid_mouths = [')', 'D']
    
    count = 0

    # Iterate through possible smileys
    for item in list:

        if len(item) == 3:

            # If the item has a length of three, check for valid eyes, nose, and mouth
            if (item[0] in valid_eyes) and (item[1] in valid_noses) and (item[2] in valid_mouths):
                count += 1

        if len(item) == 2:

            # If the item has a length of two, check for valid eyes and mouth
            if (item[0] in valid_eyes) and (item[1] in valid_mouths):
                count += 1
    
    return count

# Output test cases
output = count_smileys([])
print(f'Number of smileys: {output}')

output = count_smileys([":)", ";(", ";}", ":-D"])
print(f'Number of smileys: {output}')

output = count_smileys([";D", ":-(", ":-)", ";~)"])
print(f'Number of smileys: {output}')

output = count_smileys([";]", ":[", ";*", ":$", ";-D"])
print(f'Number of smileys: {output}')