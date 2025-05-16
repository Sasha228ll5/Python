import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы экрана
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")


# Класс змейки
class Snake:
    def __init__(self, initial_length=3):
        self.body = [(WIDTH // 2 - i * CELL_SIZE, HEIGHT // 2) for i in range(initial_length)]
        self.direction = RIGHT
        self.growth_size = 0  # Сколько сегментов нужно вырастить

    def move(self):
        x, y = self.body[0]
        new_head = (x + self.direction[0] * CELL_SIZE, y + self.direction[1] * CELL_SIZE)
        if new_head in self.body or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            return False  # Игра окончена
        self.body.insert(0, new_head)
        if self.growth_size > 0:
            self.growth_size -= 1
        else:
            self.body.pop()
        return True

    def grow(self, size=2):  # Можно менять размер роста
        self.growth_size += size

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))


# Класс еды
class Food:
    def __init__(self, count=3):
        self.count = count
        self.positions = [(random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)) for _ in
                          range(self.count)]

    def spawn(self):
        self.positions = [(random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)) for _ in
                          range(self.count)]

    def draw(self):
        for position in self.positions:
            pygame.draw.rect(screen, RED, (*position, CELL_SIZE, CELL_SIZE))


# Главная функция игры
def main():
    clock = pygame.time.Clock()
    initial_snake_length = 5  # Измените значение, чтобы задать начальный размер змейки
    snake = Snake(initial_length=initial_snake_length)
    food = Food()
    running = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        if not snake.move():
            running = False

        for position in food.positions:
            if snake.body[0] == position:
                snake.grow(size=3)  # Измените размер увеличения змейки
                food.spawn()
                break

        snake.draw()
        food.draw()
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()