import turtle as tl
import random
import numpy as np

screen = tl.Screen()
screen.bgcolor("white")
screen.title("Mandarin Tree")

# Set up tl parameters
tl.speed(0)
tl.penup()
tl.goto(0, -250)
tl.pendown()
tl.left(90)


# L-system axiom and rules
axiom = "TTTTL"
def rules(char,i) :
    if char == "T" and (i>0 and random.random()<0.10): 
        return "R[^RL]",
    elif char == "L": 
        return "B[<TL][>TL]",
    elif char == "B": 
        return "TB"
    else : 
        return char


class Tree:
# Drawing parameters
    level =0
    trunk_thickness = 20
    trunk_length = 10
    branch_angle = 14
    tilt_angle_range = 30
    tilt_correction = 25
    #leaf_colors =

    # L-system generation function
    def generate_l_system(axiom, rules, iterations):
        current_sequence = axiom
        for i in range(iterations):
            
            next_sequence = "".join("".join(rules(char,i)) for char in current_sequence)
            current_sequence = next_sequence
        return current_sequence
    
    # Drawing function
    def draw_mandarin_tree(sequence):
        stack = []
        #Tree.drawLog()
        
        for char in sequence:
            if char == "T":
                if random.random() < 0.5:  # 50% probability of skipping trunk
                    continue
                Tree.drawLog()
                
                
            elif char == "B":
                tl.color("brown4")
                if random.random() < 0.5:  # 50% probability of skipping branch
                    continue
                tl.width(Tree.trunk_thickness* 0.75**Tree.level)
                tl.forward(Tree.trunk_length)
            elif char == "L":
                if random.random() < 0.05:  # 5% chance for tangerine leaf
                    tl.fillcolor("orange")
                    tl.color("orange")
                    tl.begin_fill()

                    tl.circle(10)
                    tl.end_fill()
                else:
                    Tree.drawLeaf()
            elif char == "[":
                stack.append((tl.position(), tl.heading(), tl.pensize(),Tree.level))
                Tree.level += 1  # Reduce trunk thickness
            elif char == "]":
                
                position, heading, pensize, Tree.level = stack.pop()
                tl.penup()
                tl.goto(position)
                tl.setheading(heading)
                tl.pendown()
                tl.pensize(pensize)
            elif char == "<":
                tl.left(14)
            elif char == ">":
                tl.right(14)
            elif char == "^":
                angle=random.uniform(-Tree.tilt_angle_range, Tree.tilt_angle_range)
                tilt = angle + Tree.tilt_correction*np.sign(angle)
                tl.right(tilt)
                
                
    def drawLog():
        tl.color("brown4")
        tl.width(Tree.trunk_thickness* 0.75**Tree.level)
        tl.forward(Tree.trunk_length)
    def drawLeaf():
        tl.width(1)
        tl.color("green")
        if random.random() <0.15:
            tl.fillcolor('lime')
        else:
            tl.fillcolor('green')
        tl.begin_fill()
        tl.circle(4)
        tl.end_fill()
    # Generate and draw the Mandarin tree

iterations = 12
# = Tree.generate_l_system(axiom, rules, iterations)
screen.tracer(0)
example = ""
mandarin_sequence = Tree.generate_l_system(axiom,rules,iterations)
Tree.draw_mandarin_tree(mandarin_sequence)

screen.update()

screen.mainloop()
# Hide tl