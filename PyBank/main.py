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


#-------------------------------------------
#sort budget list by profit/losses amount
#-------------------------------------------
def sort_by_profitloss(item):
    return(item[1]) 


#---------------------------------------------------------------------------
#determine change over the year and the average. Return list with each monthly change 
#---------------------------------------------------------------------------
def avg_year_change(budget_list,text_f):
    #create average change list
    monthly_change_list = []
    date_change_list = []
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
            #add associated date to date_change_list 
            date_change_list.append(month2[index-1])

    #Create list by merging monthly change with associated date
    combined_list = list(zip(date_change_list, monthly_change_list))


    #get total change
    total_change = 0
    for x in range(len(monthly_change_list)):
        total_change += monthly_change_list[x]
    #calculate average change
    avg_change = round(total_change/len(monthly_change_list),2)
    
    #--------------------------------------------
    #print output to terminal and to text file
    #--------------------------------------------

    #open output file for writing (appending)
    with open(text_f, 'a') as outputfile:
        #print to terminal
        print(f"\nAverage Change: ${avg_change}")
        #print to text file
        outputfile.write('\n'+"Average Change: $"+str(avg_change))


    #return list of dates and associated monthly change
    return(combined_list)


#---------------------------------------------------------------------------
#Determine greatest increase and decrease and print to terminal and text file
#List is already sorted by profit/losses
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

    # print total number of months in dataset and 
    # net total amount of "Profit/Losses" over the period
    printtotals(csvreader,textfile_path)

#re-create csvreader,as it no longer exists
with open(budget_data_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    header = next(csvreader)

    #convert csv to a list
    budget_list = list(csvreader)
    

    #determine monthly change and associated date. Return these as a list.
    #Print average change based on calculated monthly change
    new_budget_list = avg_year_change(budget_list,textfile_path)
     

    #sort monthly change list in ascending order of profit/losses
    sorted_budget_change_list = sorted(new_budget_list, key=sort_by_profitloss)

    #determine greatest and least monthly change and print
    greatest_least(sorted_budget_change_list,textfile_path)







# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period
