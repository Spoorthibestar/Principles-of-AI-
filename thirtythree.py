# Function to find the common elements in two lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Input two lists
lst1 = input("Enter elements of the first list separated by space: ").split()
lst2 = input("Enter elements of the second list separated by space: ").split()

# Display the common elements
print("Common elements:", common_elements(lst1, lst2))
