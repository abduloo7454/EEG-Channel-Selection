import pandas as pd
import altair as alt
import streamlit as st

# Load datasets
data_files = {
    "BCI Competition IV I Subject-a": "k-adaptEEGCS Streamlit/IV_I_Calib_Subject-a.xlsx",
    "BCI Competition IV I Subject-b": "k-adaptEEGCS Streamlit/IV_I_Calib_Subject-b.xlsx",
    "BCI Competition IV I Subject-f": "k-adaptEEGCS Streamlit/IV_I_Calib_Subject-f.xlsx",
    "BCI Competition IV 2a Subject-1": "k-adaptEEGCS Streamlit/IV_2a_Subject-1.xlsx",
    "BCI Competition IV 2a Subject-2": "k-adaptEEGCS Streamlit/IV_2a_Subject-2.xlsx",
    "BCI Competition IV 2a Subject-3": "k-adaptEEGCS Streamlit/IV_2a_Subject-3.xlsx",
    "BCI Competition III V Subject-1": "k-adaptEEGCS Streamlit/IV_3_Subject-1.xlsx",
    "BCI Competition III V Subject-2": "k-adaptEEGCS Streamlit/IV_3_Subject-2.xlsx",
    "BCI Competition II Ia": "k-adaptEEGCS Streamlit/Subject-II_Ia.xlsx",
    "BCI Competition II Ib": "k-adaptEEGCS Streamlit/Subject-II_Ib.xlsx"
}

# Load all dataframes into a dictionary
dfs = {name: pd.read_excel(path) for name, path in data_files.items()}


# Sidebar for dataset selection
dataset_name = st.sidebar.selectbox("Select Dataset", list(data_files.keys()))
df = dfs[dataset_name]

# Set the title dynamically based on the selected dataset
st.title(f"EEG Channel Selection for k-adaptEEGCS Method: {dataset_name}")

# Sidebar for centrality score selection
clusters = st.sidebar.selectbox("Select Centrality Score", df["Different Clusters"].unique())

# Filter dataframe
filtered_df = df[df["Different Clusters"] == clusters]

# Create Altair charts
def create_chart(df, y_value, title):
    return alt.Chart(df).mark_bar().encode(
        alt.X('Similarity Parameter:O'),
        alt.Y(y_value)
    ).properties(title=title)

chart_acc = create_chart(filtered_df, 'Accuracy', 'Accuracy')
chart_f1Score = create_chart(filtered_df, 'f1-Score', 'f1-Score')
chart_kappa = create_chart(filtered_df, 'Kappa', 'Kappa')
chart_Channels = create_chart(filtered_df, '# of Selected Channels', '# of Selected Channels')
chart_Time = create_chart(filtered_df, 'Time', 'Time')

# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Accuracy", "f1-Score", "Kappa", "# of Selected Channels", "Time"])

with tab1:
    st.altair_chart(chart_acc, use_container_width=True)
with tab2:
    st.altair_chart(chart_f1Score, use_container_width=True)
with tab3:
    st.altair_chart(chart_kappa, use_container_width=True)
with tab4:
    st.altair_chart(chart_Channels, use_container_width=True)
with tab5:
    st.altair_chart(chart_Time, use_container_width=True)

# Display the filtered data
st.dataframe(filtered_df)


