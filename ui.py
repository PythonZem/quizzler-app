from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}",
                                 background=THEME_COLOR,
                                 fg="white",
                                 font=("Arial", 13, "italic"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="White")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 18, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        TRUE_IMG = PhotoImage(file="images/true.png")
        self.buttons_true = Button(image=TRUE_IMG, highlightthickness=0, command=self.take_answer_true)
        self.buttons_true.grid(column=0, row=2)

        FALSE_IMG = PhotoImage(file="images/false.png")
        self.buttons_false = Button(image=FALSE_IMG, highlightthickness=0, command=self.take_answer_false)
        self.buttons_false.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You`ve reached thr end of the quiz.")
            self.buttons_true.config(state="disabled")
            self.buttons_false.config(state="disabled")
    def take_answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def take_answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(background="Green")
        else:
            self.canvas.config(background="Red")
        self.window.after(1000, self.get_next_question)