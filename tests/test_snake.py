from snake.snake import Snake

def test_move_right():
    snake = Snake((3,3),(1,0))
    snake.move(1,0)
    head = snake.head()
    assert head == (4,3)

def test_move_up():
    snake = Snake((3,3),(0,-1))
    snake.move(0,-1)
    head = snake.head()
    assert head == (3,2)

def test_move_down():
    snake = Snake((3,3),(0,1))
    snake.move(0,1)
    head = snake.head()
    assert head == (3,4)    
