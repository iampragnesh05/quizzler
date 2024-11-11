from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk  # This requires the pillow library: install with `pip install pillow`
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CORRECT_COLOR = "green"
WRONG_COLOR = "red"
DEFAULT_COLOR = "white"

class QuizInterface:
    def __init__(self , quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 13),
            pady=20
        )
        self.score_label.grid(row=0, column=1, sticky="e")

        # Question box
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Question goes here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            anchor="center"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # True and False buttons
        true_image = Image.open("Images/true.png")
        self.true_button_image = ImageTk.PhotoImage(true_image)
        self.true_button = Button(image=self.true_button_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = Image.open("Images/false.png")
        self.false_button_image = ImageTk.PhotoImage(false_image)
        self.false_button = Button(image=self.false_button_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
            self.canvas.config(bg=DEFAULT_COLOR)  # Reset background color for the next question
        else:
            self.quiz_over()

    def true_pressed(self):
        correct = self.quiz.check_answer("True")
        if correct:
            self.canvas.config(bg=CORRECT_COLOR)  # Green for correct
            self.update_score()  # Update score on correct answer
        else:
            self.canvas.config(bg=WRONG_COLOR)  # Red for wrong
            print("Incorrect. You chose True.")  # Print feedback on incorrect answer
        self.window.after(1000, self.get_next_question)  # Wait 1 second before showing the next question

    def false_pressed(self):
        correct = self.quiz.check_answer("False")
        if correct:
            self.canvas.config(bg=CORRECT_COLOR)  # Green for correct
            self.update_score()  # Update score on correct answer
        else:
            self.canvas.config(bg=WRONG_COLOR)  # Red for wrong
            print("Incorrect. You chose False.")  # Print feedback on incorrect answer
        self.window.after(1000, self.get_next_question)  # Wait 1 second before showing the next question

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def quiz_over(self):
        # Display a message box when the quiz is over
        messagebox.showinfo(
            "Game Over",
            f"Your final score is: {self.quiz.score}/{len(self.quiz.question_list)}",
        )
        self.window.quit()

