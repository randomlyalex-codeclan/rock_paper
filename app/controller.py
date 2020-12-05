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
