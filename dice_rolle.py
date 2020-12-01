import random


def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 1
    while rounds != 4:
        print("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 Roll: " + str(player1))
        print("Player 2 Roll: " + str(player2))

        if player1 == player2:
            print("Draw!")
        elif player1 > player2:
            player1wins += 1
            print("Player 1 Wins Round: " + str(rounds))
        else:
            player2wins += 1
            print("Player 2 Wins Round: " + str(rounds), "\n")
        rounds += 1
    print("*" * 50, "\n Final Results")
    print("*" * 50)

    if player1wins == player2wins:
        print("Draw!")
    elif player1wins > player2wins:
        print("Player 1 Wins - Rounds Won! " + str(player1wins))
    else:
        print("Player 2  Wins - Rounds Won! " + str(player2wins))


def dice_roll():
    """
    Random select for dice
    :return:
    """
    diceRoll = random.randint(1, 6)
    return diceRoll


main()
