# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Display temperature in Kelvin
print("Temperature in Kelvin:", celsius_to_kelvin(celsius))
