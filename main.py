
#import the questions.py file bzw. eben die Klasse daraus, damit wir sie dann verwenden können

from Question import Question


#write down a list of question prompts (not really the questions but the promots) in an array
question_prompts = [
    "Habe ich Hendrik lieb?\n(a) Nein\n(b) Wenn er mir gerade Essen macht dann ja\n(c) Ein bisschen\n\n",
    "Werde ich jemals programmieren können?\n (a) Äh, obviously not\n(b) wenn mein Gehirn noch wächst, dann ja\n (c) Sehr unwahrscheinlich, aber möglich",
    "Wieviele Antworten hast du falsch beantwortet?\n(a) Beide\n(b) Keine\n(c) woher willst du das wissen?!"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
]
#this up here is an array

def run_test (questions):
    print ("\nIf you get at least two incorrect, you owe me Pasta! \nLet's get it started: \n")
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score =+1
    print("Wow, you got " + str(score) + "/" + str(len(questions)) + " correct")

    if score < 2:
        print (",which means Pasta for me")
    else:
        print ("sadly no pasta vor bea..")

run_test(questions)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# NICHT DIE ANTWORTEN OBEN ANSCHAUEN!!!!!!!!!!!!!!!!!
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
