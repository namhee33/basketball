from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "mikeandkrissecretkey"

team = [
    {'first_name':'Charles' , 'last_name':'Barkley' , 'jersey': 34 },
    {'first_name': 'Michael', 'last_name': 'Jordan' , 'jersey': 23 },
    {'first_name': 'Larry' , 'last_name': 'Bird' , 'jersey': 33 },
    {'first_name': 'Shawn' , 'last_name': 'Kemp' , 'jersey': 40},
    {'first_name': 'Kareem' , 'last_name': 'Abdul-Jabbar' , 'jersey': 33 }]
@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/players') #show us all the players (index)
def index_players():
    return render_template('/players/index.html',team = team)



if __name__ == '__main__':
    app.run(debug=True)
