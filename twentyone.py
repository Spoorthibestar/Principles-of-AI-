# Function to find the longest palindromic substring
def longest_palindrome(s):
    n = len(s)
    table = [[False for x in range(n)] for y in range(n)]
    max_length = 1

    for i in range(n):
        table[i][i] = True

    start = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            start = i
            max_length = 2

    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if table[i][j - 1] and s[i] == s[j]:
                table[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k

    return s[start:start + max_length]

# Input a string
string = input("Enter a string: ")

# Find the longest palindromic substring
print("The longest palindromic substring is:", longest_palindrome(string))
