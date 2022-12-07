import random
import words

score_under_3 = [
    "I'm sure you can do better than that.",
    "Oops",
    "Again!",
]
score_under_6=[
    "Not bad but not enough!",
    "Try again!",
]
score_under_10=[
"Great!",
"That was good, though.",
"Nice try."
]
score_under_15=[
"That one was difficult, right?",
]
score_under_20=[
    "THAT WAS CLOSE!",
    "You've been trying hard, I know.",
    "Just one more time again!"
]
score_more_30=[ #Game clear
"IMPOSSIBLE!",
"You are THE MASTER of hang man, aren't you?",
"You are THE ONE I HAVE BEEN WAITING FOR!",
"I can't believe you've really got here."
]


class Lines:
    def __init__(self):
        self.under3 = random.choice(score_under_3)
        self.under6 = random.choice(score_under_6)
        self.under10 = random.choice(score_under_10)
        self.under15 = random.choice(score_under_15)
        self.under20 = random.choice(score_under_20)
        self.more30 = random.choice(score_more_30)
    def greeting_line(self):
        return "Hi, and I'm about to die."

    def score_evaluation_line(self,score):
        if score < 3:
            return self.under3
        elif score < 6:
            return self.under6
        elif score < 10:
            return self.under10
        elif score < 15:
            return self.under15
        elif score < 20:
            return self.under20
        elif score >= 30:
            return self.more30



