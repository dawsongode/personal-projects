# Get regular season details
weeks = int(input("How many weeks during the regular season did you score high points?(0-14)\n"))

# Define payout values
buy_in = 100
high_points = 10
division_winner = 100
third = 100
second = 200
first = 560
money_won = weeks * high_points
money_lost = buy_in - money_won

# Determine if they made the playoffs or placed
playoffs = str(input("Did you make the playoffs?(yes/no)\n"))

if playoffs == "no":
    print("You won", money_won, "dollars, but lost", money_lost, "dollars")

elif playoffs == "yes":
    division = str(input("Did you win your division?\n"))

    # If they won their division, add $100 to their money won total
    if division == "yes":
        money_won = weeks * high_points + division_winner

    place = str(input("Did you get first, second, or third place?\n"))

    if place == "first":
        money_won = weeks * high_points + first
    if place == "second":
        money_won = weeks * high_points + second
    if place == "third":
        money_won = weeks * high_points + third
    if (money_won - buy_in > 0):
        print("You won", money_won - buy_in, "dollars")
    else:
        print("You won", money_won, "dollars, but lost", money_lost, "dollars")