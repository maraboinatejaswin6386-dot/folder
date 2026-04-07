
# Comphrensive guide on pandas libary


The pandas library in python provides powerful tools for conducting EDA efficiently.

It provides the data structures like one dimenstional (series) and two dimenstional (Dataframe) to handle dta  efficiently
By using pandas library,we can clean, manipulate data as per the business requirements.

Most widly used functions are:

head()

tail()

transform()

merge()

join()

describe()

info()

isnull()

columns() 


![IMAGE](https://github.com/user-attachments/assets/72da955-1618-4c60-912c-02cb94b534b4)



we have to install pandas library using  pip install pandas command as shown in the above.



import pandas as  pd 
It means we are loading the pandas library and call it "pd"
"https://github.com/user-attachments/assets/a13bf928-6cac-443f-9e4b-cd5dbfe421ac" 


Using pandas we can read the csv file.
read_csv() function helps us to read from csv file.
"https://github.com/user-attachments/assets/e8537397-3fc4-4d4d-8a72-701e7be694f7" 



The df.info() method provides a concise summary of a pandas Dataframe,including.

✔️Number of entries (rows)

✔️Column names

✔️Non-null values (missing data check)

✔️Data types of each column (int, float, object, etc.)

✔️Memory usage.

"https://github.com/user-attachments/assets/30a63b38-e4fc-4c78-aafa-a76d370be15b" 


The df.describe() 

✔️count → number of non-null values

✔️mean → average value

✔️std → standard deviation (spread of data)

✔️min → smallest value

✔️25% → first quartile

✔️50% (median) → middle value

✔️75% → third quartile

✔️max → largest value

"https://github.com/user-attachments/assets/4b8add3f-21c0-4687-806e-a54bd8ebc6c7" 


df.columns

columns is an attribute in pandas that shows the names of all columns in your dataset

Know all variables in dataset
Fix column names
Avoid spelling mistakes in coding

"https://github.com/user-attachments/assets/11c6fc3d-74a2-46b6-8b4b-401a415e9b30" 


df.isnull()

isnull() is used to check missing values (NaN) in your dataset

True → value is missing
False → value is present

Detect missing data
Decide whether to:
Fill values (fillna())
Drop rows (dropna())

"https://github.com/user-attachments/assets/ae6a1cfe-d4b4-4292-a971-37a85384b346" 


merge()

merge() is used to combine two DataFrames based on one or more common columns.

Works on columns (not index)
More flexible than join()
Default = inner join

"https://github.com/user-attachments/assets/ba164541-e0c8-4b56-b4e8-d49a9caf129d" 

 
dataframe1.join(dataframe2.set_index('ID),on='ID)

Match df1['ID']
With df2 index

join = index based combine

"https://github.com/user-attachments/assets/94338db4-f857-4b9c-b4bb-ed7ab70ee90b" 

df.tail()

tail() is used to view the last few rows of a dataset.


Check end of dataset
Verify data loading
Inspect recent records

![Logo] "https://github.com/user-attachments/assets/787e8dc9-d2f5-44e7-abe4-1c78b899dd0e" >



![Logo ] <img width="1104" height="258" alt=!["Image"] src=    "https://github.com/user-attachments/assets/a7d44807-5364-4a9e-8a1e-8ccb281c54a6"  