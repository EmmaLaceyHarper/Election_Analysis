#The data we need to retrieve
#1. Tht total number of votes cast. 
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won. 
#4. The total number of votes each candidate won. 
#5. The winnder of the election based on popular vote. 


import csv
import os
#Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indiret path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Intialize a total vote counter.
total_votes = 0

#Candidate Options
candidate_options=[]

# Declare the empty dictionary. 
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

 ## Determine the percentage of votes for each candidate by looping through the counts. 
 #Iterate through the candidate list. 
for candidate_name in candidate_votes:
   #Retrieve vote counto of candidate. 
   votes = candidate_votes[candidate_name]
   #Calculate the percentage of votes. 
   vote_percentage = float(votes)/float(total_votes)*100

   #Print the candidate name and percenag of votes. 
   print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")

   #Determine winning vote count and candidate
   #Determine if the votes is greater than the winning count. 
   if (votes > winning_count) and (vote_percentage > winning_percentage):
     #If true then set winning_count = votes and winning_percent = 
     #vote_percenage
     winning_count = votes
     winning_percentage = vote_percentage
     #And, set the winning_candidate equal to the candidate's name
     winning_candidate = candidate_name

#Print the winnig candidate, vote count and percentage to terminal
winning_candidate_summary= (f"---------------------\n" f"Winner: {winning_candidate}\n" f"Winning Vote Count: {winning_count:,}\n" f"Winning Percentage: {winning_percentage:.1f}%\n" f"---------------------\n")
print(winning_candidate_summary)





