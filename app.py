import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title
st.set_page_config(page_title="CSV Insights App")

# Title
st.title("📊 CSV Insights Application")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Show the first few rows
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Show summary statistics
    st.write("### Data Summary")
    st.write(df.describe())

    # Visualization
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    
    if numeric_columns:
        st.write("### Data Visualization")
        selected_column = st.selectbox("Select a column for Histogram", numeric_columns)
        fig, ax = plt.subplots()
        sns.histplot(df[selected_column], kde=True, ax=ax)
        st.pyplot(fig)

        # Correlation Heatmap
        st.write("### Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
else:
    st.info("Please upload a CSV file to proceed.")
