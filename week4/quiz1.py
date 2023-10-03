# task 1
# def encrypt(message):
#     even_chars = message[0::2]  # Get characters at even indices
#     odd_chars = message[1::2]   # Get characters at odd indices
#     encrypted_message = even_chars + odd_chars  # Combine even and odd characters
#     return encrypted_message

# # Example usage:
# message = str(input())
# encrypted_message = encrypt(message)
# print(encrypted_message)

#task 6
# f1 = [3, 6, 9, 12, 15, 18, 21]
# f2 = [4, 8, 12, 16, 20, 24, 28]
# even = f2[::2]
# odd = f1[1::2]
# print(odd)
# print(even)

# print(odd, even)


# task 2
# def find_matching_strings(pattern, string_list):
#     # Create a dictionary to store the non-asterisk characters and their corresponding indices in the pattern
#     pattern_dict = {}
    
#     # Populate the pattern_dict
#     for index, char in enumerate(pattern):
#         if char != '*':
#             pattern_dict[index] = char
    
#     matching_strings = []
    
#     # Iterate through the list of strings
#     for string in string_list:
#         if len(string) != len(pattern):
#             continue  # Skip strings with different lengths
        
#         is_match = True
        
#         # Check if the string matches the pattern based on the pattern_dict
#         for index, char in pattern_dict.items():
#             if string[index] != char:
#                 is_match = False
#                 break
        
#         if is_match:
#             matching_strings.append(string)
    
#     return matching_strings


# task 3
# # Example usage:
# user_pattern = 'a**a****'
# string_list = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

# matching_strings = find_matching_strings(user_pattern, string_list)

# if matching_strings:
#     print("Matching strings are:")
#     for string in matching_strings:
#         print(string)
# else:
#     print("No matching strings found.")

# task 5
# Function to calculate 'a' and 'b' for a given pair of points
# def calculate_linear_equation(x1, y1, x2, y2):
#     a = (y2 - y1) / (x2 - x1)
#     b = y1 - a * x1
#     return a, b

# # Read the number of test cases
# num_test_cases = int(input())

# # Initialize a list to store the results
# results = []

# # Process each test case
# for _ in range(num_test_cases):
#     x1, y1, x2, y2 = map(int, input().split())
#     a, b = calculate_linear_equation(x1, y1, x2, y2)
#     results.append((a, b))

# # Print the results
# for result in results:
#     print(f"({int(result[0])} {int(result[1])})", end=" ")
