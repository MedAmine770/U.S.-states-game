import turtle
from turtle import Turtle
import pandas as pd

# Setup the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the CSV file into a DataFrame
data = pd.read_csv("50_states.csv")

# List of guessed states
list_state = []

# All states
states = data.state.to_list()

# Open game, keep game window open
while len(list_state) < 50:
    answer = screen.textinput(title=f"Number of states guessed: {len(list_state)}/50", prompt="Give name of state").title()
    
    if answer == "Exit":
        states_not_mentioned = []
        for state in states:
            if state not in list_state:
                states_not_mentioned.append(state)
        
        new_data = pd.DataFrame(states_not_mentioned)
        new_data.to_csv("states_not_mentioned.csv")
        break
    
    row = data[data.state == answer]

    if not row.empty:
        list_state.append(answer)
        
        # Convert the row to a list
        row_list = row.values.tolist()[0]
        
        # Extract the coordinates from the list
        value_x = int(row_list[1])
        value_y = int(row_list[2])

        state_turtle = Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()  # Ensure the turtle does not draw lines while moving
        state_turtle.goto(value_x, value_y)
        state_turtle.color("black")
        state_turtle.write(answer, align="center", font=("Arial", 12, "normal"))

# Keep the screen open until clicked




