import random

from snake.snake import Snake

POINTS_FOR_LVLUP = 10
MAX_SPEED = 3

class Game:
    @property
    def delay(self) -> float:
        return 1.0/self.speed
    @property
    def is_over(self) -> bool:
        return self._game_over
    @property
    def is_victory(self) -> bool:
        return self._victory
    def __init__(self, w: int, h: int, speed: int) -> None:
        self.width: int = w + 2
        self.height: int = h + 2
        self.speed: int = speed
        self.snake = Snake(((w+2)//2, (h+2)//2), (1,0))
        self.score = 0
        self.level = 1
        self._game_over = False
        self._victory = False
        self.food = (0,0)
        self.spawn_food()

    def spawn_food(self) -> None:
        while True:
            y = random.randint(1, self.height-2)
            x = random.randint(1, self.width-2)
            if (x,y) not in self.snake.body:
                self.food = (x,y)
                break

    def step(self, direction: tuple[int, int]) -> None:
        head = self.snake.head()
        new_head = (head[0] + direction[0], head[1] + direction[1])
        ate_food = new_head == self.food
        if new_head == self.food:
            self.snake.grow()
            self.score += 1
            if self.score % POINTS_FOR_LVLUP == 0:
                self.level += 1
                if self.speed < MAX_SPEED:
                    self.speed += 1
        self.snake.move(direction[0], direction[1])
        if len(self.snake.body) == (self.width - 2)*(self.height -2):
                    self._victory = True
                    self._game_over = True
        if ate_food and not self._game_over:
            self.spawn_food()
        head = self.snake.head()
        if (head[0] < 1 or head[0] >= (self.width -1) or
            head[1] < 1 or head[1] >= (self.height - 1)):
            self._game_over = True
        if self.snake.collides_self():
            self._game_over = True    

