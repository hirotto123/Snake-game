# Snake Game

Консольная реализация классической игры "Змейка" на Python.

## Требования

- Python 3.10+
- `uv` или `poetry`

## Установка и запуск

1. Установите зависимости:

```bash
uv sync --extra dev
```

2. Запустите игру с параметрами по умолчанию (поле 20x20, скорость 2):

```bash
uv run python -m snake.cli
```

3. Или задайте свои параметры:

```bash
uv run python -m snake.cli --width 15 --height 15 --speed 3
```

## Тесты и проверки качества

```bash
uv run pytest
uv run ruff check snake/
uv run ruff format snake/
```

## Структура проекта

```
snake-game/
├── snake/
│   ├── __init__.py
│   ├── snake.py
│   ├── game.py
│   └── cli.py
├── tests/
│   ├── test_snake.py
│   └── __init__.py
├── .github/workflows/ci.yml
├── pyproject.toml
└── README.md
```