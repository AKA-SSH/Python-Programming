# copied from chatGPT for now

from collections import OrderedDict

def check_order(input_string, pattern):
    # Create an OrderedDict to maintain the order of characters in the input string
    char_order = OrderedDict.fromkeys(input_string)

    # Check if the pattern is present in the ordered characters
    pattern_index = 0
    for char in char_order:
        if pattern_index < len(pattern) and char == pattern[pattern_index]:
            pattern_index += 1

    # If all characters in the pattern are found in order, return True; otherwise, return False
    return pattern_index == len(pattern)
# Example usage
input_str = "hello world"
pattern_to_check = "hlo"
result = check_order(input_str, pattern_to_check)
if result:
    print(f"The characters in '{pattern_to_check}' appear in order in the string.")
else:
    print(f"The characters in '{pattern_to_check}' do not appear in order in the string.")
