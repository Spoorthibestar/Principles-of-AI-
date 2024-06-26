# Function to perform binary search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # x is not present in array
    return -1

# Input a sorted list
arr = list(map(int, input("Enter elements of the sorted list separated by space: ").split()))

# Input the element to search for
x = int(input("Enter the element to search for: "))

# Perform binary search
result = binary_search(arr, x)

# Display the result
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in the list")
