import turtle
import pandas

# Game class
class USStatesGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game 🇺🇸")
        self.screen.setup(width=725, height=491)
        self.screen.bgpic("blank_states_img.gif")

        self.data = pandas.read_csv("50_states.csv")
        self.all_states = self.data.state.to_list()
        self.guessed_states = []

    def prompt_guess(self):
        return self.screen.textinput(
            title=f"{len(self.guessed_states)}/50 States Correct",
            prompt="What's another state's name?"
        )

    def mark_state(self, state_name):
        state_data = self.data[self.data.state == state_name]
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(int(state_data.x), int(state_data.y))
        marker.write(state_name, align="center", font=("Arial", 8, "normal"))

    def play(self):
        while len(self.guessed_states) < 50:
            answer = self.prompt_guess()
            if answer is None:
                break
            answer = answer.title()
            if answer in self.all_states and answer not in self.guessed_states:
                self.guessed_states.append(answer)
                self.mark_state(answer)

        self.save_missing_states()

    def save_missing_states(self):
        missing = [state for state in self.all_states if state not in self.guessed_states]
        pandas.DataFrame(missing).to_csv("states_to_learn.csv")
        print("Game over. Missing states saved to 'states_to_learn.csv'.")

# Run the game
if __name__ == "__main__":
    game = USStatesGame()
    game.play()