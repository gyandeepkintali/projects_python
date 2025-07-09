import turtle
import pandas as pd  # type: ignore
from typing import List, Tuple

states_data = [
    ["Alabama", 139, -77], ["Alaska", -204, -170], ["Arizona", -203, -40],
    ["Arkansas", 57, -53], ["California", -297, 13], ["Colorado", -112, 20],
    ["Connecticut", 297, 96], ["Delaware", 275, 42], ["Florida", 220, -145],
    ["Georgia", 182, -75], ["Hawaii", -317, -143], ["Idaho", -216, 122],
    ["Illinois", 95, 37], ["Indiana", 133, 39], ["Iowa", 38, 65],
    ["Kansas", -17, 5], ["Kentucky", 149, 1], ["Louisiana", 59, -114],
    ["Maine", 319, 164], ["Maryland", 288, 27], ["Massachusetts", 312, 112],
    ["Michigan", 148, 101], ["Minnesota", 23, 135], ["Mississippi", 94, -78],
    ["Missouri", 49, 6], ["Montana", -141, 150], ["Nebraska", -61, 66],
    ["Nevada", -257, 56], ["New Hampshire", 302, 127], ["New Jersey", 282, 65],
    ["New Mexico", -128, -43], ["New York", 236, 104], ["North Carolina", 239, -22],
    ["North Dakota", -44, 158], ["Ohio", 176, 52], ["Oklahoma", -8, -41],
    ["Oregon", -278, 138], ["Pennsylvania", 238, 72], ["Rhode Island", 318, 94],
    ["South Carolina", 218, -51], ["South Dakota", -44, 109], ["Tennessee", 131, -34],
    ["Texas", -38, -106], ["Utah", -189, 34], ["Vermont", 282, 154],
    ["Virginia", 234, 12], ["Washington", -257, 193], ["West Virginia", 200, 20],
    ["Wisconsin", 83, 113], ["Wyoming", -134, 90]
]

def setup_screen() -> turtle.Screen:
    """Initialize and setup the game screen"""
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.setup(725, 491)  
    
    image = "blank_states_img.gif"
    try:
        screen.addshape(image)
        turtle.shape(image)
    except turtle.TurtleGraphicsError:
        print(f"Error: Cannot find image file '{image}'. Make sure it's in the same directory.")
        exit(1)
    
    return screen

def create_states_dataframe() -> pd.DataFrame:
    """Create DataFrame with states data"""
    return pd.DataFrame(states_data, columns=["state", "x", "y"])

def write_state_name(state_name: str, x: int, y: int) -> None:
    """Write state name at given coordinates"""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.write(state_name, align="center", font=("Arial", 8, "normal"))

def main():
    screen = setup_screen()
    data = create_states_dataframe()
    all_states = data.state.tolist()
    guessed_states: List[str] = []
    
    while len(guessed_states) < 50:
        score = len(guessed_states)
        title = f"{score}/50 States Correct"
        
        answer_state = screen.textinput(title=title, prompt="What's another state's name?")
        
        if not answer_state or answer_state.lower() == "exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            pd.DataFrame(missing_states, columns=["States to Learn"]).to_csv("states_to_learn.csv")
            break
        
        answer_state = answer_state.title()
        if answer_state in all_states and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state].iloc[0]
            write_state_name(answer_state, int(state_data.x), int(state_data.y))
    
    if len(guessed_states) == 50:
        print("Congratulations! You've guessed all states!")
    else:
        print(f"Game ended. You got {len(guessed_states)} states correct!")
    
    screen.exitonclick()

if __name__ == "__main__":
    main()