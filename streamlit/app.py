import streamlit as st
import numpy as np
import pandas as pd

# Write title 
st.title("Balaji PG 102")

# Write text
st.write("We have 3 beds, 2 tables, 3 chairs, 1 large bathroom, 1 TV and many cupboards")

# Print a DataFrame
df = pd.DataFrame({"name": ["Vinayak", "Umesh", "Guddu", "Sohel"], 
                   "age": [23, 24, 25, 31]})

st.write(df)

#Create a line chart
chart = pd.DataFrame(np.random.randint(1, 100, (10, 4)), columns=["A", "B", "C", "D"])
st.line_chart(chart)