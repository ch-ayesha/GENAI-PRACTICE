import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
def main():
    st.title("Temperature Conversion App")
    
    # User choice for conversion
    option = st.radio("Select Conversion", ('Celsius to Fahrenheit', 'Fahrenheit to Celsius'))
    
    # If the user selects 'Celsius to Fahrenheit'
    if option == 'Celsius to Fahrenheit':
        celsius = st.number_input("Enter temperature in Celsius:", format="%.2f")
        if st.button("Convert"):
            if celsius is not None:  # Ensure valid input
                fahrenheit = celsius_to_fahrenheit(celsius)
                st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
            else:
                st.error("Please enter a valid temperature in Celsius.")
    
    # If the user selects 'Fahrenheit to Celsius'
    elif option == 'Fahrenheit to Celsius':
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
        if st.button("Convert"):
            if fahrenheit is not None:  # Ensure valid input
                celsius = fahrenheit_to_celsius(fahrenheit)
                st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
            else:
                st.error("Please enter a valid temperature in Fahrenheit.")

if __name__ == "__main__":
    main()
