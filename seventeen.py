# Function to find the median of a list
def median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

# Input a list
lst = list(map(int, input("Enter elements of the list separated by space: ").split()))

# Display the median
print("The median is:", median(lst))
