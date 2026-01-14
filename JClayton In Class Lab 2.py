#W2 In Class Lab 2

#Program Prompt: The csv file classLab2.csv contains a list of rooms, the maximum number of people that the room 
#Can accommodate, and the number of people currently registered for the event. Write a program that
#Displays all rooms that are over the maximum limit of people and the number of people that have to
#Be notified that they will have to be put on the wait list. After the file is completely processed the
#Program should display the number of records processed and the number of rooms that are over the limit

#Variable Dictionary:


#--Import------------------------------------
import csv
#--Functions---------------------------------
def difference(people, max_cap) :
    diff = max_cap - people
    return diff
#--Main--------------------------------------

#initialize known or needed values (counting variables)
total_records = 0
rooms_over = 0


print (f"\n\n{'Room Name':20}   {'Max':5}   {'PPL':5}   {'! Remove !':5}")
print ("-" * 50)
with open ("classLab2.csv") as csvfile :
    #Read Text File Data Into 'File'
    file = csv.reader(csvfile)
    #Process each 'Record' in 'File'
    for record in file:
        total_records += 1

        #Assign Each Field to a Variable
        name = record[0]
        max = int(record[1])
        ppl = int(record[2])

        #Call The Differnce () to Find People Over/Under Capacity
        remaining = difference(ppl, max)

        if remaining < 0 :
            rooms_over += 1
            print (f"Room: {name:20} {max:5} {ppl:5} {-remaining :5}")
print ("-" * 50)
#Disconncet From File 

#Display final values: Totals rooms counted, Number of rooms over capacity
print(f"\n\nrooms over capacity: {rooms_over} \nTotal rooms counted: {total_records}")