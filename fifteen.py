# Function to calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Input the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Display the area
print("The area of the triangle is:", area_of_triangle(base, height))
