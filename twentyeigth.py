# Function to sort a list in ascending order
def sort_list(lst):
    return sorted(lst)

# Input a list
lst = list(map(int, input("Enter elements of the list separated by space: ").split()))

# Display the sorted list
print("Sorted list:", sort_list(lst))
