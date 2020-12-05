class Player():
    valid_choices = [
        "rock",
        "paper",
        "scissors"
    ]

    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

    def valid_choice(self):
        return self.choice.lower() in Player.valid_choices
