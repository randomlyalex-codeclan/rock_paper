import unittest

from app.models.rock_paper import RockPaper
from app.models.player import Player


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Rocky", "Rock")
        self.player2 = Player("Snippy", "Scissors")\


    def test_name_exists(self):
        self.assertEqual("Rocky", self.player1.name)

    def test_choice_exists(self):
        self.assertEqual("Scissors", self.player2.choice)
