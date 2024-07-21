# Rock Paper Scissors game - TASK 4
import random

def play():
    user_input = ''
    user_score = 0
    comp_score = 0
    while user_input != '0':
        print("Choose any one:-\n rock -> r\n paper -> p\n scissors -> s\n to exit -> 0")
        user_input = input("Enter your choice: ").lower()
        if user_input not in ['r','p','s','0']:
            print("Invalid Input!")
        else:
            comp_choice = random.choice(['r','p','s'])
            if comp_choice == 'r':
                if user_input == 'r':
                    print(f"Your Choice: {user_input} \nComputer Choice: {comp_choice}")
                    print("Tie!")
                elif user_input == 'p':
                    print(f"Your Choice: {user_input} \nComputer Choice: {comp_choice}")
                    print("You win!")
                    user_score += 1
                elif user_input == 's':
                    print(f"Your Choice: {user_input} \nComputer Choice: {comp_choice}")
                    print("You lose!")
                    comp_score += 1
            elif comp_choice == 'p':
                if user_input == 'p':
                    print(f"Your Choice: {user_input} \nComputer Choice: {comp_choice}")
                    print("Tie!")
                elif user_input == 's':
                    print(f"Your Choice: {user_input} \nComputer Choice: {comp_choice}")
                    print("You win!")
                    user_score += 1
                elif user_input == 'r':
                    print(f"Your Choice: {user_input} \nComputer Choice: {comp_choice}")
                    print("You lose!")
                    comp_score += 1
            elif comp_choice == 's':
                if user_input == 's':
                    print(f"Your Choice: {user_input} \nComputer Choice: {comp_choice}")
                    print("Tie!")
                elif user_input == 'r':
                    print(f"Your Choice: {user_input} \nComputer Choice: {comp_choice}")
                    print("You win!")
                    user_score += 1
                elif user_input == 'p':
                    print(f"Your Choice: {user_input} \nComputer Choice: {comp_choice}")
                    print("You lose!")
                    comp_score += 1
        print("---------------------------------------------")

    if user_score > comp_score:
        print(f"Your Score: {user_score} \nComputer Score: {comp_score}")
        print("YOU WON!!")
    elif user_score == comp_score:
        print(f"Your Score: {user_score} \nComputer Score: {comp_score}")
        print("TIE MATCH!")
    elif user_score < comp_score:
        print(f"Your Score: {user_score} \nComputer Score: {comp_score}")
        print("YOU LOST! BETTER LUCK NEXT TIME!")
    
    if user_input == '0':
        play_again = input("Do you wish to play again?\n yes -> y\n no -> n\n").lower()
        if play_again == 'y':
            play()
        elif play_again == 'n':
            print("Goodbye!")
        else:
             print("Invalid!")


play()
