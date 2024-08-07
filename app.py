import pandas as pd
import streamlit as st

st.title("EEG Channel Selection for BCI competition Dataset")
# st.set_page_config(page_title="EEG Channel Selection", layout="wide")

df1 = pd.read_excel("G-EEGCS-Streamlit/IV_I_Calib_Subject-a.xlsx")
df2 = pd.read_excel("G-EEGCS-Streamlit/IV_I_Calib_Subject-b.xlsx")
df3 = pd.read_excel("G-EEGCS-Streamlit/IV_I_Calib_Subject-f.xlsx")

df4 = pd.read_excel("G-EEGCS-Streamlit/IV_2a_Subject-1.xlsx")
df5 = pd.read_excel("G-EEGCS-Streamlit/IV_2a_Subject-2.xlsx")
df6 = pd.read_excel("G-EEGCS-Streamlit/IV_2a_Subject-3.xlsx")

df7 = pd.read_excel("G-EEGCS-Streamlit/III_V_Subject-1.xlsx")
df8 = pd.read_excel("G-EEGCS-Streamlit/III_V_Subject-2.xlsx")

df9 = pd.read_excel("G-EEGCS-Streamlit/II_Ia.xlsx")
df10 = pd.read_excel("G-EEGCS-Streamlit/II_Ib.xlsx")

# Display the filtered data
st.dataframe(df1)
