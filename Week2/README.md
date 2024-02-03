# Week 2 Homework
## Question:
### Question 1. Data Loading
### Once the dataset is loaded, what's the shape of the data?
- **266,855 rows x 20 cols**
### Question 2. Data Transformation
### Upon filtering the dataset where the passenger count is greater than 0 and the trip distance is greater than zero, how many rows are left?
-  **257,400 rows**
### Question 3. Data Transformation
### Which of the following creates a new column lpep_pickup_date by converting lpep_pickup_datetime to a date?
- **data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date**
### Question 4. Data Transformation
### What are the existing values of VendorID in the dataset?
- **1 or 2**
### uestion 5. Data Transformation
### How many columns need to be renamed to snake case?
- **4**
### Question 6. Data Exporting
### Once exported, how many partitions (folders) are present in Google Cloud?
- **96**
