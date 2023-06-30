quiz = {
    "question1": {
        "question" : "What year did the Titanic sink?",
        "answer": "1912"
    },
    "question2": {
        "question" : "Which country is Tasmania a part of?",
        "answer": "Australia"
    },
    "question3": {
        "question" : "What biological order do frogs belong to?",
        "answer": "Amphibians"
    },
    "question4": {
        "question" : "Who painted the Mona Lisa?",
        "answer": "Leonardo da Vinci"
    },
    "question5": {
        "question" : "What is your body's largest organ?",
        "answer": "skin"
    },
    "question6": {
        "question" : "What is the joule a unit of?",
        "answer": "Energy"
    },
    "question7": {
        "question" : "How many oceans are there on Earth?",
        "answer": "Five"
    },
    "question8": {
        "question" : "In what country could you find the Leaning Tower of Pisa?",
        "answer": "Italy"
    },
    "question9": {
        "question" : "What is the chemical symbol for potassium?",
        "answer": "K"
    },
    "question10": {
        "question" : "What is the deepest point in the ocean?",
        "answer": "Challenger Deep"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value["answer"].lower():
        print('Correct')
        score = score + 1
        print("Your Score is: " +str(score))
        print("")
        print("")
        
    else:
        print('Incorrect!')
        print("The answer is: " + value["answer"])
        print("Your Score is: " +str(score))
        print("")
        print("")
     
print("You got " + str(score) + " out of 10 questions correctly")   
print("Your percentage is " + str(int(score/10 * 100)) + "%")
        