from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = 70

all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)
    y_position -= 25

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            
            # 메시지 출력용 거북이
            message_turtle = Turtle()
            message_turtle.hideturtle()
            message_turtle.penup()
            message_turtle.goto(0, 150)

            if winning_color == user_bet:
                message_turtle.write(f"The winner is {winning_color}! Your turtle won!", align="center", font=("Arial", 16, "bold"))
            else:
                message_turtle.write(f"You lost! The {winning_color} turtle won!", align="center", font=("Arial", 16, "bold"))
            
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()