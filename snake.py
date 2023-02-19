
import turtle
import random

WIDTH = 600
HEIGHT = 600
#DELAY = 150 #millisec
FOODSIZE = 10

highscore =0

offsets = {
    "up": (0, 20),
    "down" : (0, -20),
    "left" : (-20, 0),
    "right" : (20, 0)
}



def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")


def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"


def game_loop():
    global highscore
    stamper.clearstamps() #remove existing stamps made by stamper

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    #check collision
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        if score > highscore:
            highscore = score
        reset()
    else:
        #add new head to snake body
        snake.append(new_head)

        if not food_collision():
            snake.pop(0)   #remove last segment of snake ie keep same length unless colide with food

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        screen.title(f"Snake game  Score: {score}   HIGHSCORE: {highscore}")
        #refresh screen
        screen.update()

        #repeat
        turtle.ontimer(game_loop, DELAY)


def food_collision():
    global food_pos, score, DELAY, FOODSIZE, count
    if get_distance(snake[-1], food_pos) <20:
        if DELAY >= 30:
            DELAY -= 5
        # score += 10
        count += 1    
        if(FOODSIZE == 10):
            score += 10
        else:
            score += 20
        if count % 10 == 0:
            FOODSIZE = 30
            food.shapesize(FOODSIZE/20)
        else:
            FOODSIZE = 10
            food.shapesize(FOODSIZE/20)
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- WIDTH/2 + FOODSIZE, WIDTH/2 - FOODSIZE)
    y = random.randint(- HEIGHT/2 + FOODSIZE, HEIGHT/2 - FOODSIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2-y1)**2 + (x2-x1)**2)**0.5
    return distance

def reset():
    global score, snake, snake_direction, food_pos, count, DELAY
    score = 0
    count = 0
    DELAY = 150
    snake = [[0,0], [20,0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    game_loop()
    


#Create a window to do draw
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT) #set dimensions
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)


#event handlers
screen.listen()
bind_direction_keys()

# create snake as a list of coord pairs
# snake = [[0,0], [20,0], [40, 0], [60, 0]]
# snake_direction = "up"
# score = 0


#turtle snake
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.penup()

# food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOODSIZE/20)
food.penup()

reset()

turtle.done()

