import time
from datetime import datetime, timedelta
from questions import Questions
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)


class Management:
    score = 0
    QuizeDuaration = 15  # time in seconds
    Started = False
    Start_time = 0
    Name = ""
    quize_token = "1224"


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

        Management.Name = name
        if Management.quize_token == token_number_user:
            print("Token number Verified")
            return "success"
        else:
            print("Token Failed")


def QuizeTimer():

    if Management.Started:
        duration = timedelta(seconds=Management.QuizeDuaration)
        current_time = datetime.now()
        time_elapsed = current_time-Management.Start_time
        seconds_rem = int(duration.total_seconds()) - \
            int(time_elapsed.total_seconds())
        print(f"TIME REMEINING: {seconds_rem}seconds \n")
        if time_elapsed > duration:

            return False
        else:

            return True
    else:
        Management.Start_time = datetime.now()
        Management.Started = True
        return True


def start_Quize():
    for question in Questions.question_list:
        timerResponse = QuizeTimer()

        if timerResponse:
            print()
            engine.say(question["question"])
            engine.runAndWait()
            answer = input("ENTER ANSWER: ")
            if answer == question["answer"]:
                Management.score += 1
        else:
            print("TIMER OVER!!")
            break


def UserResults():
    grades = Questions.grades(score=Management.score)
    Results = f"""
Name:{Management.Name}
Your score is: {Management.score}
Grades: {grades}
"""

    print(Results)


if __name__ == "__main__":
    QuizeTimer()
    response = user_credentions()
    if response:
        start_Quize()
        UserResults()
