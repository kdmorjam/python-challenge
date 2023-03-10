# python-challenge
Python Challenge assignment
This challenge contains two python scripts, PyPoll & PyBank.
For PyBank, main.py reads budget_data.csv in the Resources folder and writes the results
to budget_analysis.txt in the analysis folder and the terminal.
The tasks for this script are broken into four functions.
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
  * printtotal_votes
  * calc_cand_vote
  * calc_vote_percent
  * sort_byname
  * sort_vote_count
  * print_results
  * highest_vote_count

