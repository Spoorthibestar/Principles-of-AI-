# Function to convert a list to a string
def list_to_string(lst):
    return ' '.join(map(str, lst))

# Input a list
lst = input("Enter elements of the list separated by space: ").split()

# Display the string
print("The list as a string is:", list_to_string(lst))
