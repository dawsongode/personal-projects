def no_playoff(a, b):
    return a * b


def no_division(a, b, c):
    return a * b + c


def division_place(a, b, c, d):
    return a * b + c + d


def no_division_place(a, b, c):
    return a * b + c


weeks = int(input("How many weeks during the regular season did you score high points?(0-14)\n"))
playoffs = str(input("Did you make the playoffs?(yes/no)\n"))

buy_in = 100
high_points = 10
division_win = 100
third = 100
second = 200
first = 560

if playoffs == "no":
    payout = no_playoff(weeks, high_points)
    print("You won/lost", payout - buy_in, "dollars")

elif playoffs == "yes":
    division = str(input("Did you win your division?\n"))
    place = (input("Did you get first, second, or third place?\n"))
    if division == "yes":
        if place == "third":
            payout = division_place(weeks, high_points, division_win, third)
        if place == "second":
            payout = division_place(weeks, high_points, division_win, second)
        if place == "first":
            payout = division_place(weeks, high_points, division_win, first)
        else:
            payout = no_division_place(weeks, high_points, division_win)
        print("You won/lost", payout - buy_in, "dollars")

    if division == "no":
        if place == "third":
            payout = no_division_place(weeks, high_points, third)
        if place == "second":
            payout = no_division_place(weeks, high_points, second)
        if place == "first":
            payout = no_division_place(weeks, high_points, first)
        else:
            payout = no_playoff(weeks, high_points)
            money_lost = buy_in - payout
        print("You won/lost", payout - buy_in, "dollars")
        print("You won/lost", payout - buy_in, "dollars")