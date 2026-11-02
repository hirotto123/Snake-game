from snake.game import Game
import os
import time
import msvcrt
def draw(game: Game) -> None:
        for y in range(0, game.height):
                for x in range(0, game.width):
                        if (x,y) == game.snake.head():
                                print('🐍', end = '')
                        elif (x,y) in game.snake.body:
                                print("🟢", end = '')
                        elif (x,y) == game.food:
                                print('🍎', end = '')
                        elif (((x==0) or (x == game.width - 1)) or ((y == 0) or (y == game.height - 1))):
                                print('🧱', end = '')
                        else:
                                print('⬜', end = '')   
                print() 
        print(f"Score: {game.score}, Level: {game.level}")       

if __name__ == '__main__':
        game = Game(20,20,2)
        draw(game)  
        current_direction = (1, 0)
        DIRECTIONS = {
            b'H': (0, -1),   # вверх
            b'P': (0, 1),    # вниз
            b'K': (-1, 0),   # влево
            b'M': (1, 0),    # вправо
            }
        while not game.is_over:
            if msvcrt.kbhit():
                key = msvcrt.getch()        
                if key == b'\xe0':  
                    key = msvcrt.getch()
                    direction = DIRECTIONS.get(key)
                    if direction is not None:
                        if (current_direction[0] + direction[0], current_direction[1] + direction[1]) != (0,0):
                            current_direction = direction
            game.step(current_direction)            
            os.system('cls' if os.name == 'nt' else 'clear') 
            draw(game)
            time.sleep(game.delay)