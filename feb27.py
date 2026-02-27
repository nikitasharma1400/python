import turtle

def apply_rules(axiom, rules, iterations):
    for _ in range(iterations):
        axiom = "".join([rules.get(char, char) for char in axiom])
    return axiom

def draw_l_system(t, instructions, length, angle):
    for cmd in instructions:
        if cmd == 'F': t.forward(length)
        elif cmd == '+': t.right(angle)
        elif cmd == '-': t.left(angle)

def main():
    # settings for the koch snowflake
    axiom = "F--F--F"
    rules = {"F": "F+F--F+F"}
    iterations = 3
    angle = 60
    length = 5
    
    # setup turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("black")
    t.color("cyan")
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    
    # execute
    final_instructions = apply_rules(axiom, rules, iterations)
    draw_l_system(t, final_instructions, length, angle)
    
    wn.exitonclick()

if __name__ == "__main__":
    main()