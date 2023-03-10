import os
import csv

# The total number of votes cast
def printtotal_votes(filereader,text_f):
    total_votes = 0

    for row in filereader:
        total_votes += 1

     # create print list
    print_lines = ["Election Results","-------------------------","Total Votes: "+str(total_votes),
                   "-------------------------"]

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
                

    cand_vote_list = list(zip(name_list, votecount_list))

    return(cand_vote_list)
    
#-------------------------------------------
#sort candidate list by vote count
#-------------------------------------------
def sort_vote_count(item):
    return(item[1]) 

                  
# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.


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

    #------------------------------------------
    # Convert file to a list
    #------------------------------------------
    election_list = list(csvreader)

    #----------------------------------------------------
    # Get list of candidates and corresponding vote count
    #----------------------------------------------------
    cand_vote_list = calc_cand_vote(election_list)

    #----------------------------------------------------
    # Determine and print winner of election
    #----------------------------------------------------
    highest_vote_count(cand_vote_list)
