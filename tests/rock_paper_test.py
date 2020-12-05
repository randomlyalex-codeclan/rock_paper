import unittest

from app.models.rock_paper import RockPaper
from app.models.player import Player


class RockPaperTest(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Rocky", "Rock")
        self.player2 = Player("Snippy", "Scissors")
        self.player3 = Player("Marty", "Rock")
        self.game = RockPaper(self.player1, self.player2)

    def test_game_exists(self):
        self.assertEqual("Rocky", self.game.player_1.name)

    def test_player1_wins_over_player2(self):
        self.assertEqual(self.player1, self.game.check_winner(
            self.player1, self.player2))

    def test_player1_wins_over_player2__reversed(self):
        self.assertEqual(self.player1, self.game.check_winner(
            self.player2, self.player1))

    def test_draw_returns_none(self):
        self.assertEqual(None, self.game.check_winner(
            self.player1, self.player3))
