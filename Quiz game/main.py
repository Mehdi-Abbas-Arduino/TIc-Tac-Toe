# A Quiz Game
'''
Ask 10 Qs
2 People
adding a score
no time limit
'''
def ask_questions(player):
    score = 0
    
    q1 = input(f"Player {player}, Q1: What's your name? A.Mark, B.Mehdi, C.Naqi: ").upper()
    if q1 == 'B':
        score += 1

    q2 = input(f"Player {player}, Q2: What's your age? A.15, B.16, C.17: ").upper()
    if q2 == 'B':
        score += 1

    q3 = input(f"Player {player}, Q3: What is your favorite subject? A.Computer, B.Maths: ").upper()
    if q3 == 'A':
        score += 1

    q4 = input(f"Player {player}, Q4: What is a Magnetic Material? A.Steel, B.Iron: ").upper()
    if q4 == 'A':
        score += 1
    
    return score

if __name__ == "__main__":
    print("Welcome to the Quiz Game")
    
    print("Turn of player 1")
    score1 = ask_questions(1)
    
    print("Turn of player 2")
    score2 = ask_questions(2)
    
    if score1 > score2:
        print("Player 1 wins")
    elif score2 > score1:
        print("Player 2 wins")
    else:
        print("It's a tie")

