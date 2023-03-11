# python-challenge
# Python Challenge assignment
This challenge contains two python scripts, PyPoll & PyBank.
For PyBank, main.py reads budget_data.csv in the Resources folder and writes the results
to budget_analysis.txt in the analysis folder and the terminal.
The tasks for this script are broken into four functions:
  * printtotals function determines and prints theh total number of months in the csv file and 
    the total profil/losses over te entire period.
    
  * avg_year_change determines the change in profit/loss from month to month and the associated month. 
    This is put into a list and returned by this function.The average of these monthly changes is calculated 
    and printed to the budget_analysis.txt file and the terminal.
    
  * sort_by_profitloss returns the key (profit/loss) to the Python sorted() function. The sorted() function 
    is used on the list returned by the avg_year_change function.
    
  * greatest_least determines the greatest and least monthly change from the sorted list and prints the results
    to the budget_analysis.txt file and the terminal.
    
    
    
In PyPoll, main.py reads election_data.csv in the Resources folder and writes the results 
to election_results.txt in the analysis folder and the terminal.
The tasks for this script are broken into seven functions.
  * printtotal_votes determines the total votes cast and prints to election_results.txt and the terminal.
  
  * calc_cand_vote calculates the total votes for each candidates and return the candidate/vote pairs in a list.
  
  * calc_vote_percent caclulates each candidate's vote percentage and returns a list of lists containing candidate
    name, vote count and precentage votes.
    
  * sort_byname returns the key (candidate name) to the Python sorted() function. The sorted() function 
    is used on the election list created by the Python list() function.
    
  * sort_vote_count returns the key (total candidate vote count) to the Python sorted() function. The sorted() function 
    is used on the list returned by the calc_vote_percent function.
    
  * print_results prints results for each candidate to the election_results.txt file and the terminal
  
  * highest_vote_count determines and prints the winner of the election from a sorted list

