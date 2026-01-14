#W2 - Text File Handling Demo

#Step 1: import the csv (comma separated values) library
import csv

total_records = 0 #holds total number of records in file 

#Step 2: connect to the file
#--connected to file -----------------------------------
#include relative file path in open() - make sure to switch \ to /
with open("simple.csv") as csvfile:
    #make sure to indent inside of code block!
  
    #allow the csv reader to access and read the file 
    file = csv.reader(csvfile)
    #file = entries date from file! organized as records 

    #step 3 : process throuugh every record (row) in the file
    for record in file:
        #add to total records count
        total_records += 1

        #display data to user
        #print(record) #entire record/row data as a list 

        name = record[0]
        number = record[1]
        color = record[2]

        print(f"{name} 's number is {number} and their favorite color is {color}.")
    



#--disconnect from the file --------------------------------
print("----------------------------------------------")
print(f"\nTotal Records Processed: {total_records}\n")