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

def test_grow():
    snake = Snake((1,1), (1,0))
    snake.move(1,0)
    snake.grow()
    snake.move(1,0)
    assert len(snake.body) == 2
    assert snake.body == [(3,1), (2,1)]

def test_without_collisions():
    snake = Snake((1,1), (1,0))
    snake.move(1,0)
    snake.grow()
    snake.move(1,0)
    assert snake.collides_self() == False

def test_with_collisions():
    snake = Snake((1,1), (1,0))
    snake.body = [(1,1),(1,0),(1,1)]
    assert snake.collides_self() == True