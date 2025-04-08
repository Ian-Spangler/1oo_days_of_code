from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
            width=280,
            text=f"bla",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        check_image = PhotoImage(file="Images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.check_true)
        self.check_button.grid(column=0, row=2)

        cross_image = PhotoImage(file="Images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.check_false)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def check_true(self):
        check = self.quiz.check_answer("True")
        self.give_feedback(check)

    def check_false(self):
        check = self.quiz.check_answer("False")
        self.give_feedback(check)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(2000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")