from collections import Counter

# Function to count the frequency of elements in a list
def count_frequency(lst):
    return Counter(lst)

# Input a list
lst = input("Enter elements of the list separated by space: ").split()

# Display the frequency of elements
print("Frequency of elements in the list:", count_frequency(lst))
