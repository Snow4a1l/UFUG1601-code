from __future__ import annotations

from dataclasses import dataclass
from random import Random


Position = tuple[int, int]


UP: Position = (0, -1)
DOWN: Position = (0, 1)
LEFT: Position = (-1, 0)
RIGHT: Position = (1, 0)

OPPOSITE_DIRECTIONS = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT,
}


@dataclass(frozen=True)
class GameState:
    width: int
    height: int
    snake: tuple[Position, ...]
    direction: Position
    food: Position
    score: int = 0
    game_over: bool = False


def create_initial_state(width: int = 16, height: int = 16, seed: int = 0) -> GameState:
    if width < 4 or height < 4:
        raise ValueError("Grid must be at least 4x4.")

    center_x = width // 2
    center_y = height // 2
    snake = (
        (center_x, center_y),
        (center_x - 1, center_y),
        (center_x - 2, center_y),
    )
    rng = Random(seed)
    food = place_food(width, height, snake, rng)
    return GameState(
        width=width,
        height=height,
        snake=snake,
        direction=RIGHT,
        food=food,
        score=0,
        game_over=False,
    )


def normalize_direction(current: Position, requested: Position | None) -> Position:
    if requested is None:
        return current
    if requested not in OPPOSITE_DIRECTIONS:
        return current
    if requested == OPPOSITE_DIRECTIONS[current]:
        return current
    return requested


def advance_state(
    state: GameState,
    requested_direction: Position | None = None,
    rng: Random | None = None,
) -> GameState:
    if state.game_over:
        return state

    direction = normalize_direction(state.direction, requested_direction)
    head_x, head_y = state.snake[0]
    delta_x, delta_y = direction
    next_head = (head_x + delta_x, head_y + delta_y)

    if not is_inside_grid(next_head, state.width, state.height):
        return GameState(**{**state.__dict__, "direction": direction, "game_over": True})

    grows = next_head == state.food
    body_to_check = state.snake if grows else state.snake[:-1]
    if next_head in body_to_check:
        return GameState(**{**state.__dict__, "direction": direction, "game_over": True})

    next_snake = (next_head,) + state.snake
    if not grows:
        next_snake = next_snake[:-1]

    next_food = state.food
    next_score = state.score
    if grows:
        random_source = rng or Random()
        next_food = place_food(state.width, state.height, next_snake, random_source)
        next_score += 1

    return GameState(
        width=state.width,
        height=state.height,
        snake=next_snake,
        direction=direction,
        food=next_food,
        score=next_score,
        game_over=False,
    )


def place_food(width: int, height: int, snake: tuple[Position, ...], rng: Random) -> Position:
    free_cells = [
        (x, y)
        for y in range(height)
        for x in range(width)
        if (x, y) not in snake
    ]
    if not free_cells:
        raise ValueError("No free cell available for food.")
    return rng.choice(free_cells)


def is_inside_grid(position: Position, width: int, height: int) -> bool:
    x, y = position
    return 0 <= x < width and 0 <= y < height
