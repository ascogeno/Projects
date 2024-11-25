def main():
    """Prompts the user to asnwer 10 questions with D,d,a,A. Returns their score and whether or not they're doing good with self esteem"""

    print("""This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:

             D means you strongly disagree with the statement.
             d means you disagree with the statement.
             a means you agree with the statement.
             A means you strongly agree with the statement.
                                                            """)
    score = 0
    questions = ["1. I feel that I am a person of worth, at least on an equal plane with others",
                 "2. I feel that I have a number of good qualities.",
                 "3. All in all, I am inclined to feel that I am a failure.",
                 "4. I am able to do things as well as most other people.",
                 "5. I feel I do not have much to be proud of.",
                 "6. I take a positive attitude toward myself.",
                 "7. On the whole, I am satisfied with myself.",
                 "8. I wish I could have more respect for myself.",
                 "9. I certainly feel useless at times.",
                 "10. At times I think I am no good at all."]
    for x, question in enumerate(questions):
        print(f"{question}")
        if x == 0 or x==1 or x==3 or x==5 or x==6:
            score = score+posScore()
        if x == 2 or x==4 or x==7 or x==8 or x==9:
            score = score+negScore()
    
    print(f"Your score is {score}")
    print("A score below 15 may indicate problematic low self-esteem.")

def posScore():
    """Tallies the score for the user's answers to positive questions, and returns that tally"""

    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3
    return score
    
def negScore():
    """Tallies the score for the user's answers to negative questions, and returns that tally"""

    answer = input('Enter D, d, a, or A: ')
    score = 0
    if answer == 'D':
        score = 3
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    elif answer == 'A':
        score = 0
    return score

if __name__ == "__main__":
    main()