# This is the input string we need to convert into denary 
romanInput = 'IX'

# define the different roman numeral in a dictionary to make look up O(1)
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L':  50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

# i is used to keep track of the index of the character in the string we should look at 
# x is the sum of the converted roman numeral  
i = 0
value = 0 

# # Loop through the string using a while loop
# while i < len(romanInput):
#     # Check if the value after the current index is less then the next value in the string to handle subtracktion cases 
#     if i +1 < len(romanInput) and roman[romanInput[i]] < roman[romanInput[i + 1]]:
#         # If subtraction parameter is meet we add it to x 
#         value += roman[romanInput[i + 1]] - roman[romanInput[i]]
#         # Then skip two  character in the input string to the next character to look at  
#         i += 2
#     else:
#         # If there is no subtraction case we simply check the index value against our dict and add it to x and skip one character in the string 
#         value += roman[romanInput[i]]
#         # Then increase the index by one to handle the next character in the string 
#         i += 1

# print(x)

while i < len(romanInput):
    if i+1 <len(romanInput) and roman[romanInput[i]] < roman[romanInput[i + 1]]:
        value += roman[romanInput[i + 1]] - roman[romanInput[i]]
        i += 2
    else:
        value += roman[romanInput[i]]
        i += 1


while i < len(romanInput):
    if i + 1 < len(romanInput) and roman[romanInput[i]] < roman[romanInput[i + 1]]:
        value += roman[romanInput[i + 1]] - roman[romanInput[i]]
        i += 2
    else: 
        value += roman[romanInput[i]]
        i += 1
print(romanInput, value)
