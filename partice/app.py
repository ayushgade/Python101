from Question import Question

questions_prompts = [
    "What color are Apples? \n(a) Red\n(b) Purple,\n(c) Orange\n\n",
    "What color are Bananas? \n(a) Teal\n(b) Magenta,\n(c) Yellow\n\n",
    "What color are strawberries? \n(a) Yellow\n(b) Red,\n(c) Blue\n\n"
]

questions = [
        Question(questions_prompts[0], "a"),
        Question(questions_prompts[1], "c"),
        Question(questions_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("You Got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)