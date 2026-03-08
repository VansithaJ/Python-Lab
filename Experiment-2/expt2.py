Aim:
The aim is to classify a cricket player's performance level (Excellent, Good, Average, or Poor) across batting, bowling, and fielding using conditional logic based on specific match statistics.

Algorithm:
Step1: Start
Step2: Initialize: Get inputs for Runs, Balls, Wickets, Economy, Overs, RunsConceded, and Catches.
Step3: Batting: Calculate SR = (Runs / Balls) * 100.
                   Assign "Excellent", "Good", "Avg", or "Poor" based on (Runs, SR) thresholds.
Step4: Bowling: Calculate Economy Rate: ER = RunsConceded/Overs.
                   Assign "Excellent", "Good", "Avg", or "Poor" based on (Wickets, Economy) thresholds.
Step5: Fielding: If Catches >= 2 ->"Outstanding"; if 1 -> "Active"; else "Needs Improvement".
Step6: All-Rounder Check: If both Batting and Bowling are at least "Excellent", output "Star All-Rounder".Else If both Batting and Bowling are at least "Good", output "Strong All-Rounder".
Step7: Stop

Source code:
# Input Section
Runs = int(input("Enter the runs: "))
Balls = int(input("Enter the balls: "))
Wicket = int(input("Enter the wickets: "))
Economy = int(input("Enter the Economy: "))
Overs = int(input("Enter the no of overs: "))
RunsConceded = int(input("Enter the runs conceded: "))
Catches = int(input("Enter the Catches: "))

# Batting Logic
SR = (Runs / Balls) * 100
if Runs >= 50 and SR >= 120:
    batter = "Excellent"
    print("Excellent Batter")
elif Runs >= 30 and SR >= 100:
    batter = "Good"
    print("Good Batter")
elif Runs >= 20:
    batter = "Avg"
    print("Avg Batter")
else:
    batter = "Poor"
    print("Poor Batter")

# Bowling Logic
ER = RunsConceded / Overs
if Wicket >= 3 and Economy <= 6:
    bowler = "Excellent"
    print("Excellent Bowler")
elif Wicket >= 2 and Economy <= 8:
    bowler = "Good"
    print("Good Bowler")
elif Wicket >= 1:
    bowler = "Avg"
    print("Avg Bowler")
else:
    bowler = "Poor"
    print("Poor Bowler")

# Fielding Logic
if Catches >= 2:
    print("Outstanding Fielder")
elif Catches == 1:
    print("Active Fielder")
else:
    print("Needs Improvement")

# All-Rounder Logic (from second image)
if batter == "Excellent" and bowler == "Excellent":
    print("Star All-Rounder")
elif batter == "Good" and bowler == "Good":
    print("Strong All-Rounder")
else:
    print("Needs Improvement")
