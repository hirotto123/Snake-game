import random
from snake.snake import Snake

class Game:
    def __init__(self, w: int, h: int, speed: int) -> None:
        self.width: int = w
        self.height: int = h
        self.speed: int = speed
        self.snake = Snake((w//2, h//2), (1,0))
        self.score = 0
        self.level = 1
        self._game_over = False
        self.food = (0,0)
        self.spawn_food()

    def spawn_food(self) -> None:
        while True:
            y = random.randint(0, self.height - 1)
            x = random.randint(0, self.width - 1)    
            if (x,y) not in self.snake.body:
                self.food = (x,y)
                break

    def step(self, direction: tuple[int, int]) -> None:
        head = self.snake.head()
        new_head = (head[0] + direction[0], head[1] + direction[1])
        if new_head == self.food:
            self.snake.grow()
            self.score += 1
            self.spawn_food()
        self.snake.move(direction[0], direction[1]) 
        head = self.snake.head()  
        if (head[0] < 0 or head[0] >= self.width or head[1] < 0 or head[1] >= self.height):
            self._game_over = True
        if self.snake.collides_self():
            self._game_over = True            

