import streamlit as st

# Updated emission factors specific to Indian coal mines
EMISSION_FACTORS = {
    "India": {
        "Mining": 0.85,  # kgCO2/tonne of coal mined
        "Transportation": 0.14,  # kgCO2/km for transporting coal
        "Electricity": 0.82,  # kgCO2/kWh for electricity used in mining
        "Waste": 0.1,  # kgCO2/kg for waste generated during mining operations
        "Fuel": 2.68,  # kgCO2/liter for diesel consumption
        "Methane": 25,  # kgCO2 equivalent/tonne of coal mined (methane emissions)
        "Explosives": 0.02  # kgCO2/kg of explosives used
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Coal Mine Carbon Footprint Calculator")

# Streamlit app code
st.title("Carbon Footprint Calculator For Indian Coal Mines")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["India"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("⛏️ Total coal mined (in tonnes)")
    coal_mined = st.slider("Coal Mined", 0.0, 10000.0, key="coal_mined_input")

    st.subheader("🚗 Average transportation distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("🚜 Fuel consumption (in liters)")
    fuel_consumption = st.slider("Fuel Consumption", 0.0, 5000.0, key="fuel_input")

with col2:
    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

    st.subheader("🗑️ Waste generated per month (in kg)")
    waste = st.slider("Waste", 0.0, 1000.0, key="waste_input")

    st.subheader("💥 Explosives used (in kg)")
    explosives = st.slider("Explosives", 0.0, 500.0, key="explosives_input")

# Normalize inputs
if coal_mined > 0:
    coal_mined = coal_mined  # Total coal mined in tonnes remains as is
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly (if needed)
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if waste > 0:
    waste = waste * 12  # Convert monthly waste to yearly
if fuel_consumption > 0:
    fuel_consumption = fuel_consumption  # Fuel consumption in liters remains as is
if explosives > 0:
    explosives = explosives  # Explosives usage remains as is

# Calculate carbon emissions
mining_emissions = EMISSION_FACTORS[country]["Mining"] * coal_mined
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste
fuel_emissions = EMISSION_FACTORS[country]["Fuel"] * fuel_consumption
methane_emissions = EMISSION_FACTORS[country]["Methane"] * coal_mined  # Methane emission from coal
explosive_emissions = EMISSION_FACTORS[country]["Explosives"] * explosives

# Convert emissions to tonnes and round off to 2 decimal points
mining_emissions = round(mining_emissions / 1000, 2)
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)
fuel_emissions = round(fuel_emissions / 1000, 2)
methane_emissions = round(methane_emissions / 1000, 2)
explosive_emissions = round(explosive_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    mining_emissions + transportation_emissions + electricity_emissions + waste_emissions +
    fuel_emissions + methane_emissions + explosive_emissions, 2
)

if st.button("Calculate CO2 Emissions"):

    # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"⛏️ Mining: {mining_emissions} tonnes CO2 per year")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")
        st.info(f"🚜 Fuel Consumption: {fuel_emissions} tonnes CO2 per year")
        st.info(f"💥 Explosives: {explosive_emissions} tonnes CO2 per year")
        st.info(f"🌱 Methane: {methane_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        #st.warning("This calculation is based on average emission factors. Actual emissions may vary based on specific mining practices and technologies.")
