import time
from datetime import datetime, timedelta
from questions import Questions

quize_token = 1224


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


def start_Quize():
    for question in Questions.question_list:
        print(question)
        answer = input("ENTER ANSWER: ")


start_Quize()
