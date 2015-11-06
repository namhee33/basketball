from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "mikeandkrissecretkey"

@app.route('/')
def index():
    return render_template('/index.html')

if __name__ == '__main__':
    app.run(debug=True)
