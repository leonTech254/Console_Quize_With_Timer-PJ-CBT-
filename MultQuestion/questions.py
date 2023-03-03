
class Questions:
    question_list = [
        {
            "question": "Where is Lambogini made? (a) Germany\n (b) Italy\n (c) Nigeria\n\n",
            "answer": "b"
        },
        {
            "question": "Who is the first man to travel to space? (a) Neil Armstrong\n (b) Yuri Gagarin\n (c) Micheal Jackson\n\n",
            "answer": "b"
        },
        {
            "question": "Who is the first man to land on the moon? (a) Neil Armstrong\n (b) Yuri Gagarin\n (c) Micheal Jackson\n\n",
            "answer": "a"
        },
        {
            "question": "Who is the founder of Apple Inc.? (a) Mark Zuckerberg\n (b) Steve Jobs\n (c) Sergery Brin\n",
            "answer": "b"
        },
        {
            "question": "What is Google Inc parent? (a) Alphabet\n (b) Sun Microsoft\n (c) Amazon\n\n",
            "answer": "a"
        },
        {
            "question": "Who is the founder of Globaltech\n (a) Paul Smith\n (b) G.O Asogbon\n (c) Praise Jah\n\n",
            "answer": "b"
        },
        {
            "question": "Who is the president of Germany?\n (a) Angela Merkel (b) Buhari Jones\n (c) Nana Addo\n\n",
            "answer": "a"
        },
        {
            "question": "What is the full meaning of YCMA?\n (a) Young Men Clubbing Activity\n (b) Young Church Movement Action\n (c) Young Men Christain Association\n (d) Young Men Chest Arm\n\n",
            "answer": "c"
        },
        {
            "question": "Which of the following is a name of a continent? (a) South America\n (b) Niger\n (c) Spain\n\n",
            "answer": "a"
        },
        {
            "question":  "_____ is the name of a continent and a country? (a) United States\n (b) Australia\n (c) Europe\n\n",
            "answer": "b"
        }

    ]

    def grades(score):
        if score == 0:
            return "\nYour Grade: F"
        elif (score >= 1) and (score <= 4):
            return "\nYour Grade: D"
        elif (score >= 5) and (score <= 6):
            return "\nYour Grade: C"
        elif (score >= 6) and (score < 8):
            return "\nYour Grade: B"
        elif (score > 8) and (score <= 9):
            return "\nYour Grade: B+"
        else:
            return "\nYour Grade: A"
