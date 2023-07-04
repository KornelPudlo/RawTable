###OLD CODE 
import streamlit as st
import pandas as pd


# Free Text at the top of the tool
st.title('Raw Data Table')
st.write('Raw Data Table with filters section for internal use only  ')

# Read the CSV file into a dataframe
csv_file_path = 'test_file.csv'
dataframe = pd.read_csv(csv_file_path)



st.dataframe(dataframe)


###NEW CODE

import streamlit as st
import pandas as pd
import re
# Free Text at the top of the tool
st.title('Raw Data Table')
st.write('Raw Data Table with filters section for internal use only  ')

# Read the CSV file into a dataframe
csv_file_path = 'test.csv'
dataframe = pd.read_csv(csv_file_path)

#st.write(dataframe)

#Age buckets - error przy age buckets

# df['Age'] = df['Column4'].apply(lambda x: re.findall(r'\((\d+)\)', x)[0] if re.findall(r'\((\d+)\)', x) else None)
#
# def create_age_bucket(age):
#     if age is not None:
#         age = int(age)
#         if age <= 18:
#             return '<18'
#         elif 19 <= age <= 23:
#             return '19-23'
#         elif 24 <= age <= 28:
#             return '24-28'
#         else:
#             return '28+'
#     else:
#         return None
#
# df['Age Bucket'] = df['Age'].apply(create_age_bucket)
#
# selected_bucket = st.sidebar.selectbox('Select Age Bucket', ['<18', '19-23', '24-28', '28+'])
# filtered_df = df[df['Age Bucket'] == selected_bucket]
#
#
# # Add sidebar filter for Team Selection
teams = dataframe.iloc[:, 0].unique()  # Get unique values from the 1st column ('Team')
player = dataframe.iloc[:,1].unique()  # Get unique values from the 2nd column ('Player')
position = dataframe.iloc[:,2].unique() # Get unique values from the 3rd column ('Position')
date_of_birth = dataframe.iloc[:,3].unique() # Get unique values from the 4th column ('Date of birth') # Jak założyć filtr żeby się filtrowaływ wszystkie wartości???
nationality = dataframe.iloc[:,4].unique() #Get unique values from the 5th column ('nationality')
market_value = dataframe.iloc[:,5].unique() # Get unique values from 6th column ('market value')



selected_team = st.sidebar.selectbox('Team Selection', teams) #error przy zmianie na multiselect
selected_player = st.sidebar.multiselect('Player Name', player)
selected_position = st.sidebar.multiselect('Position', position)
selected_date_of_birth = st.sidebar.multiselect('Date of birth',date_of_birth)
selected_nationality = st.sidebar.multiselect('Nationality ',nationality)
seleceted_market_value = st.sidebar.multiselect('Market Value [M€]',market_value) # To create buckets
# Filter the dataframe based on the selected team
filtered_df = dataframe[dataframe['Team'] == selected_team]
#filtered_df = dataframe[dataframe['Player']== selected_player]

# Display the filtered dataframe
st.write(filtered_df)


#Create sidebar filters

# st.sidebar.write('Filters section')
# unique_team = sorted(test.csv['Team'].unique())
# segment_checkbox = st.sidebar.checkbox('All Teams', help='Check this box to select all segments')

