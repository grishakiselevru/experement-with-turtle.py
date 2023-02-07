import turtle
import numpy as np
##################################################################################################################
                                #Создаётся один геном на весь эксперимент#
##################################################################################################################
def exp_one(dl=30, ang=90, iter = 8):
    genom = np.random.randint(1, 4, 8)
    print(f'genom is {genom}')
    for i in range(iter):
        for use in genom:

            if use == 1:
                turtle.forward(dl)

            if use == 2:
                turtle.backward(dl)

            if use == 3:
                turtle.left(ang)

            if use == 4:
                turtle.right(ang)
##################################################################################################################
                                    #Создаётся геном каждую итерацию#
##################################################################################################################
def exp_two(dl=30, ang=90, iter = 8):
    for i in range(iter):
        genom = np.random.randint(1, 4, 8)
        print(f'genom is {genom}')
        for use in genom:

            if use == 1:
                turtle.forward(dl)

            if use == 2:
                turtle.backward(dl)

            if use == 3:
                turtle.left(ang)

            if use == 4:
                turtle.right(ang)
##################################################################################################################
                        #Создаётся геном каждую итерацию + усложненные правила#
##################################################################################################################
def exp_three(dl=30, ang=90, iter = 8):
    for i in range(iter):
        genom = np.random.randint(1, 4, 8)
        print(f'genom is {genom}')
        for use in genom:

            if use == 1:
                turtle.forward(dl)
                turtle.right(ang)
                turtle.forward(dl)
                turtle.right(ang)
                turtle.forward(dl)
                turtle.right(ang)
                turtle.forward(dl)
                turtle.right(ang)

            if use == 2:
                turtle.backward(dl)
                turtle.left(ang/2)
                turtle.backward(dl)
                turtle.left(ang/2)
                turtle.backward(dl)
                turtle.left(ang/2)

            if use == 3:
                turtle.left(ang)

            if use == 4:
                turtle.right(ang)

turtle.hideturtle()
exp_three(15, 143, 16)
print("Stop")
turtle.exitonclick()
