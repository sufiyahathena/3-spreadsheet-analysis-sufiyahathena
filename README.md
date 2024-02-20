# Data Analysis Report

## Dataset Details

### Origin: 
The dataset used for this analysis was obtained from (https://data.cityofnewyork.us/City-Government/Film-Permits/tg4x-b46p/about_data).
It contains information about film permits issued in New York City.

### Format: 
The original data file was in CSV format.

## Sample of Raw Data
Here is a sample of the raw data from the original CSV file:
![image](https://github.com/sufiyahathena/3-spreadsheet-analysis-sufiyahathena/assets/69389276/932c4829-cd71-41c2-94ef-e439f265c38f)


## Data Scrubbing
1. Removed unnecessary columns such as 'EnteredOn', 'EventAgency', 'ParkingHeld', 'Country'.
2. Converted date and time columns to datetime objects.
3. Calculated event duration by subtracting StartDateTime from EndDateTime.
4. Saved the cleaned dataset to a new CSV file.

Here is a sample of the data from the cleaned CSV file:
![image](https://github.com/sufiyahathena/3-spreadsheet-analysis-sufiyahathena/assets/69389276/b1d7d57b-2f7c-4fb3-9c83-f83c1cdf36d5)

### Links to data files:

Original raw data 
Cleaned data
Spreadsheet file

## Analysis

### Aggregate Statistics
Maximum Event Duration: The longest event duration observed was 852 hours.
Minimum Event Duration: The shortest event duration observed was 1 hours.
Average Event Duration: The average event duration across all permits was 23.61842331 hours.

## Pivot Table Analysis
Here is a sample of the results from the pivot table:

Row Labels	Sum of EventDuration in Hours	Sum of Mean Event Duration
![image](https://github.com/sufiyahathena/3-spreadsheet-analysis-sufiyahathena/assets/69389276/432614e6-47eb-4829-98e8-9e416d228c7b)

The pivot table shows the average event duration for different event types and boroughs. It helps identify trends in event durations across different locations and permit types.

