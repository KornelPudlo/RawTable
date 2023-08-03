### RUN THE APP in http ' python -m streamlit run C:\Users\kornel.pudlo\PycharmProjects\Developer\RawData_with_filters\main.py '

import streamlit as st
import pandas as pd
import re

# Free Text at the top of the tool
st.title('Raw Data Table')
st.write('Raw Data Table with filters section for internal use only ')

# Read the CSV file into a dataframe
csv_file_path = 'test.csv'
dataframe = pd.read_csv(csv_file_path)


# Function to create age value buckets
def create_age_buckets(age):
    if age < 30:
        return 'Younger than 30'
    elif age > 30:
        return 'Older than 30'
    else:
        return '30 YO'


Age_Buckets = ['All', 'Younger than 30', 'Older than 30', '30 YO']
#selected_age_bucket = st.sidebar.multiselect('Age Bucket', Age_Buckets)



# # Add sidebar filters

teams = dataframe['Team'].unique()
player = dataframe['Player Name'].unique()
position = dataframe['Position'].unique()
date_of_birth = dataframe['Date of birth'].unique()
nationality = dataframe['Nationality'].unique()
market_value = dataframe['Market Value'].unique()
age_bucket = dataframe['Age'].unique()


# teams = dataframe.iloc[:, 0].unique()  # Get unique values from the 1st column ('Team')
# player = dataframe.iloc[:,1].unique()  # Get unique values from the 2nd column ('Player')
# position = dataframe.iloc[:,2].unique() # Get unique values from the 3rd column ('Position')
# date_of_birth = dataframe.iloc[:,3].unique() # Get unique values from the 4th column ('Date of birth') # Jak założyć filtr żeby się filtrowaływ wszystkie wartości???
# nationality = dataframe.iloc[:,5].unique() #Get unique values from the 6th column ('nationality')
# market_value = dataframe.iloc[:,6].unique() # Get unique values from 6th column ('market value')
# Age_bucket = dataframe.iloc[:,4].unique() # Get unique values from 5th column ('Age Bucket')


selected_team = st.sidebar.multiselect('Team Selection', teams) #error przy zmianie na multiselect

if selected_team:
    # Filter the dataframe based on the selected team
    filtered_df = dataframe[dataframe['Team'].isin(selected_team)]

    # get unique positions
    unique_positions = filtered_df['Position'].unique()

else:
    filtered_df = dataframe

selected_position = st.sidebar.multiselect('Position', position)



# selected_player = st.sidebar.multiselect('Player Name', player)
# selected_position = st.sidebar.multiselect('Position', position)
# selected_date_of_birth = st.sidebar.multiselect('date of birth',date_of_birth)
# selected_nationality = st.sidebar.multiselect('Nationality ',nationality)
# seleceted_market_value = st.sidebar.multiselect('Market Value [M€]',market_value) # To create buckets
# Filter the dataframe based on the selected team


# Default value for selected_market_value in case it's not defined in the sidebar
# selected_market_value = []
# selected_age_bucket = st.sidebar.multiselect('Age Bucket', Age_Buckets)
#filtered_df = dataframe[dataframe['Team'] == selected_team] #232 line code in logo tool  - spróbuj zrobic niedynamiczny filtr z apply na samym dole

#Test ############################################################

# Apply all filters to the dataframe
# filtered_df = dataframe[
#     (dataframe['Team'] == selected_team) &
#     (dataframe['Player Name'].isin(selected_player)) &
#     (dataframe['Position'].isin(selected_position)) &
#     (dataframe['Date of birth'].isin(selected_date_of_birth)) &
#     (dataframe['Nationality'].isin(selected_nationality)) &
#     (dataframe['Market Value'].isin(selected_market_value)) &
#     (dataframe['Age'].isin(selected_age_bucket))
# ]


# filtered_df = dataframe[
#     (dataframe['Team'].isin(list(selected_team))) &
#     (dataframe['Player Name'].isin(list(selected_player))) &
#     (dataframe['Position'].isin(list(selected_position))) &
#     (dataframe['Date of birth'].isin(list(selected_date_of_birth))) &
#     (dataframe['Nationality'].isin(list(selected_nationality))) &
#     (dataframe['Market Value'].isin(list(selected_market_value))) &
#     (dataframe['Age'].isin(list(selected_age_bucket)))
# ]

# If no filters are selected, display the original dataframe
# if not (selected_team or selected_player or selected_position or selected_date_of_birth or selected_nationality or selected_market_value or selected_age_bucket):
#     filtered_df = dataframe

# End Test ############################################################


# Apply the age buckets function to the 'Age' column
# filtered_df['Age Bucket'] = filtered_df['Age'].apply(create_age_buckets)


# Display the filtered dataframe
st.write(filtered_df)



#Create sidebar filters

# st.sidebar.write('Filters section')
# unique_team = sorted(test.csv['Team'].unique())
# segment_checkbox = st.sidebar.checkbox('All Teams', help='Check this box to select all segments')



