import time
from datetime import datetime, timedelta
from questions import Questions

quize_token = 1224


class Management:
    score = 0
    QuizeDuaration = 1
    Started = False
    Start_time = 0


def user_credentions():
    """This function 
    verifies the Student"""
    name = input("ENTER YOUR NAME: ")
    branch = input("WHERE IS YOUR BRANCH: ")
    token_number_user = input("ENTER TOKEN NUMBER: ")

    if name == '' or branch == '' or token_number_user == '':
        print("\nall Field required")
        return "failed"
    else:
        if quize_token == token_number_user:
            print("Token number Verified")
            return "success"


def QuizeTimer():
    if Management.Started:
        duration = timedelta(seconds=Management.QuizeDuaration)
        current_time = datetime.now()
        time_elapsed = current_time-Management.Start_time
        if time_elapsed > duration:
            return False
        else:
            return True
    else:
        Management.Start_time = datetime.now()
        return True


def start_Quize():
    for question in Questions.question_list:
        timerResponse = QuizeTimer()
        if timerResponse:
            print(question["question"])
            answer = input("ENTER ANSWER: ")
            if answer == question["answer"]:
                Management.score += 1
        else:
            print("TIMER OVER!!")
            break


def UserResults():
    print(f"Your score is: {Management.score}")
    Questions.grades(score=Management.score)


start_Quize()
