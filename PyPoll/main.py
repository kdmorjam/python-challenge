import os
import csv

# The total number of votes cast
def printtotal_votes(filereader,text_f):
    total_votes = 0

    #calculate total number of rows in file
    for row in filereader:
        total_votes += 1

     # create print list
    print_lines = ["Election Results","-------------------------","Total Votes: "+str(total_votes),
                   "-------------------------"]

    #open output file for writing
    with open(text_f, 'w') as newfile:
        #print each row in print list
        for line in print_lines:
            #Newline character added to ensure 'line' is printed on a new line
            #print to terminal
            print('\n'+line)
            #print to text file
            newfile.write('\n'+line)

    return(total_votes)

def calc_cand_vote(election_lst):
     #create average change list
    name_list = []
    votecount_list = []
    index = 2
    vote_counter = 0   #vote counter for candidate

    for counter in range(len(election_lst)):
        vote_counter += 1
        #get difference between current month and next month
        if counter < (len(election_lst)-1):
            cand1 = election_lst[counter] 
            cand2 = election_lst[counter+1]
            
            if cand1[index] != cand2[index]:
                name_list.append(cand1[index])
                votecount_list.append(vote_counter)
                vote_counter = 0
        else:
            #at last row update lists
            cand1 = election_lst[counter]
            name_list.append(cand1[index])
            votecount_list.append(vote_counter)
                
    #----------------------------------------------------
    # Merge name and vote count lists
    #----------------------------------------------------
    cand_vote_list = list(zip(name_list, votecount_list))

    return(cand_vote_list)

#------------------------------------------------------
# calculate voting percentage for each candidate
#------------------------------------------------------
def calc_vote_percent(vote_list, total):
    percent_list = []

    for row in vote_list: 
        candidate_result = row[1]
        #calculate percentage vote
        percent_amt = round(((candidate_result/total) * 100),3)
        #add result to percentage list
        percent_list.append(percent_amt)
        
    #----------------------------------------------
    # Create a list of lists. Add percentage votes to 
    #---------------------------------------------
    final_list = list(zip(vote_list, percent_list))
    
    return(final_list)

#---------------------------------------------------
# Print results for all candidate
#---------------------------------------------------
def print_results(cand_vote_list, text_f):
    
    #open output file to append text)
    with open(text_f, 'a') as newfile:
        for row in cand_vote_list:
            cand_name = str(row[0][0])  #candidate name
            cand_votes = row[0][1]      #candidate votes
            vote_percent = row[1]       #percentage votes

            # create text string to print
            print_line = str(cand_name)+":  "+str(vote_percent)+"% ("+str(cand_votes)+")"
            
            #print output to terminal
            print('\n'+print_line)
            #print to text file
            newfile.write('\n'+print_line)


#-------------------------------------------
#sort candidate list by name
#-------------------------------------------
def sort_byname(item):
    return(item[2]) 

#-------------------------------------------
#sort candidate list by vote count
#-------------------------------------------
def sort_vote_count(item):
    return(item[0][1]) 

#-------------------------------------------
# Determine and print winning candidate
#------------------------------------------
def highest_vote_count(sorted_list,text_f):
    index = len(sorted_list)
    #list is in ascending order of vote count
    #winner would be the last element in list
    winner = sorted_list[index-1]
    #Get name of winner
    winner_name = str(winner[0][0])

     # create print list
    print_lines = ["-------------------------","Winner: " +winner_name,"-------------------------"]

    #print output to terminal and to text file
    #open output file for writing
    with open(text_f, 'a') as newfile:
        #print each row in print list
        for line in print_lines:
            #Newline character added to ensure 'line' is printed on a new line
            #print to terminal
            print('\n'+line)
            #print to text file
            newfile.write('\n'+line)
    


# Path to collect data from the Resources folder
election_data_path = os.path.join("Resources", "election_data.csv")
#Path to write text file to analysis folder
textfile_path = os.path.join("analysis", "election_results.txt")

# Read in the CSV file
with open(election_data_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    header = next(csvreader)

    #-------------------------------------------------
    # calculate & print total number of votes cast 
    # Return total votes to use in further calculations
    #-------------------------------------------------
    total_votes = printtotal_votes(csvreader,textfile_path)

#re-create csvreader,as it no longer exists
with open(election_data_path, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip & store header row
    header = next(csvreader)
    #------------------------------------------
    # Convert file to a list
    #------------------------------------------
    election_list = list(csvreader)

    #----------------------------------------------------
    # Sort list by Candidate name
    #----------------------------------------------------
    sorted_list = sorted(election_list,key=sort_byname)

    #----------------------------------------------------
    # Get list of candidates and corresponding vote count
    #----------------------------------------------------
    cand_vote_list = calc_cand_vote(sorted_list)

    #----------------------------------------------------
    # Calculate percentage of votes for each candidates
    #----------------------------------------------------
    final_vote_list = calc_vote_percent(cand_vote_list,total_votes)

    #------------------------------------------------------
    # Print voting results
    #------------------------------------------------------
    print_results(final_vote_list, textfile_path)

    #--------------------------------------------------------------
    #sort candidate list in ascending order of percentage of votes
    #--------------------------------------------------------------
    sorted_vote_count_list = sorted(final_vote_list, key=sort_vote_count)


    #----------------------------------------------------
    # Determine and print winner of election
    #----------------------------------------------------
    highest_vote_count(sorted_vote_count_list,textfile_path)
