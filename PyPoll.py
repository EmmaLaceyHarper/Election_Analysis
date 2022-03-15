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

#open the election results and read the file. (using with allows you to not have to close.)
with open(file_to_load) as election_data:

  #Read the file object with the reader function.
  file_reader = csv.reader(election_data)

  #Read and print the header row
  headers = next(file_reader)
  print(headers)


