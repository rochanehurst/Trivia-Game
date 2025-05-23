from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#24273a"
CANVAS_COLOR = "#f7f7f7"
CORRECT_COLOR = "#3bb273"
WRONG_COLOR = "#ff6b6b"
FONT_NAME = "Segoe UI"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("🧠 Brain Bites")
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)

        style = ttk.Style()
        style.configure("TButton", font=(FONT_NAME, 12, "bold"), padding=10)
        style.map("TButton",
                  foreground=[('active', 'white')],
                  background=[('active', '#3e8e41')])

        # Score
        self.score_label = Label(
            text="Score: 0",
            fg="white", bg=THEME_COLOR,
            font=(FONT_NAME, 14, "bold")
        )
        self.score_label.grid(row=0, column=1, sticky="e")

        # Question canvas
        self.canvas = Canvas(width=400, height=250, bg=CANVAS_COLOR, bd=0, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            200, 125, width=280,
            text="Question goes here",
            fill=THEME_COLOR,
            font=(FONT_NAME, 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Buttons
        self.true_button = ttk.Button(text="✅ TRUE", command=self.true_pressed)
        self.true_button.grid(row=2, column=0, pady=10, padx=5)

        self.false_button = ttk.Button(text="❌ FALSE", command=self.false_pressed)
        self.false_button.grid(row=2, column=1, pady=10, padx=5)

        # Feedback
        self.feedback_label = Label(
            text="", fg="white", bg=THEME_COLOR,
            font=(FONT_NAME, 20, "bold")
        )
        self.feedback_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=CANVAS_COLOR)
        self.feedback_label.config(text="")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"🎉 You're done!\n\nFinal Score: {self.quiz.score}/{len(self.quiz.q_list)}"
            )
            self.true_button.state(["disabled"])
            self.false_button.state(["disabled"])
            self.feedback_label.config(text="🏁")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.canvas.config(bg=CORRECT_COLOR if is_right else WRONG_COLOR)
        self.feedback_label.config(text="✅ Nice!" if is_right else "❌ Oof!")
        self.window.after(900, self.get_next_question)
