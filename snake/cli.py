import argparse
import msvcrt
import os
import time

from snake.game import Game

"""Console interface for snake game"""
def draw(game: Game) -> None:
        """Render the current game state to the terminal"""
        for y in range(0, game.height):
                for x in range(0, game.width):
                        if (x,y) == game.snake.head():
                                print('🐍', end = '')
                        elif (x,y) in game.snake.body:
                                print("🟢", end = '')
                        elif (x,y) == game.food:
                                print('🍎', end = '')
                        elif (((x==0) or (x == game.width - 1)) or
                              ((y == 0) or (y == game.height - 1))):
                                print('🧱', end = '')
                        else:
                                print('⬜', end = '')
                print()
        print(f"Score: {game.score}, Level: {game.level}")

if __name__ == '__main__':
        while True:
                parser = argparse.ArgumentParser(description="Консольная игра Змейка")
                parser.add_argument('--width', type=int, default=20, help='Ширина поля')
                parser.add_argument('--height', type=int, default=20, help='Высота поля')
                parser.add_argument('--speed', type=int, default=2, help='Начальная скорость')
                args = parser.parse_args()
                game = Game(args.width,args.height,args.speed)
                draw(game)
                current_direction = (1, 0)
                DIRECTIONS = {
                        b'H': (0, -1),   # вверх
                        b'P': (0, 1),    # вниз
                        b'K': (-1, 0),   # влево
                        b'M': (1, 0),    # вправо
                        }
                paused = False
                os.system('cls' if os.name == 'nt' else 'clear')
                draw(game)
                time.sleep(game.delay)
                while not game.is_over:
                        if msvcrt.kbhit():
                                key = msvcrt.getch()
                                if key in (b'P', b'p'):
                                        paused = not paused
                                        continue
                                if not paused and key == b'\xe0':
                                        key = msvcrt.getch()
                                        direction = DIRECTIONS.get(key)
                                        if direction is not None:
                                                if (current_direction[0] + direction[0],
                                                    current_direction[1] + direction[1]) != (0,0):
                                                 current_direction = direction
                        if not paused:
                                game.step(current_direction)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                draw(game)
                                time.sleep(game.delay)
                        else:
                                print("ПАУЗА")
                                print("Нажмите 'P' для продолжения")
                                time.sleep(1)
                if game.is_victory:
                        print('Победа!')
                else:
                        print('Game Over', f"Score: {game.score}, Level: {game.level}")
                answer = input('Can you start again?(Y/N):')
                if answer.upper() != "Y":
                        break
