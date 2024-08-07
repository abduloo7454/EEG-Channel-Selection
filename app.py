import pandas as pd
import streamlit as st

@st.cache
st.set_page_config(page_title="EEG Channel Selection", layout="wide")

BCI_Competition_IV_I_Calib_Subject-a = pd.read_excel("G-EEGCS-Streamlit/IV_I_Calib_Subject-a.xlsx")
BCI_Competition_IV_I_Calib_Subject-b = pd.read_excel("G-EEGCS-Streamlit/IV_I_Calib_Subject-b.xlsx")
BCI_Competition_IV_I_Calib_Subject-f = pd.read_excel("G-EEGCS-Streamlit/IV_I_Calib_Subject-f.xlsx")

BCI_Competition_IV_2a_Subject-1 = pd.read_excel("G-EEGCS-Streamlit/IV_2a_Subject-1.xlsx")
BCI_Competition_IV_2a_Subject-2 = pd.read_excel("G-EEGCS-Streamlit/IV_2a_Subject-2.xlsx")
BCI_Competition_IV_2a_Subject-3 = pd.read_excel("G-EEGCS-Streamlit/IV_2a_Subject-3.xlsx")

BCI_Competition_III_V_Subject-1 = pd.read_excel("G-EEGCS-Streamlit/III_V_Subject-1.xlsx")
BCI_Competition_III_V_Subject-2 = pd.read_excel("G-EEGCS-Streamlit/III_V_Subject-2.xlsx")

BCI_Competition_II_Ia = pd.read_excel("G-EEGCS-Streamlit/II_Ia.xlsx")
BCI_Competition_II_Ib = pd.read_excel("G-EEGCS-Streamlit/II_Ib.xlsx")

# Display the filtered data
st.dataframe(BCI_Competition_III_V_Subject-1)
