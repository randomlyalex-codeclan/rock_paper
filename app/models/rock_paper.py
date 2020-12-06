from app.models.player import Player
import random


class RockPaper():

    def __init__(self, player_1, player_2=None):
        self.player_1 = player_1
        self.player_2 = player_2
        self.win_dict = {
            "scissors": "paper",
            "paper": "rock",
            "rock": "scissors"
        }

    def check_winner(self, player_1, player_2):
        if player_1.choice.lower() in self.win_dict.keys() and player_2.choice.lower() in self.win_dict.keys():
            choice1 = player_1.choice.lower()
            choice2 = player_2.choice.lower()
            if self.win_dict.get(choice1) == choice2:
                return player_1
            elif self.win_dict.get(choice2) == choice1:
                return player_2
            else:
                return None
        else:
            return "Not a valid choice"

    def play_computer(self):
        choices_keys_list = list(self.win_dict.keys())
        computer_choice = random.choice(choices_keys_list)
        computer_player = Player("Computer", computer_choice)
        return computer_player
