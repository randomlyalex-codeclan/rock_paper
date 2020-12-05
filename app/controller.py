from flask import render_template, request, redirect
from app import app
from app.models.rock_paper import RockPaper
from app.models.player import Player


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/basic/<player_1_choice>/<player_2_choice>')
def basic(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = RockPaper(player_1, player_2)
    # do the thing here in the models
    # then return the thing from the models to the viewer ie templates page.
    return f"Winner is: {game.check_winner(player_1, player_2).name}"
    # return render_template('basic.html', player_1, player_2)


@app.route('/basic2')
def basic2():
    player_1 = Player("Player 1", "Rock")
    player_2 = Player("Player 2", "Scissors")
    game = RockPaper(player_1, player_2)
    return render_template('basic2.html', player_1=player_1, player_2=player_2)


@app.route('/basic3')
def basic3():
    return render_template('basic3.html')


@app.route('/basic4', methods=['POST'])
def basic4():
    player_1_name_input = request.form['player_1_name']
    player_1_choice_input = request.form['player_1_choice']
    player_2_name_input = request.form['player_2_name']
    player_2_choice_input = request.form['player_2_choice']
    player_1 = Player(player_1_name_input, player_1_choice_input)
    player_2 = Player(player_2_name_input, player_2_choice_input)
    game = RockPaper(player_1, player_2)
    return render_template('basic2.html', player_1=player_1, player_2=player_2)

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
