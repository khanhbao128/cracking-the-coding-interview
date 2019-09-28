# 1.1 Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def contains_duplicates(given_str):

    letters = {}
    for char in given_str:
        if char in letters:
            return False
        else: 
            letters[char] = True
    return True


print(contains_duplicates("hello"))
print(contains_duplicates("ndhsko"))

# Run time complexity: O(n)
# Space complexity: O(n)