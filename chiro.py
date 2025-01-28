import streamlit as st

# Initial fixed treatment prices
treatment_prices = {
    "First Consultation": 80,
    "Follow Up": 130,
    "Follow Up (Concession Rate)": 115,
    "15x Package": 1725,
}

# Function to calculate total earnings
def calculate_earnings(treatments, commission):
    total = 0
    for treatment, patient_count in treatments.items():
        if treatment in treatment_prices:
            total += treatment_prices[treatment] * patient_count
    # Applying commission percentage
    earnings_after_commission = total * (commission / 100)
    return earnings_after_commission

# Streamlit app starts here
st.title('Chiropractor Earnings Calculator')

# Display fixed treatments and prices
st.subheader('Fixed Treatments and Prices')
for treatment, price in treatment_prices.items():
    st.write(f"{treatment}: ${price}")

# Create user input for treatments
st.subheader('Enter Treatments & Patient Count')

# Dictionary to store user input for treatments and patient counts
treatments = {}

# Add input fields for treatments
num_treatments = st.number_input("How many different treatments did you perform?", min_value=1, max_value=10, step=1)

for i in range(num_treatments):
    treatment = st.selectbox(f"Treatment {i+1}", options=list(treatment_prices.keys()) + ["Custom Treatment"])
    patient_count = st.number_input(f"Number of patients for Treatment {i+1}", min_value=0, step=1)
    
    if treatment == "Custom Treatment":
        custom_name = st.text_input(f"Enter custom treatment name for Treatment {i+1}")
        custom_price = st.number_input(f"Enter price for custom treatment {i+1}", min_value=0, step=1)
        if custom_name and custom_price:
            treatment_prices[custom_name] = custom_price
            treatment = custom_name  # Update treatment to custom name
    
    if treatment != "Custom Treatment":
        treatments[treatment] = patient_count

# Commission input
commission = st.number_input("Enter your commission percentage", min_value=25.0, step=1)

# Calculate and display earnings
if st.button("Calculate Earnings"):
    total_earnings = calculate_earnings(treatments, commission)
    st.subheader(f"Total Earnings after {commission}% commission: ${total_earnings:.2f}")

# Modify Treatment Button
#if st.button("Modify Treatment Prices"):
#    st.subheader("Modify Treatment Prices")
    # Allow the user to update treatment prices
#    for treatment in list(treatment_prices.keys()):
#        new_price = st.number_input(f"New price for {treatment}", min_value=0.0, step=1.0, value=treatment_prices[treatment])
#        treatment_prices[treatment] = new_price

#    st.success("Treatment prices updated successfully!")

# Modify Treatment Button
if st.button("Modify Treatment Prices"):
    st.subheader("Modify Treatment Prices")
    # Allow the user to update treatment prices
    for treatment in list(treatment_prices.keys()):
        new_price = st.number_input(
            f"New price for {treatment}",
            min_value=0.0,
            step=1.0,
            value=float(treatment_prices[treatment])  # Ensure the value is treated as a float
        )
        treatment_prices[treatment] = new_price

    st.success("Treatment prices updated successfully!")
