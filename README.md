# Election_Analysis
Use VS Code to write a code on python to determine the largest county and the winner of the election.

## Overview

The purpose of this analysis is to write a code which can read the date presented in CSV fromat to generate the results of the election. This will allow for to create prediction models with further analysis.

## Election Audit Results

- Total Votes: **369711 votes**

![image](https://user-images.githubusercontent.com/100053788/159828723-ccd730b3-2fdf-49d0-81bf-baf84f06983e.png)

- Votes for each County
  - Jefferson:  38855 Votes, 10.5% of the total county votes
  - Denver:     **306055 Votes, 82.8% of the total county votes**
  - Arapahoe:   24801 Votes, 6.7% of the total county votes

![image](https://user-images.githubusercontent.com/100053788/159826443-60768e3d-a288-4c09-8b9e-e03be7653f09.png)


- Largest County: **Denver**

- Votes for each Candidate
  - Charles Casper Stockham:  85213 votes, 23.0% of the total votes
  - Diana Degette:            **272892 votes, 73.8% of the total votes**
  - Raymond Anthony Doane:    11606 votes, 3.1% of the total votes

![image](https://user-images.githubusercontent.com/100053788/159826398-9fde92d8-28c5-469d-a01f-91a3458d67a5.png)


- Winning Candidate: **Diana Degette achieving 272892, 73.8% of the total votes**

![image](https://user-images.githubusercontent.com/100053788/159826102-9a278dae-fe7e-4f34-8e5f-b3c32a6e2b6e.png)

## Election Audit Sumaary

1. The code is good for state wide elections. For nation wide elections we will have to run another for loop to go from one state to the next to calculate the votes for each congressional party and save the results for each state in another dictonary.

2. We can also implement the Pandas library and use dataframes groupby() function to group the voting counts by states and quickly calculate the results using the count or the describe function.
