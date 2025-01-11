import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states quiz")
screen.setup(width=960, height=600)

image = "Ukraine_map.gif"
screen.addshape(image)
turtle.shape(image)

REGION_COUNT = 25


regions_table = pandas.read_csv("data.csv")

regions = regions_table["region"].values


def print_correct_answer(checking_answer):
    row = regions_table[regions_table["region"] == checking_answer]
    x = row["x"].values[0]
    y = row["y"].values[0]
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.goto(x, y)
    text.write(checking_answer)


correct_guesses = []

while len(correct_guesses) < REGION_COUNT:
    checking_answer = (
        turtle.textinput(
            title=f"Правильних відповідей {len(correct_guesses)}/25",
            prompt="Яка назва області?",
        )
        .strip()
        .title()
    )

    if checking_answer in regions:
        print_correct_answer(checking_answer)
        correct_guesses.append(checking_answer)
    if checking_answer == "Exit" or checking_answer == "Вихід":
        regions_to_learn = list(set(regions) - set(correct_guesses))
        data = pandas.DataFrame(regions_to_learn)
        data.to_csv("regions_need_to_learn.csv")
        break

    if len(correct_guesses) == REGION_COUNT:
        congratulation = turtle.Turtle()
        congratulation.penup()
        congratulation.hideturtle()
        congratulation.goto(0, 0)
        congratulation.write(
            "Вітаємо! Ви відгадали всі області!",
            align="center",
            font=("Arial", 24, "bold"),
        )
        break
