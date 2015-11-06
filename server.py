from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "mikeandkrissecretkey"

team = [
    {'id': 1,'first_name':'Charles' , 'last_name':'Barkley' , 'jersey': 34 },
    {'id': 2,'first_name': 'Michael', 'last_name': 'Jordan' , 'jersey': 23 },
    {'id': 3,'first_name': 'Larry' , 'last_name': 'Bird' , 'jersey': 33 },
    {'id': 4,'first_name': 'Shawn' , 'last_name': 'Kemp' , 'jersey': 40},
    {'id': 5,'first_name': 'Kareem' , 'last_name': 'Abdul-Jabbar' , 'jersey': 33 }]
#helper functions
def find_player(id):
    for player in session['team']:
        if player['id'] == id:
            return player
    return false

@app.route('/')
def index():
    try:
        session['team']
    except:
        session['team'] = team
    return render_template('/index.html')

@app.route('/players', methods = ['GET']) #show us all the players (index)
def index_players():
    return render_template('/players/index.html',team = session['team'])

@app.route('/players/<int:player_id>', methods = ['GET']) #this will get a player from our player list and show him by ID.
def show(player_id):
    player = find_player(player_id)
    if player:
         return render_template('/players/show.html', player = player)
         #return ends the function :)
    return redirect('/')

@app.route('/players/<int:player_id>/edit')
#this shows a page allowing us to edit
def edit(player_id):
    player = find_player(player_id)
    if player:
         return render_template('/players/edit.html', player = player)
    return redirect('/players/'+str(player_id))

@app.route('/players/<int:player_id>', methods = ['POST'])
def update(player_id):
    player = find_player(player_id)


    player['first_name'] = request.form['first_name']
    player['last_name'] = request.form['last_name']
    player['jersey'] = request.form['jersey']
    try:
        request.form['team']
        player['team'] = request.form['team']
    except:
        print "try and get a contract!"
        #session['team'] == [{},{},{},{}]
    for player_ses in session['team']:
            #player = {}
        if player_ses['id'] == player_id:
            player_ses = player

    print player['first_name']
    print player['last_name']
    print player['jersey']
    try:
        player['team']
        print player['team']
    except:
        print "no team yet"
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
