# Add our dependencies. 
import csv
import os
#Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indiret path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1. Intialize a total vote counter.
total_votes = 0
#Candidate Options and Candidate Votes.
candidate_options=[]
candidate_votes = {}
#Winning Candidate and Winning Count Tracker
winning_candidate= ""
winning_count= 0
winning_percentage = 0
#open the election results and read the file. (using with allows you to not have to close.)
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file. 
    for row in file_reader: 
        #2. Add to the total vote count.
        total_votes += 1
        #Print the candidate name for each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
              #Add it to the lit of candidates. 
              candidate_options.append(candidate_name)
              #Begin tracking the candidate's votes (adds candidate names to the dictionary as the keys.)
              candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    #Iterate through the candidate list. 
    for candidate_name in candidate_votes:
        #Retrieve vote counto of candidate. 
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes. 
        vote_percentage = float(votes)/float(total_votes)*100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Print the candidate name and percenag of votes. 
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = 
            #vote_percenage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    #And, set the winning_candidate equal to the candidate's name
    winning_candidate_summary =  (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)         





