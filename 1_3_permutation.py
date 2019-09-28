# Given 2 strings. Determine if one is the permutation of the other
# permutation: arranging items of one set in a different orders

def unpack_string(given_string):

    new_dict = {}

    for char in given_string:
            if char not in new_dict:
                new_dict[char] = 1
            else:
                new_dict[char] += 1
    return new_dict


def is_permutation(string_1, string_2):

    if (len(string_1) != len(string_2)):
        return False
    else: 
        new_dict_1 = unpack_string(string_1)
        new_dict_2 = unpack_string(string_2)
        if (new_dict_1 == new_dict_2):
            return True


print(is_permutation("hello", "olleh"))
print(is_permutation('kdkiko', 'kikokd'))

# Time complexity: O(2n)
# Space complexity: O(2n)

        

        



