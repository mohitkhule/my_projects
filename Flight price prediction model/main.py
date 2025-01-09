import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open(r"C:\Users\mohit\streamlit dev\flight_rf.pkl", "rb"))

# Title and Introduction
st.title("Flight Price Prediction")
st.write("Enter the flight details below to predict the price:")

# Sidebar Inputs
with st.sidebar:
    st.header("Flight Details")

 # Date and Time of Journey
    dep_date = st.date_input("Select Departure Date")
    dep_time = st.time_input("Select Departure Time")
    arr_date = st.date_input("Select Arrival Date")
    arr_time = st.time_input("Select Arrival Time")

    try:
        # Extract day, month, and time components
        Journey_day = dep_date.day
        Journey_month = dep_date.month
        Dep_hour = dep_time.hour
        Dep_min = dep_time.minute

        Arrival_hour = arr_time.hour
        Arrival_min = arr_time.minute

        # Calculate duration in hours and minutes
        dep_datetime = pd.Timestamp.combine(dep_date, dep_time)
        arr_datetime = pd.Timestamp.combine(arr_date, arr_time)
        duration = arr_datetime - dep_datetime
        if duration.days < 0:
            st.error("Arrival time cannot be earlier than departure time.")
            st.stop()

        dur_hour = duration.seconds // 3600
        dur_min = (duration.seconds % 3600) // 60
    except ValueError:
        st.error("Invalid date/time input.")
        st.stop()

    # Stops
    Total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])

    # Airline Selection
    airline = st.selectbox("Airline", [
        "Jet Airways", "IndiGo", "Air India", "Multiple carriers", "SpiceJet",
        "Vistara", "GoAir", "Multiple carriers Premium economy", "Jet Airways Business",
        "Vistara Premium economy", "Trujet"
    ])

    # Map airline to one-hot encoding
    airlines_map = {
    "Jet Airways": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "IndiGo": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "Air India": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    "Multiple carriers": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    "SpiceJet": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    "Vistara": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    "GoAir": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    "Multiple carriers Premium economy": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    "Jet Airways Business": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    "Vistara Premium economy": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    "Trujet": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
     }

    airline_encoding = airlines_map.get(airline, [0] * 11)

    # Source and Destination
    Source = st.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai"])
    Destination = st.selectbox("Destination", ["Cochin", "Delhi", "New_Delhi", "Hyderabad", "Kolkata"])

    # Map Source/Destination to one-hot encoding
    source_map = {"Delhi": [1, 0, 0, 0], "Kolkata": [0, 1, 0, 0], "Mumbai": [0, 0, 1, 0], "Chennai": [0, 0, 0, 1]}
    destination_map = {"Cochin": [1, 0, 0, 0, 0], "Delhi": [0, 1, 0, 0, 0], "New_Delhi": [0, 0, 1, 0, 0], "Hyderabad": [0, 0, 0, 1, 0], "Kolkata": [0, 0, 0, 0, 1]}

    source_encoding = source_map.get(Source, [0] * 4)
    destination_encoding = destination_map.get(Destination, [0] * 5)

# Prediction Button
if st.button("Predict Flight Price"):
    # Combine all features
    features = [
        Total_stops,
        Journey_day,
        Journey_month,
        Dep_hour,
        Dep_min,
        Arrival_hour,
        Arrival_min,
        dur_hour,
        dur_min,
        *airline_encoding,
        *source_encoding,
        *destination_encoding
    ]

    # Predict
    prediction = model.predict([features])
    output = round(prediction[0], 2)

    st.success(f"Your Flight price is Rs. {output}")
