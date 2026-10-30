from snake.snake import Snake
from snake.game import Game

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

def test_good_food():
    game = Game(10,10, 1)
    assert 0 <= game.food[0] < 10
    assert 0 <= game.food[1] < 10
    assert game.food not in game.snake.body

def test_step():
    game = Game(10,10,1)
    game.step((1,0))            
    assert game.snake.head() == (6,5)
    assert game.score == 0
    assert game._game_over == False

def test_eat_food():
    game = Game(10,10,1)
    game.food = (6,5)
    initial_len = len(game.snake.body)
    game.step((1,0))
    assert game.score == 1
    assert len(game.snake.body) == initial_len + 1
    assert game.food != (6,5)

def test_game_over():
    game = Game(10,10,1)
    game.snake.body = [(9,5)]
    game.step((1,0))
    assert game._game_over == True