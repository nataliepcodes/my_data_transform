# my_data_transform
Data processing exercise from Qwasar, Software Engeering program - Season 1 Arc 2.

## Specification
* Given a dataset of sales from My Online Coffee Shop, identify customers who are more likely to buy coffee online.
* Dataset is in CSV format.
* CSV has 3 columns: Email - Age - Order At.
* Group Email column by Email provider.
* Group Age column by the following categories: [1->20] - [21->40] - [41->65] - [66->99]
* Group Order At column by the following categories: [morning => 06:00am -> 11:59am] - [afternoon => 12:00pm -> 5:59pm] - [evening => 6:00pm -> 11:59pm]
* Create a function hat will replace the value in each of these columns with the correct actionable data. For example: if time is "2020-03-05 15:19:48", replace if by "afternoon"
* Input is a string which contains data in CSV format.
* Function returns an array of strings in CSV format with the columns Email, Age and Order At transformed.
* Prototype function: def my_data_transform(csv_content).
