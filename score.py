from turtle import Turtle  # Import the Turtle class from the turtle module
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):  # Define a Score class that inherits from the Turtle class

    def __init__(self):  # Define the constructor for the Score class
        super().__init__()  # Call the constructor of the parent class
        self.color('White')  # Set the turtle's color to white
        self.score = 0  # Initialize the score to zero default
        self.penup()  # Don't draw while moving the turtle
        self.hideturtle()  # Hide the turtle
        self.goto(0, 260)  # Move the turtle to the top center of the screen
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Write the initial score to the screen

    def game_over(self):
        self.goto(0, 0)  # go to the center
        self.write("Game Over", align=ALIGNMENT, font=FONT)  # Write the initial score to the screen

    def update_score(self):  # Define a method to update the score
        self.clear()  # Clear any previous score text from the screen
        self.score += 1  # Increment the score by one
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Write the updated score to the screen
