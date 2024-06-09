# Function to convert kilometers to miles
def km_to_miles(km):
    return km * 0.621371

# Input kilometers
kilometers = float(input("Enter distance in kilometers: "))

# Display the distance in miles
print("Distance in miles:", km_to_miles(kilometers))
