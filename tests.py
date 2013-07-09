from unittest import TestCase, main as unittest_main
from game import Game, GameOver, IllegalRoll


class CalculationTests(TestCase):

    def test_mail_example(self):
        g = Game()
        rolls = [10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10]
        score = g.full_game(rolls)
        self.assertEqual(score, 193)

    def test_simple(self):
        g = Game()
        rolls = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        score = g.full_game(rolls)
        self.assertEqual(score, 30)

    def test_max(self):
        g = Game()
        rolls = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        score = g.full_game(rolls)
        self.assertEqual(score, 300)

    def test_fail_miserably(self):
        g = Game()
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        score = g.full_game(rolls)
        self.assertEqual(score, 0)


class GameOverTests(TestCase):

    def test_simple(self):
        g = Game()
        rolls = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
        self.assertRaises(GameOver, g.full_game, rolls)

    def test_email_example(self):
        g = Game()
        rolls = [10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10, 0]
        self.assertRaises(GameOver, g.full_game, rolls)


class IllegalRollTests(TestCase):

    def test_simple_11(self):
        g = Game()
        rolls = [11, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        self.assertRaises(IllegalRoll, g.full_game, rolls)

    def test_simple_m1(self):
        g = Game()
        rolls = [1, 2, -1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        self.assertRaises(IllegalRoll, g.full_game, rolls)

    def test_email_example(self):
        g = Game()
        rolls = [10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 11]
        self.assertRaises(IllegalRoll, g.full_game, rolls)


if __name__ == '__main__':
    unittest_main()
