import os
import csv



#---------------------------------------------------------------------------
#Print total number of months and total profit/losses for the period
#---------------------------------------------------------------------------
def printtotals(filereader,text_f):
    #Initialize total amounts
    total_months = 0
    total_profitloss = 0

    # Loop through the data to calculate totals
    for row in filereader:
        total_months += 1
        total_profitloss += int(row[1])
        
    # create print list
    print_lines = ["Financial Analysis","----------------------------","Total Months: "+str(total_months),
                   "Total: $"+str(total_profitloss)]

    #print output to terminal and to text file
    #open output file for writing
    with open(text_f, 'w') as newfile:
        #print each row in print list
        for line in print_lines:
            #Newline character added to ensure 'line' is printed on a new line
            #print to terminal
            print('\n'+line)
            #print to text file
            newfile.write('\n'+line)

#Sort budget list by date
def sort_by_date(item):
    #sort_date = item[0]
    return(item[0])

#sort budget list by profit/losses amount
def sort_by_profitloss(item):
    #sort_change = item[1]
    return(item[1]) 


#---------------------------------------------------------------------------
#determine change over the year and the average
#---------------------------------------------------------------------------
def avg_year_change(budget_list,text_f):
    #create average change list
    monthly_change_list = []
    index = 1
    #counter = 1

    for counter in range(len(budget_list)):
        #get difference between current month and next month
        if counter < (len(budget_list)-1):
            month1 = budget_list[counter] 
            month2 = budget_list[counter+1]
            diff = int(month2[index]) - int(month1[index])
            #add difference to average change list
            monthly_change_list.append(diff)

    #get total change
    change = 0
    for x in range(len(monthly_change_list)):
        change += monthly_change_list[x]
    #calculate average change
    avg_change = round(change/len(monthly_change_list),2)
    
    
    #print output to terminal and to text file
    #open output file for writing (appending)
    with open(text_f, 'a') as outputfile:
        #print to terminal
        print(f"\nAverage Change: ${avg_change}")
        #print to text file
        outputfile.write('\n'+"Average Change: $"+str(avg_change))


#---------------------------------------------------------------------------
#Determine greatest increase and decrease and print t terminal and text file
#---------------------------------------------------------------------------
def greatest_least(budget_lst,text_f):
    #greatest decrease
    first_row = budget_lst[0]
    #greatest increase
    last_row = budget_lst[len(budget_lst)-1]

    # create print list
    print_lines = ["Greatest Increase in Profits: "+str(last_row[0])+" ($"+str(last_row[1])+")",
                   "Greatest Decrease in Profits: "+str(first_row[0])+" ($"+str(first_row[1])+")"]
     
    #print output to terminal and to text file
    #open output file for writing (appending)
    with open(text_f, 'a') as outputfile:
        #print each row in print list
        for line in print_lines:
            #print to terminal
            print('\n'+line)
            #print to text file
            outputfile.write('\n'+line)






# Path to collect data from the Resources folder
budget_data_path = os.path.join("Resources", "budget_data.csv")
#Path to write text file to analysis folder
textfile_path = os.path.join("analysis", "budget_analysis.txt")

# Read in the CSV file
with open(budget_data_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    header = next(csvreader)

    #create list from csv file - this changes csvreader
    #budget_list = list(csvreader)

    #print(budget_list)
    # print total number of months in dataset and 
    # net total amount of "Profit/Losses" over the period
    printtotals(csvreader,textfile_path)

#re-initialize csvreader
with open(budget_data_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    header = next(csvreader)

    #convert csv to a list - this changes csvreader
    budget_list = list(csvreader)
    

    #sort list by date
    #sorted_budget_list = sorted(budget_list, key=sort_by_date)
    avg_year_change(budget_list,textfile_path)
    # print(f"Sorted list '\n'")
    # for row in csvreader:
    #     print(row)
    # print('\n') 

    #sort list in ascending order of profit/losses
    sorted_budget_list = sorted(budget_list, key=sort_by_profitloss)
    #print(sorted_budget_list)
    greatest_least(sorted_budget_list,textfile_path)







# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period
