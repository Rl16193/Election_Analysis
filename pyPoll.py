#Open Data file in Python
#Count total number of votes
#List all candidates that got a vote
#Count total votes received by each candidate
#Calculate % votes received by each candidate (candidate_votes/total_votes * 100)
#Find winner of polls based on mximum %tage of votes received

# Import modules
import os
import  csv

# Define File Path for the data and store it in a variable
file_load=os.path.join("Resources", "election_results.csv")

# Define the location of the output file
file_save = os.path.join("Analysis", "election_analysis.txt")

# Define variable to count total votes
total_votes = 0

# Define dictionary for candidate_votes
candidate_votes={}

# Define a list to store candidate names
candidate_options = []

winning_count = 0
winning_percent = 0

# Open the file and save it as election_data
with open(file_load) as election_data:
    file_read = csv.reader(election_data)

    # Store the header of the csv file and move to the next iteration
    header = next(file_read)
    print(header)

    for row in file_read:
        
        # Count total votes
        total_votes += 1

        # Store the 1st Candidate name in the list
        candidate_name = row[2]

        # Check if candidate name in the list created, if not add it to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Define the votes of this candidate as zero
            candidate_votes[candidate_name] = 0

        # Add the votes for each candidate
        candidate_votes[candidate_name] += 1

    print (candidate_votes)
    
# Save the Output file and write in it

with open(file_save, 'w') as outputfile:
    result = (f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes = {total_votes}\n"
    f"-------------------------\n")
    outputfile.write(result)

    # for loop to obtain total votes for each candidate
    
    for candidate_name in candidate_votes:
        vote=candidate_votes[candidate_name]

         # Calculate %tage votes for each candidate
        percentvote = float(vote)/float(total_votes) * 100

        if (winning_count<vote) and (winning_percent<percentvote):
            winning_candidate = candidate_name
            winning_percent = percentvote

        # Print the output
        candidate_info = (f"{candidate_name}: {percentvote:.1f}% ({vote})\n")
        outputfile.write(candidate_info)
    
    winning_result=(f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning votes: {candidate_votes[winning_candidate]}\n"
    f"Winning Percent {winning_percent:.1f}%\n"
    f"---------------------------")
    outputfile.write (winning_result)


