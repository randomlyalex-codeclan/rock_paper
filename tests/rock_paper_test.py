import unittest

from app.models.rock_paper import RockPaper
from app.models.player import Player


class RockPaperTest(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Rocky", "Rock")
        self.player2 = Player("Snippy", "Scissors")
        self.game = RockPaper(self.player1, self.player2)
