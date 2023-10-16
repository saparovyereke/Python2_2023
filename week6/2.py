# 1) power function
# def power(base, exponent):
#     result = 1
#     for _ in range(exponent):
#         result *= base
#     return result

# base = int(input("Write the Base: "))
# exponent = int(input("Write the exponent: "))
# result = power(base, exponent)
# print(f"{base} to the power of {exponent} is {result}")

# 2) Generate the first n Fibonacci numbers using a lambda function
# fibonacci = lambda n: [] if n == 0 else [0] if n == 1 else [0, 1] if n == 2 else (fibonacci(n - 1) + [fibonacci(n - 1)[-1] + fibonacci(n - 1)[-2]])
# cubes = lambda n: [x ** 3 for x in fibonacci(n)]
# n = int(input("Write the number of Fibonacci: "))
# print(fibonacci(n))
# print(cubes(n))

# 4) replace symbols with other
# def modify_symbols(text):
#     new_text = text.replace('&&', ' and ').replace('||', ' or ')
#     return new_text

# input_text = input("Write your input text: ")
# output_text = modify_symbols(input_text)
# print(output_text)
