class Snake:
    def __init__(self,start_pos: tuple[int, int], direction: tuple [int, int]):
        self.body: list[tuple[int, int]] = [start_pos]
        self.direction: tuple[int, int] = direction

    def head(self) -> tuple[int, int]:
        return self.body[0]
    def move(self, dx: int, dy: int) -> None:
        current_head = self.body[0]
        new_head = (current_head[0] + dx, current_head[1] + dy)
        self.body.insert(0, new_head)
        self.body.pop()
