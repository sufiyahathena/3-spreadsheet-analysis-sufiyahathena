# place your code to clean up the data file below.


import pandas as pd

# Load the dataset into a pandas DataFrame
file_path = '/Users/sufiyahathena/Desktop/3-spreadsheet-analysis-sufiyahathena-main/data/Film_Permits_20240218.csv'  
data = pd.read_csv(file_path)

print("Number of rows in the original data:", data.shape[0])
print()

# Display the first few rows of the dataset to understand its structure
print("Original Data:")
print(data.head())

# Drop unnecessary columns
columns_to_drop = ['EnteredOn', 'EventAgency', 'ParkingHeld', 'Country']  
data.drop(columns=columns_to_drop, inplace=True)

# Remove excessive empty rows
data.dropna(axis=0, how='all', inplace=True)


# Add a computed column for event duration
data['StartDateTime'] = pd.to_datetime(data['StartDateTime'])  # Convert to datetime object
data['EndDateTime'] = pd.to_datetime(data['EndDateTime'])  # Convert to datetime object
data['EventDuration'] = data['EndDateTime'] - data['StartDateTime']  # Compute duration
# Convert timedelta to hours
data['EventDuration'] = data['EventDuration'].dt.total_seconds() / 3600

# Create a mapping dictionary to assign unique numbers to each event type
event_type_mapping = {event_type: index for index, event_type in enumerate(data['EventType'].unique())}

# Add a new column with the encoded numbers based on the mapping dictionary
data['EncodedEventType'] = data['EventType'].map(event_type_mapping)

# Print the mapping dictionary
print("Event Type Mapping Dictionary:")
for event_type, encoded_number in event_type_mapping.items():
    print(f"Event Type: {event_type} --> Encoded Number: {encoded_number}")


# Display the modified DataFrame
print("\nModified Data:")
print(data.head())

print()
# Print the number of rows in the modified data
print("Number of rows in the modified data:", data.shape[0])

# Save the cleaned dataset to a new CSV file
cleaned_file_path = 'cleaned_data.csv'  # Define the path for the cleaned CSV file
data.to_csv(cleaned_file_path, index=False)

print("\nData cleaned and saved to:", cleaned_file_path)