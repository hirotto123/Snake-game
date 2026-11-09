"""Snake module. Movement, growth and self-collision detection"""


class Snake:
    def __init__(self, start_pos: tuple[int, int], direction: tuple[int, int]):
        """Initialise the snake at start_pos moving in direction"""
        self.body: list[tuple[int, int]] = [start_pos]
        self.direction: tuple[int, int] = direction
        self._should_grow: bool = False

    def head(self) -> tuple[int, int]:
        """Return current position of the head"""
        return self.body[0]

    def move(self, dx: int, dy: int) -> None:
        """Move snake one step"""
        current_head = self.body[0]
        new_head = (current_head[0] + dx, current_head[1] + dy)
        self.body.insert(0, new_head)
        if self._should_grow:
            self._should_grow = False
        else:
            self.body.pop()

    def grow(self) -> None:
        """Grow by 1 segment on yhe next move"""
        self._should_grow = True

    def collides_self(self) -> bool:
        """Check for overlaps head and body"""
        head = self.body[0]
        body_without_head = self.body[1:]
        if head in body_without_head:
            return True
        return False
