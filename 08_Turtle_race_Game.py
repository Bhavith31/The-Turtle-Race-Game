from turtle import Turtle,Screen
import random
s=Screen()
s.setup(width=500,height=400)
user_bet=s.textinput(title="Make Your Bet",prompt="For which Turtle you are bidding?(available colors :- red,black,blue,orange,green,purple)")
colors=["red","black","blue","orange","green","purple"]
is_race_on=False
all_turtles=[]
a=0
for i in range(len(colors)):
    timmy=Turtle()
    timmy.shape("turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(x=-230,y=-100+a)
    a=a+40
    all_turtles.append(timmy)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on=False
                if user_bet == turtle.pencolor():
                     print(f"{turtle.pencolor()} Won the Race..Your Bet is Doubled..🎉🎉")
                     break
                else:
                     print(f"{turtle.pencolor()} Won the Race..You Lost..🙃")
                     break
            random_speed=random.randint(0,10)
            turtle.forward(random_speed)
s.exitonclick()