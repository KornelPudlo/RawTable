import streamlit as st
import pandas as pd


# Free Text at the top of the tool
st.title('Raw Data Table')
st.write('Raw Data Table with filters section for internal use only  ')

# Read the CSV file into a dataframe
csv_file_path = 'test_file.csv'
dataframe = pd.read_csv(csv_file_path)



st.dataframe(dataframe)
