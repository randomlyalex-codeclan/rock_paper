from flask import render_template, request, redirect
from app import app
from app.models.rock_paper import RockPaper
from app.models.player import Player


@app.route('/<player_1_choice>/<player_2_choice>')
def mvp(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = RockPaper(player_1, player_2)
    result = game.check_winner(player_1, player_2)
    if result == "Not a valid choice":
        return "Not a valid choice"
    elif result != None:
        return f"Winner is: {result.name} with {result.choice}"
    else:
        return "It is a Draw"


@app.route('/')
def extension():
    return render_template('index.html')


@app.route('/play_game', methods=['POST'])
def play_game():
    player_1_name_input = request.form['player_1_name']
    player_1_choice_input = request.form['player_1_choice']
    player_2_name_input = request.form['player_2_name']
    player_2_choice_input = request.form['player_2_choice']
    player_1 = Player(player_1_name_input, player_1_choice_input)
    player_2 = Player(player_2_name_input, player_2_choice_input)
    game = RockPaper(player_1, player_2)
    result = game.check_winner(player_1, player_2)
    return render_template('results.html', player_1=player_1, player_2=player_2, game=game, result=result)

# @app.route('/add-event', methods=['POST'])
# def add_event():
#   date = request.form['date']
#   # Split the date into a list
#   split_date = date.split('-')
#   # create a new date object
#   date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
#   name = request.form['name']
#   guests = request.form['guests']
#   recurring = True if 'recurring' in request.form else False
#   roomLocation = request.form['roomLocation']
#   description = request.form['description']
#   newevent = Event(date=date, name= name, guests=guests, recurring=recurring, room_location=roomLocation, description=description)
#   add_new_event(newevent)
#   return redirect('/')

# @app.route('/delete/<name>', methods=['POST'])
# def delete(name):
#   delete_event(name)
#   return redirect('/')
