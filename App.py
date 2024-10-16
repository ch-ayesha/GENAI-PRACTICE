import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
def main():
    st.title("🌡️ Temperature Conversion App")

    # User choice for conversion
    option = st.radio("Select Conversion", ('Celsius to Fahrenheit', 'Fahrenheit to Celsius'))

    # Create a list to hold conversion history
    conversion_history = []

    if option == 'Celsius to Fahrenheit':
        # Use a slider for Celsius input
        celsius = st.slider("Select temperature in Celsius:", -50.0, 100.0, 0.0, 0.1)  # min, max, default, step
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            result_message = f"{celsius:.1f}°C is equal to {fahrenheit:.2f}°F"
            st.success(result_message)
            conversion_history.append(result_message)

    elif option == 'Fahrenheit to Celsius':
        # Use a slider for Fahrenheit input
        fahrenheit = st.slider("Select temperature in Fahrenheit:", -58.0, 212.0, 32.0, 0.1)  # min, max, default, step
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            result_message = f"{fahrenheit:.1f}°F is equal to {celsius:.2f}°C"
            st.success(result_message)
            conversion_history.append(result_message)

    # Display conversion history
    if conversion_history:
        st.subheader("Conversion History")
        for entry in conversion_history:
            st.write(entry)

    # Add a brief description or tips for users
    st.sidebar.header("Tips for Users")
    st.sidebar.write("1. Use the sliders to easily select temperatures.")
    st.sidebar.write("2. Click 'Convert' to see the results.")
    st.sidebar.write("3. View your conversion history for reference.")

if __name__ == "__main__":
    main()
