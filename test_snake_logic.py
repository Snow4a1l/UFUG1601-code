import unittest
from random import Random

from snake_logic import LEFT, RIGHT, UP, GameState, advance_state, create_initial_state, place_food


class SnakeLogicTests(unittest.TestCase):
    def test_initial_state_uses_valid_food_and_length(self):
        state = create_initial_state(width=12, height=12, seed=3)
        self.assertEqual(len(state.snake), 3)
        self.assertNotIn(state.food, state.snake)
        self.assertEqual(state.direction, RIGHT)

    def test_move_forward_without_growth(self):
        state = GameState(
            width=8,
            height=8,
            snake=((3, 3), (2, 3), (1, 3)),
            direction=RIGHT,
            food=(0, 0),
        )

        next_state = advance_state(state)

        self.assertEqual(next_state.snake, ((4, 3), (3, 3), (2, 3)))
        self.assertEqual(next_state.score, 0)
        self.assertFalse(next_state.game_over)

    def test_reverse_direction_is_ignored(self):
        state = GameState(
            width=8,
            height=8,
            snake=((3, 3), (2, 3), (1, 3)),
            direction=RIGHT,
            food=(0, 0),
        )

        next_state = advance_state(state, requested_direction=LEFT)

        self.assertEqual(next_state.direction, RIGHT)
        self.assertEqual(next_state.snake[0], (4, 3))

    def test_eating_food_grows_snake_and_scores(self):
        state = GameState(
            width=6,
            height=6,
            snake=((2, 2), (1, 2), (0, 2)),
            direction=RIGHT,
            food=(3, 2),
        )

        next_state = advance_state(state, rng=Random(0))

        self.assertEqual(next_state.snake, ((3, 2), (2, 2), (1, 2), (0, 2)))
        self.assertEqual(next_state.score, 1)
        self.assertNotIn(next_state.food, next_state.snake)

    def test_wall_collision_sets_game_over(self):
        state = GameState(
            width=4,
            height=4,
            snake=((3, 1), (2, 1), (1, 1)),
            direction=RIGHT,
            food=(0, 0),
        )

        next_state = advance_state(state)

        self.assertTrue(next_state.game_over)

    def test_self_collision_sets_game_over(self):
        state = GameState(
            width=6,
            height=6,
            snake=((2, 2), (2, 3), (1, 3), (1, 2), (1, 1), (2, 1)),
            direction=UP,
            food=(5, 5),
        )

        next_state = advance_state(state, requested_direction=LEFT)

        self.assertTrue(next_state.game_over)

    def test_food_placement_uses_only_free_cells(self):
        snake = ((0, 0), (1, 0), (0, 1))
        food = place_food(2, 2, snake, Random(1))
        self.assertEqual(food, (1, 1))


if __name__ == "__main__":
    unittest.main()
