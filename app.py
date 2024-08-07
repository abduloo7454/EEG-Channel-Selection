import pandas as pd
import streamlit as st

@st.cache
st.title("EEG Channel Selection for BCI Competition Dataset")
st.set_page_config(page_title="EEG Channel Selection", layout="wide")

df1 = pd.read_excel("G-EEGCS-Streamlit/III_V_Subject-1.xlsx")

# Display the filtered data
st.dataframe(df1)
