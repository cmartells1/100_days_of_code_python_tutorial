from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Quiz Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0)
        self.check_button.grid(column=0, row=2)

        x_image = PhotoImage(file="images/false.png")
        self.x_button = Button(image= x_image, highlightthickness=0)
        self.x_button.grid(column=1, row=2)

        self.window.mainloop()